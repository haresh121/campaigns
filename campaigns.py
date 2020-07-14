# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 09:22:48 2020

@author: haresh
"""
# %% Imports
import pandas as pd
from time import strftime
from json import load

# %% Class Platform
class Platform_(object):
    def __init__(self):
        self.ads_len = 0
    
    def get_source(self, file="./campaigns.csv"):
        self.__ads__ = pd.read_csv(file)
        
    def run_auction(self, auction_data, n_slots):
        assert type(auction_data) == dict
        amt = sorted(auction_data, key=auction_data.get)[::-1][0:n_slots]
        return amt
# %% Class User
class User(object):
    ad_types = list(pd.read_csv('./campaigns.csv')['type'])
    def __init__(self):
        with open('ads.json') as adfile:
            self.ads_list = load(adfile)
    def search_assist(self, o_req):
        # here ml search req categorizer comes which helps
        # to categorise the search requests that arrive
        pass
    def search(self, req):
        type = req['type']
        self.req_time = strftime("%d/%m/%Y - %H:%M:%S")
        return self.response(type)
    def response(self, type):
        ads = self.ads_list[type]
        return ads