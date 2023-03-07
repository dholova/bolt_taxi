from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Знайдемо користувача за email
        User = get_user_model()
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None

        # Перевіримо пароль користувача
        if user.check_password(password):
            return user

    def get_user(self, user_id):
        # Отримаємо користувача за його ID
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
