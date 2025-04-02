
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HealthcareBackend.settings")
django.setup()
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import requests
from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.tokens import AccessToken

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = await self.authenticate_user()
        if not self.user or isinstance(self.user, AnonymousUser):
            print("WebSocket REJECTED: Authentication failed")
            await self.close()
            return
        print(f"WebSocket CONNECTED: {self.user.username}")
        await self.accept()

        previous_messages = await self.get_previous_messages(self.user)
        user_data = await self.get_user_data(self.user)
        print(user_data)

        await self.send(text_data=json.dumps({"previous_messages": previous_messages}))

    @database_sync_to_async
    def get_previous_messages(self, user):
        from chat.models import ChatMessage
        messages = ChatMessage.objects.filter(user=user).order_by("timestamp")[:10]
        return json.dumps([
            {"message": msg.message, "response": msg.response}
            for msg in messages
        ])

    async def disconnect(self, code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        user_message = data.get("message", "")
        message_id = data.get("message_id", None)
        
        if not user_message:
            await self.send(text_data=json.dumps({"error": "Message cannot be empty"}))
            return

        user_data = await self.get_user_data(self.user)
        previous_messages = json.loads(await self.get_previous_messages(self.user))
        
        response_text = await self.call_retrieve_api(previous_messages, user_message, user_data)
        print(response_text)
        
        await self.send(json.dumps({"message": response_text, "message_id": message_id, "streaming": False}))

        if response_text != "I'm facing technical issues. Please try again later." or response_text != "I'm sorry, but I couldn't process your request.":
            chat = await self.create_chat_message(self.user, user_message, response_text)
            await self.update_chat_response(chat, response_text)

    @database_sync_to_async
    def create_chat_message(self, user, message, response):
        from chat.models import ChatMessage
        return ChatMessage.objects.create(user=user, message=message, response=response)

    @database_sync_to_async
    def update_chat_response(self, chat, response):
        chat.response = response
        chat.save()

    async def authenticate_user(self):
        query_params = parse_qs(self.scope["query_string"].decode())
        token = query_params.get("token", [None])[0]
        if not token:
            print("No JWT token found in WebSocket URL")
            return AnonymousUser()
        try:
            access_token = AccessToken(token)
            user = await self.get_user(access_token["user_id"])
            print(f"Authenticated user: {user.username}" if user else "User not found")
            return user if user else AnonymousUser()
        except Exception as e:
            print(f"JWT Authentication failed: {e}")
            return AnonymousUser()

    @database_sync_to_async
    def get_user(self, user_id):
        from users.models import CustomUser
        try:
            return CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return None
    
    @database_sync_to_async
    def get_user_data(self, user):
        from healthcare.models import GeneralHealthForm
        try:
            form = GeneralHealthForm.objects.get(user=user)
            return {"state": form.state, "gender": form.gender}
        except GeneralHealthForm.DoesNotExist:
            return {"state": None, "gender": None}
    
    async def call_retrieve_api(self, previous_messages, user_message, user_data):
        url = "https://arpit-bansal-healthbridge.hf.space/retrieve"
        payload = {
            "previous_state": previous_messages,
            "query": user_message,
            "user_data": user_data
        }
        print("Final Payload Sent:", json.dumps(payload, indent=2))
        
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            print(response_data)
            return response_data.get("response", "I'm sorry, but I couldn't process your request.")
        except requests.exceptions.RequestException as e:
            print(f"Error calling AI retrieval API: {e}")
            return "I'm facing technical issues. Please try again later."
