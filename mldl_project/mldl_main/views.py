from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .predict_ML import predict_iris_one
from .predict_DL import predict_mnist_one

# Create your views here.

def index(request):
    return render(request, 'mldl_main/index.html', {})


def ml_iris(request):
    return render(request, 'mldl_main/ml_iris.html', {})

def predict_iris(request):

    sepal_length = float(request.POST['sepal_length']) if request.POST['sepal_length'] != '' else 5.8
    sepal_width  = float(request.POST['sepal_width'])  if request.POST['sepal_width']  != '' else 2.8
    petal_length = float(request.POST['petal_length']) if request.POST['petal_length'] != '' else 5.1
    petal_width  = float(request.POST['petal_width'])  if request.POST['petal_width']  != '' else 2.4
    data_1d_array = [sepal_length, sepal_width, petal_length, petal_width]

    predict_result = predict_iris_one(data_1d_array)

    context = {'predict_result' : predict_result}
    return render(request, 'mldl_main/ml_iris_result.html', context)


def dl_mnist(request):
    return render(request, 'mldl_main/dl_mnist.html', {})

def predict_mnist(request):

    uploaded_file = request.FILES['img_uploaded']

    # OpenCV error occurs when file's name has Korean character or white-spaces
    uploaded_file.name = uploaded_file.name.replace(' ', '')

    fs = FileSystemStorage()
    uploaded_filename = fs.save(uploaded_file.name, uploaded_file)
    uploaded_file_url = fs.url(uploaded_filename) # "/media/~~~.jpg"

    predict_result = predict_mnist_one(settings.MEDIA_ROOT_URL + uploaded_file_url)

    context = {'uploaded_file_url':uploaded_file_url,
               'uploaded_file_name':uploaded_filename,
               'predict_result' : predict_result}
    return render(request, 'mldl_main/dl_mnist_result.html', context)


def delete_mnist(request, file_name):

    fs = FileSystemStorage()
    fs.delete(file_name)

    return redirect('mldl_main:index')
