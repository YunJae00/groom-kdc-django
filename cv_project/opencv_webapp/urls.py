from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


# reversing 할 때 필요
app_name = 'opencv_webapp'

urlpatterns = [
    path('', views.first_view, name='first_view'),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
]

# media 라는 폴더를 만들텐데 그 폴더에 올라갈 애들에 대해 url 세팅을 추가로 해줌
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)