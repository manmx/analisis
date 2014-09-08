from django.shortcuts import render
from django.http import HttpResponse
import procesaCSV
import graficas
import matplotlib

def index(request):
	lista = procesaCSV.retrieve()
	#template = loader.get_template('analisis/index.html')
	context = {
		'lista' : lista,
	}
	
	html = render(request, 'analisis/index.html', context)
	return html
def plotResults(request):
	import random
	import django
	import datetime
	import numpy as np
	import matplotlib.pyplot as plt

	from matplotlib.backends.backend_agg import FigureCanvasAgg as  FigureCanvas
	from matplotlib.figure import Figure
	fig = Figure()
	ax = fig.add_subplot(111)

	## the data
	N = 5
	menMeans = [18, 35, 30, 35, 27]
	menStd =   [2, 3, 4, 1, 2]
	womenMeans = [25, 32, 34, 20, 25]
	womenStd =   [3, 5, 2, 3, 3]

	## necessary variables
	ind = np.arange(N)                # the x locations for the 		groups
	width = 0.35                      # the width of the bars

	## the bars
	rects1 = ax.bar(ind, menMeans, width,
			color='black',
			yerr=menStd,
			error_kw=dict(elinewidth=2,ecolor='red'))

	rects2 = ax.bar(ind+width, womenMeans, width,
			    color='red',
			    yerr=womenStd,
			    error_kw=dict(elinewidth=2,ecolor='black'))

	# axes and labels
	ax.set_xlim(-width,len(ind)+width)
	ax.set_ylim(0,45)
	ax.set_ylabel('Scores')
	ax.set_title('Scores by group and gender')
	xTickMarks = ['Group'+str(i) for i in range(1,6)]
	ax.set_xticks(ind+width)
	xtickNames = ax.set_xticklabels(xTickMarks)
	#plt.setp(xtickNames, rotation=45, fontsize=10)

	## add a legend
	ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )
	canvas=FigureCanvas(fig)
	response=django.http.HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response
	#return HttpResponse("Usted esta en el index de analisis")

# Create your views here.
