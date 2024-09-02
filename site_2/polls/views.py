from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Choice

# Create your views here.
def index(request):
    # Question.objects.all()
    latest_question_list =  Question.objects.order_by('-pub_date')[:5]

    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return Question.objects.get(id=question_id)


def vote(request, question_id):
    question = Question.objects.get(id=question_id)


def results(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = question.choice_set.all()
    return choices.order_by('choice_text')


