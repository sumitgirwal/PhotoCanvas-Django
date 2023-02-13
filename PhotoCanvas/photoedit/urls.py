from django.urls import path 
from . import views

urlpatterns = [
    
    path('', views.index , name='home'),
    path('crop-image', views.cropImage , name='crop_image'),
    path('upload-image', views.uploadImage, name='upload_image'),

]
