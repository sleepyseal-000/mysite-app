from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. (View our webpages)

def homepage(request):
    return render(request,'index.html')
