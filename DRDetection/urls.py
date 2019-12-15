from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from . import views

app_name = 'DRDetection'

urlpatterns = [

    path('', views.index, name='index'),
    
    path('result/<int:stage_id>/', views.resultview, name='resultview'),
    path('result/', views.resultview, name='resultview'),

    path('example/', views.samplewebpage, name='example'),

]
  