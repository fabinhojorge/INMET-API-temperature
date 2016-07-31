#!/usr/bin/python
import re


file_name = "todas_estacoes_automaticas_raw"



f = open("../dados/"+file_name)
text = f.readlines()
station_numbers = []

for t in text:
	if ""