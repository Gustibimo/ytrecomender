from rest_framework import serializers
from music.models import NewVideo
class NewVideoSerializer(serializers.ModelSerializer):
 class Meta:
  model = NewVideo
  fields = [
   'video_title',
   'video_id',
   'moods',
  ]