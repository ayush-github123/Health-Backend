# from chat.websocket.consumers import ChatConsumer
# from users.models import CustomUser

# user = CustomUser.objects.get(username="user1")
# print(user.is_active)

# list1 = []
# def RetreiveChat():
#     from chat.models import ChatMessage  # Import to avoid circular import issues
#     messages = ChatMessage.objects.filter(user=user).order_by("timestamp")[:20]
#     for message in messages:
#         list1.append(f"Message : {message.message} || Response : {message.response}")
#     return list1



# print(RetreiveChat())

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HealthcareBackend.settings")
django.setup()
import asyncio
from channels.db import database_sync_to_async
from users.models import CustomUser
from chat.websocket.consumers import ChatConsumer

@database_sync_to_async
def get_user(username):
    return CustomUser.objects.get(username=username)

async def retrieve_and_print_messages():
    user = await get_user("user1")
    consumer = ChatConsumer()
    messages = await consumer.get_previous_messages(user)
    for message in messages:
        print(f"Message: {message['message']} || Response: {message['response']} || Timestamp: {message['timestamp']}")

# Run the asynchronous function
asyncio.run(retrieve_and_print_messages())