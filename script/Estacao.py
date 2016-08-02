#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Estacao:

	estates = {
	"AC":{"name":"Acre", "region":"Norte"},
	"AL":{"name":"Alagoas", "region":"Nosdeste"},
	"AP":{"name":"Amapa", "region":"Norte"},
	"AM":{"name":"Amazonas", "region":"Norte"},
	"BA":{"name":"Bahia", "region":"Nordeste"},
	"CE":{"name":"Ceara", "region":"Nordeste"},
	"DF":{"name":"Distrito_Federal", "region":"Centro-Oeste"},
	"ES":{"name":"Esperito_Santo", "region":"Sudeste"},
	"GO":{"name":"Goias", "region":"Centro-Oeste"},
	"MA":{"name":"Maranhao", "region":"Nordeste"},
	"MT":{"name":"Mato_Grosso", "region":"Centro-Oeste"},
	"MS":{"name":"Mato_Grosso_do_Sul", "region":"Centro-Oeste"},
	"MG":{"name":"Minas_Gerais", "region":"Sudeste"},
	"PA":{"name":"Para", "region":"Norte"},
	"PB":{"name":"Paraiba", "region":"Nordeste"},
	"PR":{"name":"Parana", "region":"Sul"},
	"PE":{"name":"Pernambuco", "region":"Nordeste"},
	"PI":{"name":"Piaui", "region":"Nordeste"},
	"RJ":{"name":"Rio_de_Janeiro", "region":"Sudeste"},
	"RN":{"name":"Rio_Grande_do_Norte", "region":"Nordeste"},
	"RS":{"name":"Rio_Grande_do_Sul", "region":"Sul"},
	"RO":{"name":"Rondonia", "region":"Norte"},
	"RR":{"name":"Roraima", "region":"Norte"},
	"SC":{"name":"Santa_Catarina", "region":"Sul"},
	"SP":{"name":"Sao_Paulo", "region":"Sudeste"},
	"SE":{"name":"Sergipe", "region":"Nordeste"},
	"TO":{"name":"Tocantins", "region":"Norte"},
	}

	head = "codigo_omm,station_name,state,state_initials,region,latitude,longitude,altitude,altitude_type,start_operation_date,station_situation,data_situation"
	
	def __init__(self, name_complete, lat, lng, alt, situation, op_date):

		splited = name_complete.split("-")
		self.name = splited[0].strip()

		splited = splited[1].split("(")
		self.setState(splited[0].strip())

		self.codigo_omm = splited[1].replace("OMM: ", "").replace(")", "")

		self.lat = lat
		self.lng = lng
		self.alt = alt
		self.situation = situation
		self.setStartOpDate(op_date)

	def getStateName(self, initial):
		return self.estates[initial]["name"]

	def getStateRegion(self, initial):
		return self.estates[initial]["region"]

	def setState(self, state_initials):
		self.state_initials = state_initials
		self.state_name = self.getStateName(self.state_initials)
		self.state_region = self.getStateRegion(self.state_initials)

	def setStartOpDate(self,date):
		date = date.split("/")
		date.reverse()
		date = "-".join(date)
		self.op_start_date = date

	def toCsvRow(self):
		row = ",".join([self.codigo_omm, self.name, self.state_name, self.state_initials, self.state_region, self.lat, self.lng, self.alt, "meters",self.op_start_date,"operante","operante"])
		return row

	@staticmethod
	def exportFileCSV(file_name, dados):
		
		try:
			f = open(file_name, "w")
			f.write(self.getHead()+"\n")

			for i in range(len(dados)):
				f.write(dados[i].toCsvRow()+"\n")

			f.close()
		except IOError:
			cookie = {}
			print "** ERROR: Erro ao abrir o arquivo %s **" % (file_name)
			return False

		return True

	def __str__(self):
		s = "Estação: "+self.name+"\n" \
		"Latitude: "+self.lat+"\n" \
		"Longitude: "+self.lng+"\n" \
		"Altitude: "+self.alt+"\n" \
		"Situação: "+self.situation+"\n" \
		"Latitude: "+self.lat+"\n" \
		"Em operação desde "+self.op_start_date
		return s