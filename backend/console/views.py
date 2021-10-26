# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
# Create your views here.
from django.template import loader
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic, View
from django.views.generic import TemplateView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from .serializers import CameraSerializer, FootageSerializer, access_instanceSerializer
from .models import Camera, Footage, SignUpForm, access_instance
from rest_framework import generics, views
from rest_framework.response import Response

class CameraView(generics.ListCreateAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer

class FootageView(views.APIView):

    def get(self, request, *args, **kwargs):
        cameraId = kwargs['camera_id']
        footageDate = kwargs['footage_date']
        footage = Footage.objects.filter(camera = cameraId)
        footage = footage.filter(date = footageDate)
        serializer = FootageSerializer(footage, many=True)
        return Response(serializer.data)

class access_instanceView(views.APIView):

    def get(self, request, *args, **kwargs):
        cameraId = kwargs['camera_id']
        access_object = access_instance.objects.filter(accessed_camera = cameraId)
        serializer = access_instanceSerializer(access_object, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = access_instanceSerializer(data=request.data)
        print (request)
        if serializer.is_valid():
            username = serializer.data.get('username')

            accessed_camera = serializer.data.get('accessed_camera')
            accessed_camera = Camera.objects.get(pk = accessed_camera)
            
            accessed_footage = serializer.data.get('accessed_footage')
            accessed_footage = Footage.objects.get(pk = accessed_footage)

            accessed_location = accessed_camera.coordinates
            accessed_date = accessed_footage.date
            accessed_time = accessed_footage.time

            access_object = access_instance(
                username = username, 
                accessed_camera = accessed_camera,
                accessed_footage = accessed_footage,
                accessed_camera_location = accessed_location,
                accessed_footage_date = accessed_date,
                accessed_footage_time = accessed_time
            )

            access_object.save()
        message = "Access instance successfully posted!"
        return Response({'message': message})