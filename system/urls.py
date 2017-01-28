# -*- coding=utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin', RedirectView.as_view(url='/admin/')),
	url(r'^', include('form.urls', namespace="form")),
]