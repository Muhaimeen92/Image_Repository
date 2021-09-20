from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import Image
from .helpers import handle_uploaded_file, upload_new_image
from ImageRepository.settings import MEDIA_URL
import os

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        images = Image.objects.all()
        current_user = request.user
        return render(request, "images/index.html", {
            "images": images,
            "current_user": current_user
        })

def add(request):
    if request.method == "POST":
        file_name = str(request.FILES['image_file'])
        handle_uploaded_file(request.FILES['image_file'], file_name)
        upload_new_image(request, file_name)
        return HttpResponseRedirect(reverse('index'))

def delete(request):
    if request.method == "POST":
        image_id = request.POST['image_id']
        image_to_delete = Image.objects.get(id=image_id)
        delete_media('media/' + str(image_to_delete.image))
        image_to_delete.delete()
        return HttpResponseRedirect(reverse('index'))

def delete_media(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "images/login.html", {
                'message': "Invalid Credentials"
            })
    else:
        return render(request, "images/login.html")

def logout_view(request):
    logout(request)
    return render(request, "images/login.html", {
        "message": "Logged Out"
    })