# -*- coding: utf-8 -*-
from django import forms
from .models import Form

class Form(forms.ModelForm):
	name = forms.CharField(label='ИМЯ*',widget=forms.TextInput(attrs={'placeholder': 'ИМЯ*'}),required=True)
	email = forms.EmailField(label="Email-адрес",widget=forms.TextInput(attrs={'placeholder': 'Email адрес'}),required=True)
	phone = forms.CharField(label='Номер телефона*:',widget=forms.TextInput(attrs={'placeholder': '(Формат: 099 999 99 99)','title':'0976664455','pattern':'0[0-9]{2}[0-9]{3}[0-9]{2}[0-9]{2}'}),required=True)

	class Meta:
		model = Form
		fields = ('name','email','phone')