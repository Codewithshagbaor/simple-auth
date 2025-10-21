from django.urls import path
from .views import UserRegistrationView, EmailLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', EmailLoginView.as_view(), name='email-login'),
]