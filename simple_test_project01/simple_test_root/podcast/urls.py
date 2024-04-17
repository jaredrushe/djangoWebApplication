from django.urls import path
from . import views

urlpatterns = [
    path('', views.PodcastList.as_view(), name='podlist'),
    path("create/", views.PodcastCreate.as_view(), name="podcastcreate"),
    path("<int:pk>/", views.PodcastDetail.as_view(), name="podcastdetail"),
    path("podcast/update/<int:pk>/", views.PodcastUpdate.as_view(), name="podcastupdate"),
    path("podcast/delete/<int:pk>/", views.PodcastDelete.as_view(), name="podcastdelete"),
    path('rate/<int:podcast_id>/', views.rate_podcast, name='rate_podcast'),
]



