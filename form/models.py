#-*- coding=utf-8 -*-
from django.db import models

class Form(models.Model):
	name = models.CharField(max_length=255, verbose_name='Имя')
	phone = models.PositiveIntegerField(verbose_name='Телехвон')
	email = models.EmailField(max_length=255,verbose_name='Адрес почты')

	class Meta:
		verbose_name = 'Пользователи'
		verbose_name_plural = 'Пользователи'