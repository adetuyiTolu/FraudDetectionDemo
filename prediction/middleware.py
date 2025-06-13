import logging

logger = logging.getLogger("django.request")


class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")
        user_agent = request.META.get("HTTP_USER_AGENT", "")
        path = request.get_full_path()

        logger.info(f"[REQUEST] IP={ip}, Path={path}, UA={user_agent}")

        response = self.get_response(request)

        return response
