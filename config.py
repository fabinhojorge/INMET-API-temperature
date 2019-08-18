#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Fabio Rodrigues Jorge
Email: fabinhojorgenet@gmail.com
Description: Config file.
"""

LOGIN = {
    'url': 'http://www.inmet.gov.br/projetos/rede/pesquisa/inicio.php',
    'username': '<USER>',
    'password': '<PASS>',
}

URL_TEMPLATE = {
    'HOUR': 'http://www.inmet.gov.br/projetos/rede/pesquisa/gera_serie_txt.php?&mRelEstacao={omm_code}'
            '&btnProcesso=serie&mRelDtInicio={start_date}&mRelDtFim={end_date}&mAtributos=1,1,,,1,1,,1,1,,,1,,,,,',
    'DAY': 'http://www.inmet.gov.br/projetos/rede/pesquisa/gera_serie_txt.php?&mRelEstacao={omm_code}'
           '&btnProcesso=serie&mRelDtInicio={start_date}&mRelDtFim={end_date}&mAtributos=,,1,1,,,,,,1,1,,1,1,1,1,',
    'DAYFULL': 'http://www.inmet.gov.br/projetos/rede/pesquisa/gera_serie_txt.php?&mRelEstacao={omm_code}'
               '&btnProcesso=serie&mRelDtInicio={start_date}&mRelDtFim={end_date}'
               '&mAtributos=1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1',
    'MONTH': 'http://www.inmet.gov.br/projetos/rede/pesquisa/gera_serie_txt_mensal.php?&mRelEstacao={omm_code}'
             '&btnProcesso=serie&mRelDtInicio={start_date}&mRelDtFim={end_date}'
             '&mAtributos=1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1',
}
