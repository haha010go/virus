# -*- coding: utf-8 -*-
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    # print(request)
    # latest_question_list= Question.objects.order_by('-pub_date')[:5]
    # output=','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    return HttpResponse("helloworld")

def detail(request,question_id):
    return HttpResponse("You are looking at question %s." % question_id)
def results(request,question_id):
    response= "You are looking at the results of question %s"
    return HttpResponse(response % question_id)
def vote(request,question_id):
    return HttpResponse("You're votin on question %s"% question_id)