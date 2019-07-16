from django.contrib import admin

# Register your models here.

from .models import NewVideo

class NewVideoAdmin(admin.ModelAdmin):
    list_display = [
        'video_id',
        'video_title',
        'moods',
        'labeled',
        'predicted_moods',
    ]
    search_fields = [
        'video_id',
        'video_title',
        'moods',
    ]
    list_editable = [
        'moods',
        'labeled',
    ]

admin.site.register(NewVideo, NewVideoAdmin)