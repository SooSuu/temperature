from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def graph(request):
  return render(request, 'graph.html')


def alarm(request):
  return render(request, 'alarm.html')


def camera(request):
  return render(request, 'camera.html')


def info(request):
  return render(request, 'info.html')
