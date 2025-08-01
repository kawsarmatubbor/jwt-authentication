from rest_framework.views import APIView
from rest_framework.response import Response
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