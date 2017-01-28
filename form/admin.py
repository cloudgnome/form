# -*- coding: utf-8 -*-
from django.contrib import admin
from .forms import Form
from .models import Form as FormModel

class FormAdmin(admin.ModelAdmin):
	form = Form

	list_display = ('phone','name','email',)
	list_filter = ('name',) 
	fieldsets = (
		(None, {'fields': ('name','phone','email')}),
	)
	search_fields = ('email','name','phone')
	ordering = ('name',)

admin.site.register(FormModel, FormAdmin)