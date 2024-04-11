from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.PodcastList.as_view(), name='podlist'),
    path("create/", views.PodcastCreate.as_view(), name="podcastcreate"),
    path("<pk>/", views.PodcastDetail.as_view(), name="podcastdetail"),
]

