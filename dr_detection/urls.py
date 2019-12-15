from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    
	#Plug and play module
    path('', include('DRDetection.urls')),


    path('admin/', admin.site.urls),
]