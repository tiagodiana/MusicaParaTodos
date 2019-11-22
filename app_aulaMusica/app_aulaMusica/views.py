from django.shortcuts import render, redirect


def index(request):
    return render(request, 'app_aulaMusica/index.html')

