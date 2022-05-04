from django.shortcuts import render,redirect
from web.models import Funfact,Scale,Tip,Post,Link,Photo

from random import randint


# Create your views here.

# from django.http import HttpResponse
# def hello(request):
#   return HttpResponse("Hello, World! i'm <b>appoo project</b>")


def home(request):
  # query_funfacts = Funfact.objects.all()
  len_obj = len(Funfact.objects.all())
  query_funfacts = Funfact.objects.all()[randint(0, len_obj-1)]
  # value = randint(0, 10)
  return render(request,'web/home.html',{'query_funfacts':query_funfacts})
  


def escala(request):
  return render(request,'web/escala.html')

def recomendaciones(request):
  return render(request,'web/recomendaciones.html')

def blog(request):
  return render(request,'web/blog.html')

def enlaces(request):
  return render(request,'web/enlaces.html')

def fotos(request):
  return render(request,'web/fotos.html')