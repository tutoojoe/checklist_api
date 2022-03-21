
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserRegisterSerializer

from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


class RegisterAPIView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request,format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            # token generation
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
                }
            # we are sending token instead of serialized data
            # serializer_data = serializer.data
            return Response(response_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    def post(self, request, format = None):
        # Details from jwt settings
        try:
            refresh_token = request.data.get('refresh_token')
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist() 
            return Response({'message':'successfully logged out'},status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

