from django.shortcuts import render
from django.http import HttpResponse
import procesaCSV

def index(request):
	lista = procesaCSV.retrieve()
	#template = loader.get_template('analisis/index.html')
	context = {
		'lista' : lista,
	}
	html = render(request, 'analisis/index.html')
	return html
	#return HttpResponse("Usted esta en el index de analisis")

# Create your views here.
