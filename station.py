#!/usr/bin/env python
# -*- coding: utf-8 -*-

from state import State


class Station:
	"""This class keep the information related for each one of the stations in station list. And also their
	observations"""
	
	def __init__(self, name_complete, lat, lng, alt, status, op_date):
		"""Constructor of the Station class: name_complete, lat, lng, alt, status, op_date."""

		self.name_complete = name_complete
		self.lat = lat
		self.lng = lng
		self.alt = alt
		self.status = status
		self.op_start_date = op_date
		self.weather_observation = []
		self.weather_observation_header = ''

		name_splitted = self.name_complete_parser(name_complete)
		self.name = name_splitted['name']
		self.state_initials = name_splitted['state_initials']
		state = State.find_state_by_key(self.state_initials)
		self.state_name = state['name']
		self.state_region = state['region']
		self.omm_code = name_splitted['omm_code']

	@staticmethod
	def name_complete_parser(name_complete):
		"""(Static Method) Parser that given the station name extract from the observation page, it returns a Dict with
		the name, state_initials and omm_code"""

		s = name_complete.split('-')
		name = s[0].strip()
		s = s[1].split('(')
		state_initials = s[0].strip()
		omm_code = s[1].replace('OMM: ', '').replace(')', '')

		return {'name': name, 'state_initials': state_initials, 'omm_code': omm_code}

	@staticmethod
	def parser(data):
		"""(Static Method) Parser that given the Station information it returns a Station object."""
		ds = data.split('\n')
		return Station(ds[1][20:], ds[2][20:], ds[3][20:], ds[4][20:], ds[5], ds[6][20:])

	@staticmethod
	def observation_parser(data):
		"""(Static Method) Parser that given a observation data it returns a Dict with header and data."""
		ds = data.split('\n')
		ds = list(filter(None, ds))
		return {'header': ds[0], 'data': ds[1:], }

	def set_observation(self, observation):
		"""Given an observation parser object, it sets the observation and observation_header attributes for the Station
		class."""
		self.weather_observation_header = observation['header']
		self.weather_observation = observation['data']

	@staticmethod
	def get_station_header():
		"""(Static Method) It returns the fixed header fields for the Station. This is used to create the CSV header"""
		return [
			'CodigoOMM', 'NomeEstacao', 'Estado', 'EstadoDesc', 'EstadoRegiao', 'Latitude', 'Longitude', 'Altitude',
			'EstacaoStituacao', 'OperanteDesde', ]

	def get_station_information(self):
		"""It returns the Station information as a list"""
		return [
			self.omm_code, self.name, self.state_initials, self.state_name, self.state_region, self.lat, self.lng,
			self.alt, self.status, self.op_start_date, ]

	def __str__(self):
		return "{0}|{1}/{2}/{3}/{4})| Lat: {5}| Lng: {6}| Alt: {7}| Situação: {8}| Em operação desde {9}"\
			.format(
				self.omm_code, self.name, self.state_initials, self.state_name, self.state_region, self.lat, self.lng,
				self.alt, self.status, self.op_start_date)
