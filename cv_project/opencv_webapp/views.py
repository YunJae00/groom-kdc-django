from django.shortcuts import render

from .forms import SimpleUploadForm


# Create your views here.
def first_view(request):
    return render(request, 'opencv_webapp/first_view.html', {})


def simple_upload(request):
    form = SimpleUploadForm()
    context = {'form': form}
    return render(request, 'opencv_webapp/simple_upload.html', context)
