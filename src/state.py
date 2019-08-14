#!/usr/bin/env python
# -*- coding: utf-8 -*-


class State:
    """This is a helper class that contains the Brazilian states and their respective regions."""

    __state = {
        'AC': {'name': 'Acre', 'region': 'Norte'},
        'AL': {'name': 'Alagoas', 'region': 'Nosdeste'},
        'AP': {'name': 'Amapa', 'region': 'Norte'},
        'AM': {'name': 'Amazonas', 'region': 'Norte'},
        'BA': {'name': 'Bahia', 'region': 'Nordeste'},
        'CE': {'name': 'Ceara', 'region': 'Nordeste'},
        'DF': {'name': 'Distrito_Federal', 'region': 'Centro-Oeste'},
        'ES': {'name': 'Esperito_Santo', 'region': 'Sudeste'},
        'GO': {'name': 'Goias', 'region': 'Centro-Oeste'},
        'MA': {'name': 'Maranhao', 'region': 'Nordeste'},
        'MT': {'name': 'Mato_Grosso', 'region': 'Centro-Oeste'},
        'MS': {'name': 'Mato_Grosso_do_Sul', 'region': 'Centro-Oeste'},
        'MG': {'name': 'Minas_Gerais', 'region': 'Sudeste'},
        'PA': {'name': 'Para', 'region': 'Norte'},
        'PB': {'name': 'Paraiba', 'region': 'Nordeste'},
        'PR': {'name': 'Parana', 'region': 'Sul'},
        'PE': {'name': 'Pernambuco', 'region': 'Nordeste'},
        'PI': {'name': 'Piaui', 'region': 'Nordeste'},
        'RJ': {'name': 'Rio_de_Janeiro', 'region': 'Sudeste'},
        'RN': {'name': 'Rio_Grande_do_Norte', 'region': 'Nordeste'},
        'RS': {'name': 'Rio_Grande_do_Sul', 'region': 'Sul'},
        'RO': {'name': 'Rondonia', 'region': 'Norte'},
        'RR': {'name': 'Roraima', 'region': 'Norte'},
        'SC': {'name': 'Santa_Catarina', 'region': 'Sul'},
        'SP': {'name': 'Sao_Paulo', 'region': 'Sudeste'},
        'SE': {'name': 'Sergipe', 'region': 'Nordeste'},
        'TO': {'name': 'Tocantins', 'region': 'Norte'},
    }

    @classmethod
    def find_state_by_key(cls, key):
        """This is the State.find_state_by_key. It returns the state information given the initials of the respective
        state."""
        if key not in cls.__state.keys():
            return dict()
        return cls.__state[key]

    @classmethod
    def find_state_by_name(cls, name):
        """This is the State.find_state_by_name. It returns the state information given the Name of the respective
        state."""
        return dict(filter(lambda a: str(name).upper() == str(a[1]['name']).upper(), cls.__state.items()))
