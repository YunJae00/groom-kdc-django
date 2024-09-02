from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
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
    question = Question.objects.get(id=question_id)


def results(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = question.choice_set.all()
    return choices.order_by('choice_text')


