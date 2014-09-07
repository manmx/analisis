import matplotlib.pyplot as plt

def generaHistograma(filename, dictionary):
	xmax = max(dictionary.keys())
	ymax = max(dictionary.values())
	plt.figure()
	plt.hist(dictionary, xmax)
	plt.title('Histogram Title')
	plt.xlabel('xLabel')
	plt.ylabel('yLabel')
	plt.axis([0, xmax, 0, ymax])
	plt.savefig(filename)

