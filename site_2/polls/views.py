from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice

# Create your views here.
def index(request):
    # Question.objects.all()
    latest_question_list =  Question.objects.order_by('-pub_date')[:5]

    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', context)


def detail(request, question_id):

    # try:
    #     q = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question {} does not exist".format(question_id))

    #q = Question.objects.get(id=question_id)

    q = get_object_or_404(Question, id=question_id)

    context = {'question': q}

    return render(request, 'polls/detail.html', context)


def vote(request, question_id):

    question = get_object_or_404(Question, id=question_id)

    # print(question_id)

    try:
        selected_choice = question.choice_set.get(id=request.POST['choice_select'])
    except:
        context = {'question': question, 'error_message': 'Please select a choice'}
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # url 에서 별명 name 으로 불러옴
        return redirect('polls:results', question_id=question.id)



def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/result.html', {'question': question})


