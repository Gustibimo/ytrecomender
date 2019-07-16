from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import generics
from music.models import NewVideo
from .serializers import NewVideoSerializer
# Create your views here.
class NewVideoAPIView(generics.ListCreateAPIView):
 queryset = NewVideo.objects.all()
 serializer_class = NewVideoSerializer