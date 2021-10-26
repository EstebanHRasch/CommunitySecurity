from rest_framework import serializers
from .models import Camera, Footage, access_instance

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ('id', 'coordinates', 'live_stream')


class FootageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footage
        fields = ('id', 'camera', 'date', 'time', 'URL', 'thumbnail')


class access_instanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = access_instance
        fields = ('id', 'accessed_camera', 'accessed_footage', 'accessed_camera_location', 'accessed_footage_date', 'accessed_footage_time', 'date', 'time', 'username')
