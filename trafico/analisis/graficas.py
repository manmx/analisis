import matplotlib.pyplot as plt

def generaHistograma():
	fig = Figure()
	N = {1 : 10, 2 : 20, 3 : 40}
	plt.bar(N.keys(), N.values(), align='center')
	
	canvas = FigureCanvas(fig)
	return canvas

