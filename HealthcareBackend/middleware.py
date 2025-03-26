import logging
from django.http import HttpResponseForbidden
from django.conf import settings

logger = logging.getLogger(__name__)

class RestrictAdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        admin_url = "/secure-admin-panel/"  # Update if you changed the admin URL
        user_ip = request.META.get("REMOTE_ADDR")

        logger.info(f"User IP: {user_ip}, Allowed: {settings.ALLOWED_ADMIN_IPS}")

        if request.path.startswith(admin_url):
            if user_ip not in settings.ALLOWED_ADMIN_IPS:
                logger.warning(f"Access Denied for IP: {user_ip}")
                return HttpResponseForbidden("Access Denied")

        return self.get_response(request)
