import sqlite3
import plotly.graph_objs as go
import pandas as pd
from plotly.subplots import make_subplots

def decide_sql_query():
    rating_scale  = ["0", '0.5','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0']
    price_scale  = ["0", '1','2','3','4','5']
    order_scale  = ["ASC", "DESC"]
    default_list = ['A','B','C','DESC',10']
    while True:
        rating_sca = ("What is the lowest rating would you like to search? sacle from 0 to 5, separate by 0.5")
        if rating_sca not in rating_scale:
            print("invalid value! Please try again")
        else:
            default_list[0] = rating_sca
            break
    while True:
        price_sca = ("What is the lowest price range would you like to search? sacle from 0 to 5, separate by 1")
        if price_sca not in price_scale:
            print("invalid value! Please try again")
        else:
            default_list[1] = price_sca
            break
    while True:
        review_sca = ("What is the lowest number of revuew would you like to search? must be a integer")
        if bool(int(review_sca.isdigit()) == False
            print("invalid value! Please try again")
        else:
            default_list[2] = review_sca
            break
    while True:
        order_sca = ("What order of data would you like, ASC or DESC, default value = DESC")
        if order_sca.strip(" ").upper() not in order_scale:
            print("invalid value! Please try again")
        else:
            default_list[3] = order_sca
            break
    while True:
        data_sca = ("How much data do you wnat?, from 1 to 20, default value = 10")
        if bool(int(data_sca.strip(" "))) = True and 1 <= int(data_sca.strip(" ") <=20:
            default_list[4] = data_sca
            break
        else:
            print("invalid value! Please try again")
    return default_list

    


def sql_query()
conn = sqlite3.connect('practice.db')
cur = conn.cursor()
sql_query_result= '''SELECT F.RestaurantName, F.PhoneNumber, F.Rating, F.ReviewCount, F.Price FROM FOOD_RESULT AS F JOIN RESTAURANT_RESULT AS R  ON F.RefId = R.RefId 
WHERE R.Rating > 3.0 ORDER BY R. ReviewCount DESC LIMIT 50'''
result = cur.execute(sql_query_result).fetchall()
new_list = []

for ele in result:
    if ele not in new_list:
        new_list.append(ele)
    else:
        new_list=new_list


outer_list = []
for ele in new_list:
    inner_list = []
    for ele1 in ele:
        inner_list.append(ele1)
    outer_list.append(inner_list)
print(outer_list)

def scale_convert(alist):
    ''' convert the data scale
    
    Parameters
    ----------
    alist
        the list contains the data for conversion
        
    Returns
    -------
    final_result
        the search results
    '''
    for ele in alist:
        print(ele[4])
        if ele[3] >= 2000:
            ele[3] = 5
        elif 2000 > ele[3] >= 1800:
            ele[3] = 4.75
        elif 1800 > ele[3] >= 1600:
            ele[3] = 4.5
        elif 1600 > ele[3] >= 1400:
            ele[3] = 4.25
        elif 1400 > ele[3] >= 1200:
            ele[3] = 4.0
        elif 1200 > ele[3] >= 1000:
            ele[3] = 3.75
        elif 1000 > ele[3] >= 800:
            ele[3] = 3.5
        elif 800 > ele[3] >= 600:
            ele[3] = 3.25
        elif 600 > ele[3] >= 400:
            ele[3] = 3.0
        elif 400 > ele[3] >= 200:
            ele[3] = 2.75
        elif 200 > ele[3] >= 100:
            ele[3] = 2.5    
        elif 100 > ele[3] >= 50:
            ele[3] = 2.0  
        elif 50 > ele[3] >= 0:
            ele[3] = 1.0
        if ele[4] == '$':
            ele[4] = 1
        elif ele[4] == "$$":
            ele[4] = 2
        elif ele[4] == "$$$":
            ele[4] = 3
        elif ele[4] == "$$$$":
            ele[4] = 4
        elif ele[4] == "$$$$$":
            ele[4] = 5
        else:
            ele[4] = 0
    return alist

def draw_barplot(alist):
    usr_input = input("which one do you want to comapre, Average rating = 1, Review_account =0")
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
    #bar_data1 =go.Bar(x=xval, y=yval)

    #basic_layout = go.Layout(title = 'result')
    #fig = go.Figure(data=bar_data, layout = basic_layout)
    #fig.show()

draw_barplot(outer_list)

def draw_radarplot(alist):

    cate = ["AverageRating", "Review", "Price"]
    fig = go.Figure()
    for i in range(len(outer_list)):
        fig.add_trace(go.Scatterpolar(r=[outer_list[i][2], outer_list[i][3], outer_list[i][4]],theta=cate, fill='toself',name=new_list[i][0]))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True,range=[0, 5])),showlegend=True)

    fig.show()
