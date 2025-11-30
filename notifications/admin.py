from django.contrib import admin
from .models import VideoNotification, BaseNotification, UpdateNotification, CommentNotification, MilestoneNotification, MiscellaneousNotification

@admin.register(VideoNotification)
class VideoNotificationAdmin(admin.ModelAdmin):
    list_display = ['video__id', 'message']
    search_fields = ['video__id', 'message']

@admin.register(UpdateNotification)
class UpdateNotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'message']
    search_fields = ['id', 'message']

@admin.register(CommentNotification)
class CommentNotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'message']
    search_fields = ['id', 'message']

@admin.register(MilestoneNotification)
class MilestoneNotificationAdmin(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ['id']

@admin.register(MiscellaneousNotification)
class MiscellaneousNotificationAdmin(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ['id']

@admin.register(BaseNotification)
class BaseNotificationAdmin(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ['id']