from django.shortcuts import render
from .utility import *
from .forms import *


from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages



# home page
def index(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)

# crop image
@csrf_exempt
def cropImage(request):
    template_name = 'crop-image.html'
    form = None
    if request.method == 'POST':
        pass

    context = {
        "form": form
    }
    return render(request, template_name, context)

import json
@csrf_exempt
def uploadImage(request):
    fs = FileSystemStorage()
    try:
        if request.method == 'POST':
            printStar()
            file_obj = json.loads(request.POST.get('cropped_image'))
            file_name = 'email_cover_image.png'
            
            
            print("file_obj: ", file_obj)
            print("file_name: ", file_name)
            f = file_obj
            with open(f.name, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
            

            # filename = fs.save(file_name, file_obj)
            # file_path = fs.url(filename)
            printStar()

            return JsonResponse({
                'status': 'success',
                'message': 'Image Uploaded Successfully',
                'url': file_path
            })
    except Exception as E:
        print(E)
    return JsonResponse({
        'status': 'failed',
        'message': 'failed_to_upload_image'
    })

########################################################



# class ImageCropper(View):
#     def get(self, request):
#         return render(request, 'crop-image.html')


# @csrf_exempt
# def uploadImage(request):
#     fs = FileSystemStorage()
#     try:
#         if request.FILES.get('cropped_image'):
#             file_obj = request.FILES['cropped_image']
#             file_name = 'email_cover_image.png'
#             filename = fs.save(file_name, file_obj)
#             file_path = fs.url(filename)
#             return JsonResponse({
#                 'status': 'success',
#                 'message': 'Image Uploaded Successfully',
#                 'url': file_path
#             })
#     except Exception as E:
#         print(E)
#     return JsonResponse({
#         'status': 'failed',
#         'message': 'failed_to_upload_image'
#     })
