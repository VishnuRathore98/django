import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from pytube import YouTube
import os
from django.conf import settings
import assemblyai as aai 

@login_required
def index(request):
    return render(request, 'index.html') 
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = 'username or password incorrect'
            return render(request, 'login.html', {'error_message':error_message})

    return render(request, 'login.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']

        if password == repeatPassword:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                return redirect('/')
            except:
                error_message = 'Error creating user! Please try again'
                return render(request, 'signup.html', {'error_message':error_message})
        else:
            error_message = 'password did not matched!'
            return render(request, 'signup.html', {'error_message':error_message})
        
    return render(request, 'signup.html')

def user_logout(request):
    logout(request)
    return redirect('/')

@csrf_exempt 
def generate_blog(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body) 
            yt_link = data['link']
            
            #title
            title = get_yt_title(yt_link)
            #transcript
            transcript = get_video_transcript(yt_link)
            #blog

            #save blog

            #return blog


            return JsonResponse({'content':transcript})
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error_message':'Invalid data sent'}, status=400)

    else:
        return JsonResponse({'error_message': 'not a valid request method'}, status=405)

def get_yt_title(link: str):
    yt = YouTube(link)
    title = yt.title
    return title

def download_audio(link: str):
    yt = YouTube(link)
    audio = yt.streams.filter(only_audio=True).first()
    out_audio_file = audio.download(output_path=settings.MEDIA_ROOT)
    base, ext = os.path.splitext(out_audio_file)
    new_file = base+'.mp3'
    os.rename(out_audio_file, new_file)
    return new_file

def get_video_transcript(link):
    audio_file = download_audio(link)
    aai.settings.api_key = ''

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_file)

    return transcript.text
