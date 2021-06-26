from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Question

def index(request):
     # return HttpResponse("HelloWorld.You are at the polls index.")
    last_question_list =Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in last_question_list])
    # return HttpResponse(output)
    context = {
        'last_question_list' :last_question_list
    }
    return render(request, 'polls/index.html', context)
# Create your views here.

def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question':question})
#def results(request,question_id):
#    return (request,'result.html')