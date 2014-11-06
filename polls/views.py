from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.forms import mibrowform 
from polls.models import Question

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'latest-question_list': latest_question_list,
	})
	return HttpResponse(template.render(context))

def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response = "You are looking at the result of question %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("you are voting on question %s." % question_id)

#def result_mibrow(request)
#	form = mibrowform()
#	context = {"form": form}
#	return render(request, template, context)
