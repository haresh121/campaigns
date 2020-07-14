# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 09:22:48 2020

@author: haresh
"""
# %% Cell1
import pandas as pd
from time import strftime

# %% Cell2
class Platform_(object):
    def __init__(self):
        self.ads_len = 0
    
    def get_source(self, file="./campaigns.csv"):
        self.__ads__ = pd.read_csv(file)
        
    def run_auction(self, auction_data):
        pass