from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.template import RequestContext, loader, Context
import datetime
#This is where I am includeing the databases....
from polls.models import TarbaseV5, HumanPredictionMiranda


# Create your views here.
def index(request):
	template = loader.get_template('home.html')
	context = RequestContext(request, {
		'test',
	})
	return HttpResponse(template.render(context))

def result(request):
#	if(request.method == "POST":
#		return "this is a test"
#	else
        #miranda = HumanPredictionMiranda.objects.all().filter(Id = '1')
        database_to_use = request.POST.get("database", "")
        post_variable = request.POST.get("fname", "")	
        if(database_to_use == "worms"):
		    result_list = TarbaseV5.objects.all().filter(id_v4 = post_variable)
#            result_list = Human_Prediction_Miranda.all().filter(mirbase_acc = 'MIMAT0000062')
        if(database_to_use == "human1"):
            result_list = TarbaseV5.objects.all().filter(id_v4 = post_variable)
        if(database_to_use == "humane2"):
            result_list = TarbaseV5.objects.all().filter(id_v4 = post_variable)	
	#   else:
#	            return database_to_use 
        template = loader.get_template('resutls.html')
        fname = request.POST.get("fname", "")#"this is suposed to equal the search value..."
		#result_list = TarbaseV5.objects.order_by('id_v4')[:5]
        output = ', '.join([p.chr_loc for p in result_list])


        c = Context({'result_lists' : result_list , 'something':database_to_use})	
        now = datetime.datetime.now()
        return HttpResponse(template.render(c)) 
#HttpResponse(template.render())

def return_result(request, question_id):
    result_list = TarbaseV5.objects.order_by('id_v4')[:5]
    output = ', '.join([p.question_text for p in result_list])
    return HttpResponse(output)
    

