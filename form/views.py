#-*- coding: utf-8 -*-
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.views.generic import View
from form.forms import Form

class IndexView(View):
	def get(self,request,*args,**kwargs):
		if request.user.is_anonymous():
			user = authenticate(username='admin',password='1234qwer')
			login(request,user)
		return render(request, 'index.html',{'form':Form()})

	def post(self,request,*args,**kwargs):
		form = Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/admin/form/form/')
		else:
			return render(request, 'index.html',{'form':form})