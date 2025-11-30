from django.contrib import admin
from .models import VideoReport, ProfileReport, BugReport, Suggestion

@admin.register(VideoReport)
class VideoReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_sent', 'reporter', 'post__id')
    search_fields = ['id', 'date_sent', 'reporter', 'post__id']

@admin.register(ProfileReport)
class ProfileReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_sent', 'reporter', 'profile__id')
    search_fields = ['id', 'date_sent', 'reporter', 'profile__id']

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_sent', 'reporter')
    search_fields = ['id', 'date_sent', 'reporter']

@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_sent', 'reporter')
    search_fields = ['id', 'date_sent', 'reporter']