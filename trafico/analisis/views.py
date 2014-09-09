from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import procesaCSV
import graficas
import matplotlib
import StringIO
import urllib, base64


nACC = 0
nACV = 0
nAV = 0
nCALZ = 0
nCC = 0
nCDA = 0
nCENTRO = 0
nCicloton = 0
nENCH = 0
nEventoC = 0
nEventoD = 0
nFUEGO = 0
nFUGA = 0
nGLORIETA = 0
nII = 0
nINC = 0
nINCPRO = 0
nIOTROSA = 0
nIOTROSM = 0
nOBR = 0
nPP = 0
nRC = 0
nREVERSIBLE = 0
nSD = 0
nTL = 0
Dic = {}
sortedLista = []
checkboxValues = ['ACC','ACV','AV', 'CALZ', 'CC', 'CDA', 'CENTRO', 'Cicloton', 'ENCH', 'EventoC', 'EventoD', 'FUEGO', 'FUGA', 'GLORIETA', 'II', 'INC', 'INCPRO', 'IOTROSA', 'IOTROSM', 'OBR', 'PP', 'RC', 'REVERSIBLE', 'SD', 'TL']
def index(request):
	
	#lista = procesaCSV.retrieve()
	#sortedLista = sorted(lista, key=lambda registro: registro.motivo)
	
	#template = loader.get_template('analisis/index.html')
	context = {
	#	'lista' : sortedLista,
		'choices' : checkboxValues,
	}
	
	html = render(request, 'analisis/index.html', context)
	return html
@csrf_exempt
def filtrar(request):
	#context_instance=RequestContext(request);
	lista = procesaCSV.retrieve()
	sortedLista = sorted(lista, key=lambda registro: registro.motivo)
	
	#template = loader.get_template('analisis/page2.html')
	context = {
		'lista' : sortedLista,
		'choices' : checkboxValues,
	}
	
	html = render(request, 'analisis/index.html', context)
	return html
def plotResults(request):
	var = request.POST.getlist('checks', 'ALL')
	print var
	size = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5]
	lista = procesaCSV.retrieve(var)
	sortedLista = sorted(lista, key=lambda registro: registro.motivo_r)
	nACC = sum(r.motivo_r.find("ACC") != -1 for r in sortedLista)
	Dic['ACC'] = nACC
	nACV = sum(r.motivo_r.find("ACV") != -1 for r in sortedLista)
	Dic['ACV'] = nACV	
	nAV = sum(r.motivo_r.find("AV") != -1 for r in sortedLista)
	Dic['AV'] = nAV	
	nCALZ = sum(r.motivo_r.find("CALZ") != -1 for r in sortedLista)
	Dic['CALZ'] = nCALZ		
	nCC = sum(r.motivo_r.find("CC") != -1 for r in sortedLista)
	Dic['CC'] = nCC		
	nCDA = sum(r.motivo_r.find("CDA") != -1 for r in sortedLista)
	Dic['CDA'] = nCDA	
	nCENTRO = sum(r.motivo_r.find("CENTRO") != -1 for r in sortedLista)
	Dic['CENTRO'] = nCENTRO	
	nCicloton = sum(r.motivo_r.find("Cicloton") != -1 for r in sortedLista)
	Dic['Cicloton'] = nCicloton	
	nENCH = sum(r.motivo_r.find("ENCH") != -1 for r in sortedLista)
	Dic['ENCH'] = nENCH	
	nEventoC = sum(r.motivo_r.find("EventoC") != -1 for r in sortedLista)
	Dic['EventoC'] = nEventoC	
	nEventoD = sum(r.motivo_r.find("EventoD") != -1 for r in sortedLista)
	Dic['EventoD'] = nEventoD	
	nFUEGO = sum(r.motivo_r.find("FUEGO") != -1 for r in sortedLista)
	Dic['FUEGO'] = nFUEGO	
	nFUGA = sum(r.motivo_r.find("FUGA") != -1 for r in sortedLista)
	Dic['FUGA'] = nFUGA	
	nGLORIETA = sum(r.motivo_r.find("GLORIETA") != -1 for r in sortedLista)
	Dic['GLORIETA'] = nGLORIETA	
	nII = sum(r.motivo_r.find("II -") != -1 for r in sortedLista)
	Dic['II'] = nII	
	nINC = sum(r.motivo_r.find("INC") != -1 for r in sortedLista)
	Dic['INC'] = nINC	
	nINCPRO = sum(r.motivo_r.find("INCPRO") != -1 for r in sortedLista)
	Dic['INCPRO'] = nINCPRO	
	nIOTROSA = sum(r.motivo_r.find("IOTROSA") != -1 for r in sortedLista)
	Dic['IOTROSA'] = nIOTROSA	
	nIOTROSM = sum(r.motivo_r.find("IOTROSM") != -1 for r in sortedLista)
	Dic['IOTROSM'] = nIOTROSM	
	nOBR = sum(r.motivo_r.find("OBR") != -1 for r in sortedLista)
	Dic['OBR'] = nOBR	
	nPP = sum(r.motivo_r.find("PP") != -1 for r in sortedLista)
	Dic['PP'] = nPP	
	nRC = sum(r.motivo_r.find("RC") != -1 for r in sortedLista)
	Dic['RC'] = nRC	
	nREVERSIBLE = sum(r.motivo_r.find("REVERSIBLE") != -1 for r in sortedLista)
	Dic['REVERSIBLE'] = nREVERSIBLE	
	nSD = sum(r.motivo_r.find("SD") != -1 for r in sortedLista)
	Dic['SD'] = nSD	
	nTL = sum(r.motivo_r.find("TL") != -1 for r in sortedLista)
	Dic['TL'] = nTL		

	import random
	import django
	import datetime
	import pylab as pl
	import numpy as np
	import matplotlib.pyplot as plt

	from matplotlib.backends.backend_agg import FigureCanvasAgg as  FigureCanvas
	from matplotlib.figure import Figure
	fig = Figure()
	ax = fig.add_subplot(111)
	d = Dic
	rects = ax.bar(range(len(d)),d.values(),align='edge')
	#ax.xticks(range(len(d)), d, rotation+90)
	ax.set_xticks(size)	
	ax.set_xticklabels(d.keys(), rotation=90)
	#ax.legend(['A simple line', 'B simple '])
	for rect in rects:
		height = rect.get_height()
		ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height), ha='center', va='bottom')
	#X = np.arange(len(d))
	#ax.bar(d.keys(), d.values(), align='center')
	#ax.xticks(X, d.keys())
	#ymax = max(d.values()) + 1
	#ax.ylim(0, ymax)
	#ax.bar(N.keys(), N.values(), align='center')
	## the data
	#N = 5
	#menMeans = [18, 35, 30, 35, 27]
	#menStd =   [2, 3, 4, 1, 2]
	#womenMeans = [25, 32, 34, 20, 25]
	#womenStd =   [3, 5, 2, 3, 3]

	## necessary variables
	#ind = np.arange(N)                # the x locations for the 		groups
	#width = 0.35                      # the width of the bars

	## the bars
	#rects1 = ax.bar(ind, menMeans, width,
	#		color='black',
	#		yerr=menStd,
	#		error_kw=dict(elinewidth=2,ecolor='red'))

	#rects2 = ax.bar(ind+width, womenMeans, width,
	#		    color='red',
	#		    yerr=womenStd,
	#		    error_kw=dict(elinewidth=2,ecolor='black'))

	# axes and labels
	#ax.set_xlim(-width,len(ind)+width)
	#ax.set_ylim(0,45)
	#ax.set_ylabel('Scores')
	#ax.set_title('Scores by group and gender')
	#xTickMarks = ['Group'+str(i) for i in range(1,6)]
	#ax.set_xticks(ind+width)
	#xtickNames = ax.set_xticklabels(xTickMarks)
	#plt.setp(xtickNames, rotation=45, fontsize=10)

	## add a legend
	#ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )
	canvas=FigureCanvas(fig)
	
	imgData = StringIO.StringIO()
	fig.savefig(imgData, format='png')
	imgData.seek(0)
	uri = 'data:image/png;base64,' + urllib.quote(base64.b64encode(imgData.buf))
	return HttpResponse(uri)


	#response=django.http.HttpResponse(content_type='image/png')
	#canvas.print_png(response)
	#return response
	#return HttpResponse("Usted esta en el index de analisis")

def plotResultsOriginal(request):
	var = request.POST.getlist('checks', 'ALL')
	print var
	size = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5]
	lista = procesaCSV.retrieve(var)
	sortedLista = sorted(lista, key=lambda registro: registro.motivo_r)
	nACC = sum(r.motivo_r.find("ACC") != -1 for r in sortedLista)
	Dic['ACC'] = nACC
	nACV = sum(r.motivo_r.find("ACV") != -1 for r in sortedLista)
	Dic['ACV'] = nACV	
	nAV = sum(r.motivo_r.find("AV") != -1 for r in sortedLista)
	Dic['AV'] = nAV	
	nCALZ = sum(r.motivo_r.find("CALZ") != -1 for r in sortedLista)
	Dic['CALZ'] = nCALZ		
	nCC = sum(r.motivo_r.find("CC") != -1 for r in sortedLista)
	Dic['CC'] = nCC		
	nCDA = sum(r.motivo_r.find("CDA") != -1 for r in sortedLista)
	Dic['CDA'] = nCDA	
	nCENTRO = sum(r.motivo_r.find("CENTRO") != -1 for r in sortedLista)
	Dic['CENTRO'] = nCENTRO	
	nCicloton = sum(r.motivo_r.find("Cicloton") != -1 for r in sortedLista)
	Dic['Cicloton'] = nCicloton	
	nENCH = sum(r.motivo_r.find("ENCH") != -1 for r in sortedLista)
	Dic['ENCH'] = nENCH	
	nEventoC = sum(r.motivo_r.find("EventoC") != -1 for r in sortedLista)
	Dic['EventoC'] = nEventoC	
	nEventoD = sum(r.motivo_r.find("EventoD") != -1 for r in sortedLista)
	Dic['EventoD'] = nEventoD	
	nFUEGO = sum(r.motivo_r.find("FUEGO") != -1 for r in sortedLista)
	Dic['FUEGO'] = nFUEGO	
	nFUGA = sum(r.motivo_r.find("FUGA") != -1 for r in sortedLista)
	Dic['FUGA'] = nFUGA	
	nGLORIETA = sum(r.motivo_r.find("GLORIETA") != -1 for r in sortedLista)
	Dic['GLORIETA'] = nGLORIETA	
	nII = sum(r.motivo_r.find("II -") != -1 for r in sortedLista)
	Dic['II'] = nII	
	nINC = sum(r.motivo_r.find("INC") != -1 for r in sortedLista)
	Dic['INC'] = nINC	
	nINCPRO = sum(r.motivo_r.find("INCPRO") != -1 for r in sortedLista)
	Dic['INCPRO'] = nINCPRO	
	nIOTROSA = sum(r.motivo_r.find("IOTROSA") != -1 for r in sortedLista)
	Dic['IOTROSA'] = nIOTROSA	
	nIOTROSM = sum(r.motivo_r.find("IOTROSM") != -1 for r in sortedLista)
	Dic['IOTROSM'] = nIOTROSM	
	nOBR = sum(r.motivo_r.find("OBR") != -1 for r in sortedLista)
	Dic['OBR'] = nOBR	
	nPP = sum(r.motivo_r.find("PP") != -1 for r in sortedLista)
	Dic['PP'] = nPP	
	nRC = sum(r.motivo_r.find("RC") != -1 for r in sortedLista)
	Dic['RC'] = nRC	
	nREVERSIBLE = sum(r.motivo_r.find("REVERSIBLE") != -1 for r in sortedLista)
	Dic['REVERSIBLE'] = nREVERSIBLE	
	nSD = sum(r.motivo_r.find("SD") != -1 for r in sortedLista)
	Dic['SD'] = nSD	
	nTL = sum(r.motivo_r.find("TL") != -1 for r in sortedLista)
	Dic['TL'] = nTL		

	import random
	import django
	import datetime
	import pylab as pl
	import numpy as np
	import matplotlib.pyplot as plt

	from matplotlib.backends.backend_agg import FigureCanvasAgg as  FigureCanvas
	from matplotlib.figure import Figure
	fig = Figure()
	ax = fig.add_subplot(111)
	d = Dic
	rects = ax.bar(range(len(d)),d.values(),align='edge')
	#ax.xticks(range(len(d)), d, rotation+90)
	ax.set_xticks(size)	
	ax.set_xticklabels(d.keys(), rotation=90)
	#ax.legend(['A simple line', 'B simple '])
	for rect in rects:
		height = rect.get_height()
		ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height), ha='center', va='bottom')
	#X = np.arange(len(d))
	#ax.bar(d.keys(), d.values(), align='center')
	#ax.xticks(X, d.keys())
	#ymax = max(d.values()) + 1
	#ax.ylim(0, ymax)
	#ax.bar(N.keys(), N.values(), align='center')
	## the data
	#N = 5
	#menMeans = [18, 35, 30, 35, 27]
	#menStd =   [2, 3, 4, 1, 2]
	#womenMeans = [25, 32, 34, 20, 25]
	#womenStd =   [3, 5, 2, 3, 3]

	## necessary variables
	#ind = np.arange(N)                # the x locations for the 		groups
	#width = 0.35                      # the width of the bars

	## the bars
	#rects1 = ax.bar(ind, menMeans, width,
	#		color='black',
	#		yerr=menStd,
	#		error_kw=dict(elinewidth=2,ecolor='red'))

	#rects2 = ax.bar(ind+width, womenMeans, width,
	#		    color='red',
	#		    yerr=womenStd,
	#		    error_kw=dict(elinewidth=2,ecolor='black'))

	# axes and labels
	#ax.set_xlim(-width,len(ind)+width)
	#ax.set_ylim(0,45)
	#ax.set_ylabel('Scores')
	#ax.set_title('Scores by group and gender')
	#xTickMarks = ['Group'+str(i) for i in range(1,6)]
	#ax.set_xticks(ind+width)
	#xtickNames = ax.set_xticklabels(xTickMarks)
	#plt.setp(xtickNames, rotation=45, fontsize=10)

	## add a legend
	#ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )
	canvas=FigureCanvas(fig)
	
	#imgData = StringIO.StringIO()
	#fig.savefig(imgData, format='png')
	#imgData.seek(0)
	#uri = 'data:image/png;base64,' + urllib.quote(base64.b64encode(imgData.buf))
	#return HttpResponse(uri)


	response=django.http.HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response
	return HttpResponse("Usted esta en el index de analisis")

# Create your views here.
