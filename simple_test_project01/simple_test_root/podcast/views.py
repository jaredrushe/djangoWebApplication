from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Podcast

def home(request):
    return render(request, 'podcast/home.html')

class PodcastList(ListView):
    model = Podcast
    template_name = 'podcast/podcast_list.html'

class PodcastCreate(CreateView):
    model = Podcast
    template_name = 'podcast/podcast_create_form.html'
    fields = ["pod_name", "pod_type"]

class PodcastDetail(DetailView):
    model = Podcast
    template_name = 'podcast/podcast_detail.html'