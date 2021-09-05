from django.urls import path
from app.auth2_0.views import request_user_activation

urlpatterns = [
    path('users/activation/<str:uid>/<str:token>/', request_user_activation),
]
