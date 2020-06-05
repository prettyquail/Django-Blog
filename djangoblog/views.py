from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import BlogApp
from .forms import BlogForm
from django.contrib import messages

# Create your views here.
def create(request):
	context={}
	form =BlogForm(request.POST or None) 
	if form.is_valid():
		form.save()
		messages.success(request, 'Blog Successfully Created')
		return redirect('create')

	context['form']=form
	return render(request, "create.html", context) 

def update(request,id):
	context={}
	obj=get_object_or_404(BlogApp,id=id)
	form=BlogForm(request.POST,instance=obj)
	if form.is_valid():
		form.save()
		messages.success(request, 'Updated Successfully')
		return HttpResponseRedirect('/'+id)
	context['form']=form
	return render(request,'update.html',context)

def index(request):
	context={}
	form=BlogApp.objects.all()
	context['form']=form
	return render(request,'index.html',context)

def detail(request,id):
	context={}
	form=BlogApp.objects.get(id=id)
	context['form']=form
	return render(request,'detail.html',context)

def delete(request,id):
	context={}
	obj=BlogApp.objects.get(id=id)
	if request.method=='POST':
		obj.delete()
		return HttpResponseRedirect('/')

	return render(request,'index.html',context)