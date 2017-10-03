from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from .models import OrgList,EmpDetail
from django.shortcuts import render,get_object_or_404
from .forms import NewForm,EmpForm
from django.contrib import messages

def home(request):
	template = loader.get_template('myapp/home.html')
	cl = OrgList.objects.all()
	context = { 'cl':cl }
	return HttpResponse(template.render(context,request))

def org_create(request):
	form = NewForm(request.POST or None ,request.FILES or None )
	if form.is_valid():    
		instance= form.save(commit=False)
		instance.save()
		messages.success(request,"Successfully saved..")
		return HttpResponseRedirect(instance.get_absolute_url())

	context={
		'form': form,
	}
	return  render (request,"myapp/company_form1.html" , context)


def org_detail(request,id=None):
	#instance=OrgList.objects.get(id=id)
	instance = get_object_or_404(OrgList,id=id)
	context ={
			'instance' : instance,

	}
	return  render (request,"myapp/company_detail.html" , context)

def org_update(request,id=None):
	instance = get_object_or_404(OrgList,id=id)
	form = NewForm(request.POST or None,request.FILES or None ,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully updated..")
		return HttpResponseRedirect(instance.get_absolute_url())

	context ={
			  'instance' : instance,
			  'form':form ,
	}
	return  render (request,"myapp/company_form1.html" , context)

def org_delete(request,id=None):
	instance =get_object_or_404(OrgList,id=id)
	instance.delete()
	return render(request,"myapp/company_delete.html")


#empv views

def emp_detail(request,id=None):
	#instance=OrgList.objects.get(id=id)
	instance = get_object_or_404(EmpDetail,id=id)
	context ={
			  'instance' : instance,
	}
	return  render (request,"myapp/emp_detail.html" , context)


def emp_create(request):
	form = EmpForm(request.POST or None)
	if form.is_valid():
		instance= form.save(commit=False)
		instance.save()
		messages.success(request,"Successfully saved..")
		return HttpResponseRedirect(instance.get_absolute_url())

	context={
		'form': form,
	}
	return  render (request,"myapp/emp_form.html" , context)

def emp_update(request,id=None):
	instance = get_object_or_404(EmpDetail,id=id)
	form = EmpForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#print instance.orglist.get_absolute_url()
		messages.success(request, "Successfully updated..")
		return HttpResponseRedirect(instance.get_absolute_url())

	context ={
			  'instance' : instance,
			  'form':form ,
	}
	return  render (request,"myapp/emp_form.html" , context)

def emp_delete(request,id=None):
	instance = get_object_or_404(EmpDetail,id=id)
	instance.delete()
	return render(request,"myapp/emp_delete.html")









