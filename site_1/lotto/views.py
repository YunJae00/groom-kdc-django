from django.shortcuts import render
from django.http import HttpResponse
from lotto.models import GuessNumbers


# Create your views here.
def index(request): # user의 요청
    # params 1. request 2. user 에게 전달할 html 3. {} dict (결과를 html 에 전달해서 줘야하는 값들)
    return render(request, 'lotto/default.html', {})


def hello(requset):
    return HttpResponse("<h1 style='color:red;'>hello</h1>")


# # <input type='text' name='name'></input> user가 값을 입력하고 보내면 name으로 받아옴
# user_input_name = request.POST['name']
# user_input_text = request.POST['text']
#
# new_row = GuessNumbers(user_input_name, user_input_text)
#
# new_row.save()
#
# return HttpResponse('<h1>hello</h1>')