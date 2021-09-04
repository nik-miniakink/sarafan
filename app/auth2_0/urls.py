from django.urls import path
from .views import request_user_activation

urlpatterns = [
    path('users/activation/<str:uid>/<str:token>/', request_user_activation),
]
