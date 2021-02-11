from django.shortcuts import render
from django.http import HttpResponse
from webpage import models
# Create your views here.

def index(request):

  main_template = 'index.html'

  if request.path == "/date_sorted_new":
    posts_result = models.Posts.objects.all().order_by('-date')
  elif request.path == "/date_sorted_old":
    posts_result = models.Posts.objects.all().order_by('date')
  elif request.path == "/name_sorted":
    posts_result = models.Posts.objects.all().order_by('title')
  elif request.path == "/last_three":
    posts_result = models.Posts.objects.all()[:3]
  else:
    posts_result = models.Posts.objects.all()

  context = {'posts_result': posts_result}

  return render(request, main_template, context)