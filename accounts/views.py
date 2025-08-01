from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from . import models
from . import serializers

class RegisterViewSet(APIView):
    def get(self, request):
        return Response("Register(GET)")
    
    def post(self, request):
        serializer = serializers.UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Registration successful.")
        return Response(serializer.errors)
    
class LoginViewSet(APIView):
    def get(self, request):
        return Response("Login(GET)")
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username = username, password = password)

        if user is not None:
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        user_exists = models.CustomUser.objects.filter(username = username).exists()

        if user_exists is not None:
            return Response("Incorrect password.")
        return Response("User does not exists.")