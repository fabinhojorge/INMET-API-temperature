#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .state import State


class Station:
	
	def __init__(self, name_complete, lat, lng, alt, situation, op_date):

		self.name = name_complete
		self.state_initials = 'SP'
		self.state_name = State.find_state_by_key('SP')['name']
		self.state_region = State.find_state_by_key('SP')['region']
		self.omm_code = -1
		self.lat = lat
		self.lng = lng
		self.alt = alt
		self.situation = situation
		self.op_start_date = op_date

	def __str__(self):
		return "Estação: {0}\nLatitude: {1}\nLongitude: {2}\nAltitude: {3}\nSituação: {4}\nEm operação desde {0}"\
			.format(self.name, self.omm_code, self.lat, self.lng, self.alt, self.situation, self.op_start_date)
