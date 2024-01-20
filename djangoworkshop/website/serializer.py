from rest_framework import serializers
from .models import Room, Meeting

class RoomSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Room
        fields = '__all__'

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'
