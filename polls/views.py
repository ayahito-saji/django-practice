from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from django.shortcuts import render, get_object_or_404

from django.views import generic

from .models import Question, Choice

class IndexView (generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.all()
"""
def index(request):
    context = {
        'questions': Question.objects.all(),
    }
#    template = loader.get_template('polls/index.html')
#    return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)
"""
class DetailView (generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

"""
def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        choices = question.choice_set.all()
    except:
        raise Http404("Questionは存在しません")
    context = {
        'question': question,
        'choices': choices,
    }
    template = loader.get_template('polls/detail.html')
    return HttpResponse(template.render(context, request))
"""
class ResultsView (generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

"""
def results(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        choices = question.choice_set.all()
    except:
        raise Http404("Questionは存在しません")
    context = {
        'question': question,
        'choices': choices,
    }
    template = loader.get_template('polls/results.html')
    return HttpResponse(template.render(context, request))
"""

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    print(request.POST)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print(selected_choice)
    except:
        context = {
            'question': question,
            'choices': choices,
            'error_message': "選択されていません"
        }
        template = loader.get_template('polls/detail.html')
        return HttpResponse(template.render(context, request))
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=[question_id]))
