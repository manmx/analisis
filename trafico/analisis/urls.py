from django.conf.urls import url

from analisis import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^result.png$', views.plotResultsOriginal, name='result'),
	url(r'^result1.png$', views.plotResults, name='result1'),
	url(r'^analiza$', views.plotResults),
]
