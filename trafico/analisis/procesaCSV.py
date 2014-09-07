import csv

class Registro(object):
	def __init__(self, ticket, fecha, motivo, latitud, longitud):
		self.ticket = ticket
		self.fecha = fecha
		self.motivo = motivo
		self.latitud = latitud
		self.longitud = longitud
def retrieve():
	lista = []
	with open('/vol/data/reporte_vial') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			temp = Registro(row[0], row[1], row[2], row[3], row[4])
			lista.append(temp)
	return lista		
#print (row[0])
