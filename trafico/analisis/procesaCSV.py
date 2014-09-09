import csv

class Registro(object):
	def __init__(self, ticket, fecha, motivo_r, motivo, latitud, longitud):
		self.ticket = ticket
		self.fecha = fecha
		self.motivo_r = motivo_r
		self.motivo = motivo
		self.latitud = latitud
		self.longitud = longitud
def retrieve(var):
	lista = []
	if var == 'ALL':
		with open('/vol/data/reporte_vial') as csvfile:
			spamreader = csv.reader(csvfile)
			next(spamreader)
			for row in spamreader:
				mot = row[2].split('-')
				idRes = mot[0].strip()
				Res = mot[1]
				temp = Registro(row[0], row[1], idRes, Res, row[3], row[4])
				lista.append(temp)
		return lista
	else:		
		with open('/vol/data/reporte_vial') as csvfile:
			spamreader = csv.reader(csvfile)
			next(spamreader)
			for row in spamreader:
				mot = row[2].split('-')
				idRes = mot[0].strip()
				Res = mot[1]
				if idRes in var:
					temp = Registro(row[0], row[1], idRes, Res, row[3], row[4])
					lista.append(temp)
		return lista
#print (row[0])
