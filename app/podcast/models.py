from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Avg

class Podcast(models.Model):
    pod_name = models.CharField(max_length=200)
    pod_prod = models.CharField(max_length=200)
    pod_pic = models.ImageField(default='placeholder.png', blank=True)
    description = models.TextField()
    slide1 = models.ImageField(default='placeholder.png', blank=True)
    slide2 = models.ImageField(default='placeholder.png', blank=True)
    slide3 = models.ImageField(default='placeholder.png', blank=True)
    twitter_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    spotify_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.pod_name

    def get_absolute_url(self):
        return reverse('podcastdetail', kwargs={'pk': self.pk})

    def average_rating(self):
        ratings = self.rating_set.all()
        if ratings.exists():
            return ratings.aggregate(Avg('rating'))['rating__avg']
        else:
            return None
    
    def get_comments(self):
        return self.rating_set.exclude(comment__exact='').values_list('comment', 'user__username', 'rating')

    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)

    class Meta:
        unique_together = ('user', 'podcast')