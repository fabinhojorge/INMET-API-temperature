#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import ast

class Estacao:
	
	def __init__(self, name, lat, lng, alt, situation, op_date):
		self.name = name
		self.lat = lat
		self.lng = lng
		self.alt = alt
		self.situation = situation
		self.op_date = op_date

	def __str__(self):
		s = "Estação: "+self.name+"\n" \
		"Latitude: "+self.lat+"\n" \
		"Longitude: "+self.lng+"\n" \
		"Altitude: "+self.alt+"\n" \
		"Situação: "+self.situation+"\n" \
		"Latitude: "+self.lat+"\n" \
		"Em operação desde "+self.op_date
		return s

def getConsulta(session, url):
	response = session.get(url)

	text = response.content
	text_splited = text.split("--------------------")
	descricao = text_splited[2]
	descricao_splited = descricao.split("\n")
	descricao_splited = descricao_splited[1:(len(descricao_splited)-1)]
	desc_name = descricao_splited[0].split(":", 1)[1].strip()
	desc_lat = descricao_splited[1].split(":", 1)[1].strip()
	desc_lng = descricao_splited[2].split(":", 1)[1].strip()
	desc_alt = descricao_splited[3].split(":", 1)[1].strip()
	desc_sit = descricao_splited[4].split(" ")[1].strip()
	desc_op_date = descricao_splited[5].split(":", 1)[1].strip()

	data_consulta = descricao_splited[6].split(":", 1)[1].strip()

	e = Estacao(desc_name, desc_lat, desc_lng, desc_alt, desc_sit, desc_op_date)
	
	dados = text_splited[4]
	dados.replace(";", ",")
	dados_splited = dados.split("\n")
	dados_splited = dados_splited[1:(len(dados_splited)-1)]

	#for linha in descricao_splited:
	#	print "%s" % linha

	print e

	print "\n"

	for linha in dados_splited:
		print "%s" % linha

	print "Total: %d" % (len(dados_splited))

def getCookieFile(file_name):
	f = open(file_name)
	cookie = f.readline()
	if len(cookie) > 0:
		cookie = ast.literal_eval(cookie)
	else:
		cookie = {}
	f.close()
	return cookie

def setCookieFile(file_name, cookie):
	f = open(file_name, "w")
	f.write(cookie.__str__())
	f.close()


def checkSessionCookie(session):
	#URL de checagem para ver se esta logado
	url = 'http://www.inmet.gov.br/projetos/rede/pesquisa/mapas_mensal_sem.php'
	response = session.post(url)
	if not('<input type="text" size=51 maxlength=50 name="mCod"' in response.content):
		return True
	else:
		return False

def login(session):
	cookie_file = 'session_cookie.txt'
	cookie = getCookieFile(cookie_file)
	session.cookies = requests.utils.cookiejar_from_dict(cookie)

	# check if cookie from file is OK
	if(checkSessionCookie(session)):
		return True
	
	#IF NOT OK, then ask to user
	data = {}
	data['mCod'] = raw_input("Login: ")
	data['mSenha'] = raw_input("Password: ")
	response = session.post('http://www.inmet.gov.br/projetos/rede/pesquisa/inicio.php', data)
	
	#IF OK then return true, else FALSE
	if(checkSessionCookie(session)):
		#grava a nova cookie no arquivo
		setCookieFile(cookie_file, session.cookies.get_dict())
		return True


	

		
	return False


def main():

	session = requests.Session()
	
	logado = login(session)
	
	if logado:
		url = 'http://www.inmet.gov.br/projetos/rede/pesquisa/gera_serie_txt_mensal.php?&mRelEstacao=82487&btnProcesso=serie&mRelDtInicio=01/07/2015&mRelDtFim=25/07/2016&mAtributos=,,,,,,,,,,,,1,1,1,1'
		#url = 'http://www.inmet.gov.br/projetos/rede/pesquisa/gera_serie_txt.php?&mRelEstacao=82024&btnProcesso=serie&mRelDtInicio=01/01/1900&mRelDtFim=28/07/2016&mAtributos=1,1,,,1,1,,1,1,,,1,,,,,'
		getConsulta(session, url)
	


if __name__ == '__main__':
	main()