# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 03:08:30 2016

@author: fabinho
"""

from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib

data = pd.read_csv("../dados/estacao_dados.csv");

print data[data.altitude == data.altitude.max()]

