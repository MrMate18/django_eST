from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

from rest_framework import viewsets
from .serializer import MeetingSerializer
from .models import Meeting

# Create your views here.

def welcome (request):
    return HttpResponse("Welcome To Django Workshop!" + str(datetime.now()))

class MeetingView(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


