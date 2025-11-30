from .models import Video
from django.utils import timezone
from datetime import timedelta

def reset_recommendations():
    Video.recommendations.through.objects.all().delete()

def recalculate_score():
    videos = Video.objects.select_related('uploader').prefetch_related('likes', 'dislikes')
    now = timezone.now()

    for video in videos:
        days = (now - video.date_posted).days
        like_count = video.likes.count()
        dislike_count = video.dislikes.count()
        total_votes = like_count + dislike_count

        likeratio = like_count / total_votes if total_votes > 0 else 1
        if likeratio == 0:
            likeratio += 1

        if video.duration > 180 and video.category != "Meme":
            video.score = round((video.recommendations.count() * (video.uploader.rating + (days / 30))) * (likeratio), 1)
        else:
            video.score = video.recommendations.count()

    Video.objects.bulk_update(videos, ['score'])
