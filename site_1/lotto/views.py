from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import PostForm
from .models import GuessNumbers

# Create your views here.
def index(request): # user의 요청
    # params 1. request 2. user 에게 전달할 html 3. {} dict (결과를 html 에 전달해서 줘야하는 값들)
    # return render(request, 'lotto/default.html', {})

    # request.POST -> dict
    # - dict의 key == input tag의 name 값
    # - dict의 value == input tag의 value 값 ( == user 의 입력 값)
    # request.POST['fname']

    lottos = GuessNumbers.objects.all()

    return render(request, 'lotto/default.html', {'lottos': lottos})


def post(request):

    if request.method == 'POST':
        print(request.POST)

        # <QueryDict: {'csrfmiddlewaretoken': ['jl3ipPpavilWJFRp7R0WGv1MLrVQ5LoN3ANZ49BG42v6FZ57J3EowHBn6miXwyuT'], 'name': ['test'], 'text': ['test text']}>
        # 이런식으로 dict 로 옴
        print(request.POST['name']) # 이런식으로 하면 key 값으로 불러올 수 있음

        form = PostForm(request.POST) # 이러면 알아서 채워진 양식이
        print(form)
        #<div>
        #    <label for="id_name">Name:</label>
        #    <input type="text" name="name" value="test" maxlength="24" required id="id_name">
        #</div>
        #<div>
        #    <label for="id_text">Text:</label>
        #    <input type="text" name="text" value="test text" maxlength="200" required id="id_text">
        #</div>
        # print form 이런식으로 뜸

        if form.is_valid():

            lotto = form.save(commit=False) # 이러면 행 하나를 의미함 commit false는 중간 단계라 pk가 안찍힐거

            lotto.generate()
            # form.save() # 이거 하면 끝 저장 다 해줌 근데 여기서 generate 에 save가 이미 있어서 안해줌

            return redirect('index') # url의 별명 name을 적어주면 됨

    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form': form})



def hello(requset):
    return HttpResponse("<h1 style='color:red;'>hello</h1>")


def detail(request, lottokey):

    lotto = GuessNumbers.objects.get(id=lottokey)

    return render(request, 'lotto/detail.html', {'lotto': lotto})

# # <input type='text' name='name'></input> user가 값을 입력하고 보내면 name으로 받아옴
# user_input_name = request.POST['name']
# user_input_text = request.POST['text']
#
# new_row = GuessNumbers(user_input_name, user_input_text)
#
# new_row.save()
#
# return HttpResponse('<h1>hello</h1>')