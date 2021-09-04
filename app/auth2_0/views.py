from rest_framework import permissions
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

import requests

@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def request_user_activation(request, uid, token):
    """
    Активирует акаунт пользователя по ссылке, отправленной на email
    """
    post_url = "http://127.0.0.1:8000/auth/users/activation/"
    post_data = {"uid": uid, "token": token}
    result = requests.post(post_url, data=post_data)
    content = result.text
    return Response(content)
