from django.shortcuts import render

from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, RetrieveAPIView, GenericAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken

from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status

from .models import Profile
from .serializers import ProfileCreateSerializer


# Create your views here.

class ProfileCreateView(CreateAPIView):
    model = Profile
    serializer_class = ProfileCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = ProfileCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, create = Token.objects.get_or_create(user=serializer.instance)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)
