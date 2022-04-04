from django.shortcuts import render
from rest_framework import generics,status
from .serializers import *
from rest_framework.response import Response

# Create your views here.
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    # handle user post data
    def post(self,request):
        user = request.data
        # send user data to the serializer
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        return Response(user_data,status=status.HTTP_201_CREATED)
