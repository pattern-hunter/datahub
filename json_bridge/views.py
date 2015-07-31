from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate,login,logout
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
	if request.user.is_authenticated():
		template = loader.get_template('json_bridge/dashboard.html')
		context = RequestContext(request, {'user':request.session['username']})
		return HttpResponse(template.render(context))
	else:
		return HttpResponseRedirect('/')


#authentication

def auth_view(request):
	username = request.POST['username']
        password = request.POST['password']
	user=authenticate(username=username,password=password)
	if user is not None:
		login(request,user)
		request.session['username']=username
		return HttpResponseRedirect('/dashboard/') 
	else:
		return HttpResponseRedirect('/')

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
