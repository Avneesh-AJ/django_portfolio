from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    response=render(request,'main\index.html',context)
    return response