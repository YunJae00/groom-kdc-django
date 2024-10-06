from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .predict_ML import predict_iris_one
from .predict_DL import predict_mnist_one
from .crawl_newstitle import crawl_newstitle
import pandas as pd

# Create your views here.

def index(request):
    return render(request, 'mldl_main/index.html', {})



def crawl_simple(request):
    return render(request, 'mldl_main/crawl_simple.html', {})


def crawl_result(request):

    search_keyword = request.POST['search_keyword'] if request.POST['search_keyword'] != '' else '서울날씨'
    result_titles, result_urls = crawl_newstitle(search_keyword)

    result_df = pd.DataFrame({'News-titles': result_titles, 'News-URLs': result_urls})
    result_df_html = result_df.to_html(
                            columns=['News-titles', 'News-URLs'],
                            index=False, na_rep="", bold_rows=True,
                            classes=["table", "table-hover", "table-processed"])

    context = {'result_df_html': result_df_html, 'search_keyword':search_keyword}
    return render(request, 'mldl_main/crawl_result.html', context)



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
