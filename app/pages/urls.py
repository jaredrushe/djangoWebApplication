from django.urls import path  # Add 'include' import here
from . import views


urlpatterns = [
    path('contact/', views.contact, name='contact'),      # Include 'include' here
    path('<str:pagename>/', views.index, name='index'),
    path('', views.index, name='index'),
]
