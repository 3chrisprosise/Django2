from django.shortcuts import render, HttpResponse, Http404, get_object_or_404,HttpResponseRedirect
from . import models
from django.template import loader
from django.urls import reverse

from django.views import generic

from django.views.generic import ListView
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
    return render(req, 'homework2.html')



def md5_test(req):
    return render(req, 'TestMd5.html')

def aggregate(req):
    from django.db.models import Avg
    from django.db.models import Max, Min
    from django.db.models import Count
    from django.db.models import Sum
    from django.db.models import Q, F
    from django.db.models import FloatField
    # 第一种方法是从整个查询集生成统计值
    models.Book.objects.all().aggregate(Avg('price'))  # 这里的 all() 可以省略
    models.Book.objects.aggregate(Max('price'))  # 省略后
    models.Book.objects.all().aggregate(price_per_page=Sum(F('price') / F('pages'), output_field=FloatField()))
    models.Store.objects.annotate(min_price=Min('books__price'), max_price=Max('books__price'))
    # annotate 为表连接  aggregate 为嵌套查询
    # 使用纯sql语句查询
    persons = models.Person.objects.raw('SELECT * FROM myapp_person')
    # 传递给row的sql语句并不会被检查
    lname = 'Doe'
    models.Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])
    # 这里的参数传递要改成字符串获取参数的形式


# 游标的定义
def my_cursor(self):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
    cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    row = cursor.fetchone()

    # 查询中包含百分号字符 % ，你需要写成两个百分号字符

    # 关于Django 数据库 事物保存点的问题 ，依旧有待商议

    # 使用 QuerySet.exists() 来判断是否存在， 直接使用外键值 entry.blog_id

    '''
    
    一次性创建多个
    Entry.objects.bulk_create([
    Entry(headline="Python 3.0 Released"),
    Entry(headline="Python 3.1 Planned")
    ])
    
    '''

class PublisherList(ListView):  # listView  仅用于展示 model

    models = models.Publisher
