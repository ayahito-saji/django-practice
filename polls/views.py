from django.http import HttpResponse, Http404
from django.template import loader

from django.shortcuts import render

from .models import Question

def index(request):
    context = {
        'questions': Question.objects.all(),
    }
#    template = loader.get_template('polls/index.html')
#    return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        choices = question.choice_set.all()
    except:
        raise Http404("Questionは存在しません")
    context = {
        'question': question,
        'choices': choices
    }
    template = loader.get_template('polls/detail.html')
    return HttpResponse(template.render(context, request))

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
