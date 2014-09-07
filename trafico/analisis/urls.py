from django.conf.urls import url

from analisis import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]
