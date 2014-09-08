from django.conf.urls import url

from analisis import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^result.png$', views.plotResults, name='result'),
	url(r'^analiza$', views.plotResults),
]
