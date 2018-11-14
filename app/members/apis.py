from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from snippets.serializers import UserSerializer


class AuthTokenView(APIView):
    # URL: '/members/auth-token'
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            # 인증에 성공하면 토큰을 생성하거나 가져와서 Response에 전달
            token, __ = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
            }
            return Response(data)
        raise AuthenticationFailed()


class ProfileView(APIView):
    # URL: '/members/profile/'
    permission_classes = (permissions.IsAuthenticated, )
    def get(self, request):
        return Response(UserSerializer(request.user).data)
