from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from  pymongo import MongoClient 


#connection  to no-sql database
client = MongoClient('localhost',27017)
db = client.datahub


#views to save and add data
def save_data(request):
	db.dataset.save({"name":"ankit","code":"007"})
	return HttpResponseRedirect('/')
	

def view_data(request):
	data=db.dataset.find()
	template = loader.get_template('json_bridge/index.html')
    	context = RequestContext(request, {'data':data})
	return HttpResponse(template.render(context))

#jump to dashboard

def dashboard_view(request):
	template = loader.get_template('json_bridge/dashboard.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))
