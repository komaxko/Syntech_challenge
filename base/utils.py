from django.contrib.auth import get_user_model
from django.core.cache import cache
from rest_framework_simplejwt.tokens import RefreshToken


def create_user(username='user', password='password', email='test@domain.com'):
    User = get_user_model()
    user = User.objects.create_user(username=username, password=password, email=email)
    return user


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    access = str(refresh.access_token)
    cache.set(access, True, timeout=60 * 60)

    return {
        'refresh': str(refresh),
        'access': access,
    }
