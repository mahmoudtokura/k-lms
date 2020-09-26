from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Video

# Create your views here.
class VideoListView(ListView):
    model = Video
    context_object_name = "video_list"
    template_name = "video_list.html"
