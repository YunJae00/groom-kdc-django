from django.shortcuts import render

from .forms import SimpleUploadForm, ImageUploadForm

# 파일 저장하기 위한 도구 db 있을 땐 이거 안씀
from django.core.files.storage import FileSystemStorage


# Create your views here.
def first_view(request):
    return render(request, 'opencv_webapp/first_view.html', {})


def simple_upload(request):

    if request.method == 'POST':
        # print(request.POST) : <QueryDict: {'csrfmiddlewaretoken': [‘~~~’], 'title': ['upload_1']}>
        # print(request.FILES) : <MultiValueDict: {'image': [<InMemoryUploadedFile: ses.jpg (image/jpeg)>]}>
        # 메모리 상에 잠깐 올라가 있는 이미지 파일을 사용해야함
        # 비어있는 Form에 사용자가 업로드한 데이터를 넣고 검증합니다.

        #request.POST 'title'
        #request.FILES 'image'
        form = SimpleUploadForm(request.POST, request.FILES)

        if form.is_valid():
            myfile = request.FILES['image']

            fs = FileSystemStorage()
            # params 경로명을 포함할 파일 저장 시 활용할 이름, 파일 객체 자체
            filename = fs.save(myfile.name, myfile) # 저장이 끝난 물리적인 파일 이름

            # myfile.name : 'ses.jpg' (사용자가 업로드한 파일 원본의 이름)
            # filename : 'ses_UPArih4.jpg' (서버에 업로드가 끝난 파일의 이름, 중복될 시 자동으로 변경됨)
            # 이거의 type 을 찍어보면 두개는 다른거임 string 이랑 파일 자체로 다른거임

            uploaded_file_url =  fs.url(filename) # 저장이 끝난 물리적인 파일로 접근 가능한 URL

            context = {'form':form, 'uploaded_file_url': uploaded_file_url}

            return render(request, 'opencv_webapp/simple_upload.html', context)

    else:
        form = SimpleUploadForm()
        context = {'form': form}
        return render(request, 'opencv_webapp/simple_upload.html', context)


def detect_face(request):

    form = ImageUploadForm()
    return render(request,'opencv_webapp/detect_face.html', {'form': form} )
