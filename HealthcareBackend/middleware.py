import logging
from django.http import HttpResponseForbidden
from django.conf import settings

logger = logging.getLogger(__name__)

class RestrictAdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        admin_url = "/secure-admin-panel/"  # Change this if admin URL is different

        # Get the real user IP (handle proxy headers)
        if request.META.get("HTTP_X_FORWARDED_FOR"):
            user_ip = request.META["HTTP_X_FORWARDED_FOR"].split(",")[0].strip()
        else:
            user_ip = request.META.get("REMOTE_ADDR", "").strip()

        logger.info(f"User IP: {user_ip}, Allowed: {settings.ALLOWED_ADMIN_IPS}")

        # Allow local access when running locally
        # if settings.DEBUG and user_ip in ("127.0.0.1", "localhost"):
        #     return self.get_response(request)

        # Restrict access to the admin panel
        if request.path.startswith(admin_url):
            if user_ip not in settings.ALLOWED_ADMIN_IPS:
                logger.warning(f"Access Denied for IP: {user_ip}")
                return HttpResponseForbidden("Access Denied")

        return self.get_response(request)
