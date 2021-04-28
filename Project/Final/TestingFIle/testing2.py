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
def search_condition():
    instruction = '''What kind of filtering condition would you like?
    1. filtered by Rating first and ordered by ReviewCount.
    2. filtered by Rating first and ordered by Price.
    3. filtered by ReviewCount first and ordered by Rating.
    4. filtered by ReviewCount first and ordered by Price.
    5. filtered by Price first and ordered by Rating.
    6. filtered by Price first and ordered by ReviewCount.
    '''
    option_list = ['1','2','3','4','5','6']
    rating_list = ["0", '0.5','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0']
    price_list = ["0", '1','2','3','4','5']
    while True:
        print(instruction)
        usr_input = input("what's your choice? from 1 to 6 ")
        if usr_input in option_list:
            if usr_input == "1":
                query_list = ["R.Rating", "R.ReviewCount"]
                print("Rating range:", rating_list)
                usr_input2 =input("Enter the number, please! ")
                if usr_input2 in rating_list:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")
            elif usr_input == "2":
                query_list = ["R.Rating", "R.Price"]
                print("Rating range:", rating_list)
                usr_input2 =input("Enter the number, please! ")
                if usr_input2 in rating_list:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")
            elif usr_input == "3":
                query_list = ["R.ReviewCount", "R.Rating"]
                print("ReviewCount range: at least 1")
                usr_input2 =input("Enter the number, please! ")
                if bool(int(usr_input2))==True and int(usr_input2) > 0:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")

            elif usr_input == "4":
                query_list = ["R.ReviewCount", "R.Price"]
                print("ReviewCount range: at least 1")
                usr_input2 =input("Enter the number, please! ")
                if bool(int(usr_input2))==True and int(usr_input2) > 0:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")

            elif usr_input == "5":
                query_list = ["R.Price", "R.Rating"]
                print("Price range:", price_list)
                usr_input2 =input("Enter the number, please! ")
                if usr_input2 in price_list:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")
            elif usr_input == "6":
                query_list = ["R.Price", "R.ReviewCount"]
                print("Price range:", price_list)
                usr_input2 =input("Enter the number, please! ")
                if usr_input2 in price_list:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")
        else:
            print("invalid input!, please try again!")
    return query_list

def search_order():
    instruction = '''which order would you like?
    1, in ascending order.
    2, in descending order.
    '''
    option_list = ['1','2']
    print(instruction)
    while True:
        usr_input = input("what's your choice? from 1 to 2 ")
        if usr_input in option_list:
            if usr_input == "1":
                query_word = "ASC"
                break
            elif usr_input == "2":
                query_word = "DESC"
                break
        else:
            print("invalid input!, please try again!")
    return query_word

def search_number():
    instruction = '''How many data do you want to search?
    ranging for 1 to 20
    '''
    print(instruction)
    option_list  = ["1",'2','3','4','5','6','7','8','9','10','11',"12",'13','14','15','16','17','18','19','20']
    while True:
        usr_input = input("what's your choice? from 1 to 20 ")
        if usr_input in option_list:       
            query_word = usr_input
            break
        else:
            print("invalid input!, please try again!")
    return query_word

def sql_query():
    query_string1 = '''SELECT F.RestaurantName, F.PhoneNumber, F.Rating, F.ReviewCount, F.Price, F.Address FROM FOOD_RESULT 
    AS F JOIN RESTAURANT_RESULT AS R  ON F.RefId = R.RefId 
    '''
    init_list = search_condition()
    b_word = search_order()
    c_word = search_number()
    init_list.append(b_word) 
    init_list.append(c_word) 
    query_string2 = f'WHERE {init_list[0]} > {init_list[2]} ORDER BY {init_list[1]} {init_list[3]} LIMIT {init_list[4]}'
    
    return query_string1 + query_string2

def turn_to_list(alist):
    outer_list = []
    for idx in range(len(alist)):
        inner_list = []
        for ele in alist[idx]:
            inner_list.append(ele)
        outer_list.append(inner_list)
    return outer_list


def array_output(alist):
    outer_row = []
    for row in alist:
        trimmed_row=[]
        for i in range(len(row)):
            if type(row[i]) == str and len(row[i]) > 15:
                trimmed_row.append('{:.<14}..'.format(row[i][0:14]))
            else:
                trimmed_row.append(row[i])
        outer_row.append(trimmed_row)
    for ele in outer_row:
        print('{:<16}{:<16}{:<5}{:<5}{:<5}'.format(ele[0],ele[1],ele[2],ele[3],ele[4]))


def sql_execute(query_term):
    final_list = []
    conn = sqlite3.connect('practice.db')
    cur = conn.cursor()
    result = cur.execute(query_term).fetchall()
    for ele in result:
        if ele not in final_list:
            final_list.append(ele)
        else:
            final_list = final_list
    final_result = turn_to_list(final_list)
    return final_result

def draw_barplot(alist):
    xval = []
    yval1 = []
    yval2 = []
    yval3 = []
    fig = make_subplots(rows=2, cols=3, subplot_titles=("Rate", "Review_count ", "price_range"))

    for ele in alist:
        xval.append(ele[0])
        yval1.append(ele[2])
        yval2.append(ele[3])
        yval3.append(ele[4])
    fig.add_trace(go.Bar(x=xval, y=yval1),row=1 , col=1)
    fig.add_trace(go.Bar(x=xval, y=yval2), row=1 , col=2)
    fig.add_trace(go.Bar(x=xval, y=yval3), row=1 , col=3)
    fig.update_layout(showlegend=False)
    fig.show()

def draw_radarplot(alist):

    cate = ["AverageRating", "Review", "Price"]
    fig = go.Figure()
    for i in range(len(alist)):
        fig.add_trace(go.Scatterpolar(r=[alist[i][2], alist[i][3], 1],theta=cate, fill='toself',name=alist[i][0]))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True,range=[0, 5])),showlegend=True)

    fig.show()
query_result = sql_query()
print(query_result)
final_result = sql_execute(query_result)
#draw_radarplot(final_result)
draw_barplot(final_result)
array_output(final_result)
