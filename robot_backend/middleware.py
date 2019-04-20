
import json

from robot_status_cli.base import verify_token

from .models import UserSecretModel


class RobotBackendMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not request.user.is_authenticated():
            self.check_user_login_by_token(request)
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    def check_user_login_by_token(self, request):
        authorization = request.META.get("HTTP_AUTHORIZATION", None)
        public_key = request.META.get("HTTP_PUBLIC_KEY", None)
        timestamp = request.META.get("HTTP_TIMESTAMP", None)
        if not authorization:
            return
        token = self.get_token(authorization)
        if not token or not public_key or not timestamp:
            return
        user_secret = UserSecretModel.objects.filter(public_key=public_key, active=True)
        if not user_secret.exists():
            return
        user_secret = user_secret[:1][0]
        secret_key = user_secret.secret_key
        try:
            verify_token(secret_key, json.dumps({"timestamp": timestamp}), token)
            request.user = user_secret.user
        except Exception as e:
            pass

    def get_token(self, authotization):
        auth = authotization.split()
        if not auth or not len(auth) == 2 or auth[0].lower() != 'bearer':
            return None
        return auth[1]