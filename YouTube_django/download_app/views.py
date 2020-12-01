from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import NewMP3
from .forms import MP3Form
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from pytube import YouTube
import os

# Create your views here.
video_url = ''
class HomeView(LoginRequiredMixin, ListView):
    model = NewMP3

    def get_query(self):
        queryset = NewMP3.objects.all().filter(user=self.request.user)
        return queryset


    template_name = "download_app/home.html"


def download(request):
    #"https://www.youtube.com/watch?v=AIR5XPWK3Vk"
    # video_url = str(request.GET.get('url'))
    # if request.method == "POST":
        

    #   video_info = YoutubeDL().extract_info(url=video_url)

    #   filename = f"{video_info['title']}.mp3"

    #   options = {
    #       'format': 'bestaudio/best',
    #       'keepvideo': False,
    #       'outtmpl': filename,
    #       'postprocessors': [{
    #           'key':'FFmpegExtractAudio',
    #           'preferredcodec': 'mp3',
    #           'preferredquality': '192'
    #           }]
    #   }

    #   homedir = os.path.expanduser('~') + '/Downloads'

    #   with youtube_dl.YoutubeDL(options) as ydl:
    #       ydl.download(homedir, [video_url])
    global video_url
    if request.method == 'POST':
        video_url=request.POST['video_url']
        yt = YouTube(video_url)
        thumbnail_url = yt.thumbnail_url
        title = yt.title
        length = yt.length
        desc = yt.description
        view = yt.views
        rating = yt.rating
        age_restricted = yt.age_restricted
        return render(request,'download_app/download_mp3.html',{"title":title,"thumbnail_url":thumbnail_url,"video_url":video_url})
        
    else:
        return render(request,'download_app/home.html')

def downloading(request):
    global video_url
    if request.method == 'POST':
        
        yt = YouTube(video_url)
        
        yt.streams.first().download(os.path.expanduser('~') + '/Downloads')

        return render(request,'download_app/complate.html', {"msg":"downloading completed"})
    