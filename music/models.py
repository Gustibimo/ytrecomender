from django.db import models

# Create your models here.

class NewVideo(models.Model):
    MOOD_TYPE = (
        ('HAPPY', 'Happy'),
        ('LOVE', 'Love'),
        ('SAD', 'Sad'),
        ('CHILL', 'Chill'),
        ('WORKOUT', 'workout')
    )

    video_title = models.TextField(db_index=True, null=True, blank=True)
    video_id = models.CharField(max_length=11, null=False, primary_key=True)
    moods = models.CharField(choices=MOOD_TYPE, max_length=20, default='HAPPY')
    video_description = models.TextField(null=True, blank=True)
    predicted_moods = models.CharField(max_length=17, null=True, blank=True)

    def __str__(self):
        return self.video_title