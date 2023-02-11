from django.shortcuts import render
from .utility import *
from .forms import *

# home page
def index(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)

# crop image
def cropImage(request):
    template_name = 'crop-image.html'
    form = None
    if request.method == 'POST':
        pass

    context = {
        "form": form
    }
    return render(request, template_name, context)




