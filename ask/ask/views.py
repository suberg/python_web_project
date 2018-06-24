from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
def not_found(request):
  return HttpResponseNotFound("Found!")

def found(request):
  return HttpResponse("Not Found!")