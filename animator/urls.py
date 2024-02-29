from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.index, name='home'),
    path('up', views.upload_images, name='images')
]
