#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests

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

def getHtml():
	return ""

def getCookie():
	session = requests.Session()
	data = {}
	#fazer um esquema de salvar o cookie em um arquivo.
	#Tentar se conectar com o cookie e caso nao de pedir um novo para o usuario (email e senha)
	#se nao vai ficar pedindo toda a hora
	data['mCod'] = raw_input("Seu Login: ")
	data['mSenha'] = raw_input("Informe a senha: ")
	response = session.post('http://www.inmet.gov.br/projetos/rede/pesquisa/inicio.php', data)
	
	print session.cookies.get_dict()
	print "\n"

	#url = 'http://www.inmet.gov.br/projetos/rede/pesquisa/gera_serie_txt_mensal.php?&mRelEstacao=82487&btnProcesso=serie&mRelDtInicio=01/07/2015&mRelDtFim=25/07/2016&mAtributos=,,,,,,,,,,,,1,1,1,1'
	url = 'http://www.inmet.gov.br/projetos/rede/pesquisa/gera_serie_txt.php?&mRelEstacao=82024&btnProcesso=serie&mRelDtInicio=01/01/1900&mRelDtFim=28/07/2016&mAtributos=1,1,,,1,1,,1,1,,,1,,,,,'
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


def main():

	getCookie()
	


if __name__ == '__main__':
	main()