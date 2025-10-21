from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()

class EmailAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        email = kwargs.get('email')
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
        