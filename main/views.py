from django.shortcuts import render
from django.conf import settings


# Create your views here.
def index(request):
    
    context={
        "name":settings.DATA["name"],
        "ha":settings.DATA["ha"]
    }
    response=render(request,'main\index.html',context)
    return response

def projects(request):
    context={}
    response=render(request,'main\projects.html',context)
    return response


def experience(request):
    context={}
    response=render(request,'main\experience.html',context)
    return response