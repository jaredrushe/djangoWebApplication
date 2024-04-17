from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Podcast
from .forms import RatingForm

class PodcastCreate(CreateView):
    model = Podcast
    template_name = 'podcast/podcast_create_form.html'
    fields = ["pod_name", "pod_pic", "description", "slide1", "slide2", "slide3", "twitter_link", "youtube_link", "spotify_link"]


class PodcastUpdate(UpdateView):
    model = Podcast
    template_name = "podcast/pod_update_form.html"
    fields = ["pod_name", "pod_pic", "description", "slide1", "slide2", "slide3", "twitter_link", "youtube_link", "spotify_link"]


class PodcastDelete(DeleteView):
    model = Podcast
    template_name = "podcast/pod_delete_form.html"
    success_url = reverse_lazy("podlist")


class PodcastList(ListView):
    model = Podcast
    template_name = 'podcast/podcast_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        podcast_list = context['object_list']

        unique_producers = set()
        for podcast in podcast_list:
            if podcast.pod_prod not in unique_producers:
                unique_producers.add(podcast.pod_prod)

        context['unique_producers'] = unique_producers
        return context

class PodcastDetail(DetailView):
    model = Podcast
    template_name = 'podcast/podcast_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        podcast = self.get_object()
        context['comments'] = podcast.get_comments()
        return context

def home(request):
    return render(request, 'podcast/home.html')

def rate_podcast(request, podcast_id):
    podcast = Podcast.objects.get(pk=podcast_id)
    try:
        rating = Rating.objects.get(user=request.user, podcast=podcast)
    except Rating.DoesNotExist:
        rating = None

    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.podcast = podcast
            rating.save()
            return redirect('podcastdetail', pk=podcast_id)
    else:
        form = RatingForm(instance=rating)
    return render(request, 'podcast/rate_podcast.html', {'form': form, 'podcast': podcast})

