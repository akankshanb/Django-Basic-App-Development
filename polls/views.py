from django.shortcuts import render, get_object_or_404
from .models import Question
from django.template import loader
from django.http import Http404

# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = { 'latest_question_list' : latest_question_list}
	return render(request,'polls/index.html',context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/details.html', {'question': question})

def results(request,question_id):
	response = "Results %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s" % question_id)