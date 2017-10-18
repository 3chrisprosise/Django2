from django.shortcuts import render, HttpResponse, Http404, get_object_or_404,HttpResponseRedirect
from . import models
from django.template import loader
from django.urls import reverse

from django.views import generic
# Create your views here.

def detail(req, question_id):
    return HttpResponse("You are looking at question %s" % question_id)

def results(req, question_id):
    response = "You are looking at results of question %s"
    return HttpResponse(response % question_id)

def vote(req, questino_id):
    return HttpResponse("you are voting the quesion %s" % questino_id)

def index(req):
    latest_question_list = models.Question.objects.order_by('-pubdate')[:5]
    output = ','.join([q.question_text for q in latest_question_list])
    template = loader.get_template('index.html')
    context = {
         'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, req))

def index(request):
    latest_question_list = models.Question.objects.order_by('-pubdate')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)

def detail(req, question_id):
    try:
        question = models.Question.objects.get(pk=question_id)
    except models.Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(req,'detail.html',{"question": question})

def vote(req, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=req.POST["choice"])
    except(KeyError,models.Choice.DoesNotExist):
        return render(req, 'detail.html', {
            "question": question,
            "error_message":"didnot select a choice"
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('Basic:results',args=(question_id,)))
        # arges 的参数为一个元组，所以当只有一个元素的时候必须加逗号

''' 

    以上为复杂化的实现方法 ，下面介绍更为简单的方法
    view.generic
'''

class IndexView(generic.ListView):
    template_name = 'index.html'

    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return models.Question.objects.order_by('pubdate')[:5]

class DetailView(generic.DetailView):
    model = models.Question
    template_name = 'detail.html'

class ResultsView(generic.DetailView):
    model = models.Question
    template_name = 'result.html'

def homework(req):
    return render(req, 'HomeWork.html')