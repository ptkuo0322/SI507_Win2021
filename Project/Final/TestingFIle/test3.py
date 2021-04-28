import requests
import json
import pandas as pd
import csv 
import sqlite3
from pandas import DataFrame
import webbrowser
import time
from googleapiclient.discovery import build
import secrets
import os
import plotly.graph_objs as go
from plotly.subplots import make_subplots

a = '''SELECT F.RestaurantName, F.PhoneNumber, F.Rating, F.ReviewCount, F.Price FROM FOOD_RESULT 
    AS F JOIN RESTAURANT_RESULT AS R  ON F.RefId = R.RefId 
    WHERE R.RestaurantName = "Frita Bdatidos"'''


def turn_to_list(alist):
    ''' convert the data into list
    
    Parameters
    ----------
    alist
        the original information
        
    Returns
    -------
    outer_list
        the converted data in list format
    '''
    outer_list = []
    for idx in range(len(alist)):
        inner_list = []
        for ele in alist[idx]:
            inner_list.append(ele)
        outer_list.append(inner_list)
    return outer_list

def sql_execute(query_term):
    ''' search the SQL database
    
    Parameters
    ----------
    query_term
        the query string for SQL database
        
    Returns
    -------
    final_result
        the search results
    '''
    final_list = []
    conn = sqlite3.connect('practice1.db')
    cur = conn.cursor()
    result = cur.execute(query_term).fetchall()
    for ele in result:
        if ele not in final_list:
            final_list.append(ele)
        else:
            final_list = final_list
    final_result = turn_to_list(final_list)
    return final_result

b = sql_execute(a)
print(b)