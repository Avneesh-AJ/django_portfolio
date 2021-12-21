from django.urls import path
from main import views

urlpatterns=[
    path('projects/',views.projects,name='projects'),
    path('experience/',views.experience,name='experience'),
    path('',views.index,name='index')
   
]