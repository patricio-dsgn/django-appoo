from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def hello(request):
  return HttpResponse("Hello, World! i'm <b>appoo project</b>")




from django.shortcuts import render
def home(request):
  return render(request,'web/home.html')

from django.shortcuts import render
def escala(request):
  return render(request,'web/escala.html')

from django.shortcuts import render
def recomendaciones(request):
  return render(request,'web/recomendaciones.html')

from django.shortcuts import render
def blog(request):
  return render(request,'web/blog.html')

from django.shortcuts import render
def enlaces(request):
  return render(request,'web/enlaces.html')

from django.shortcuts import render
def fotos(request):
  return render(request,'web/fotos.html')