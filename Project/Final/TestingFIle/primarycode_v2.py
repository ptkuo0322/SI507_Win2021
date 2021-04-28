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

## general setting 
# This section is for API keys (need to be in secret code)
YELP_API_KEY = secrets.YELP_API_KEY
YELP_BASEURL = 'https://api.yelp.com/v3/businesses/search'
YtWatchhUrl = "https://www.youtube.com/watch?"
map_url = "https://www.google.com/maps/search/?api=1"
YOUTUBE_API_KEY = secrets.YOUTUBE_API_KEY
MAP_API_KEY = secrets.MAP_API_KEY
HEADERS = {'Authorization': 'bearer %s' % YELP_API_KEY}
symbol_list = ['A','B','C','D','E','F','G','H','I','J','H']
query_list0 = []
query_list1 = []
query_list2 = []
query_list3 = []
query_list4 = []
name_list = []
final_list = []


#headers = ['RestaurantName', 'PhoneNumber', 'ReviewCount', 'Rating','Address', 'Longitude', 'Latitude', 'UrlLink', 'id']
def read_loc_cache():
    # To read the dictionary from the cache file if it exists, if not, create an empty dictionary
    try:
        cache_file = open('ResultofLocation.json', 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache  #return a dictionary

def write_to_Loc_cache(cache_dict):
    with open("ResultofLocation.json", "w") as outputfile:
            json.dump(cache_dict, outputfile)

def write_to_Food_cache(cache_dict):
    with open("ResultofFOOD.json", "w") as outputfile:
            json.dump(cache_dict, outputfile)

    
def write_to_csv(result, filename):
    file_exists = os.path.isfile(filename)
    with open(filename, 'a+', newline='') as outfile:
        headers = ['id','RestaurantName', 'PhoneNumber', 'ReviewCount', 'Rating', 'Price', 'Address', 'Longitude', 'Latitude', 'UrlLink', 'RefId']
        file_is_empty = os.stat(filename).st_size == 0
        writer = csv.writer(outfile)
        if file_is_empty:
            writer.writerow(headers)
        writer.writerows(result)    


def read_rest_cache():
    # To read the dictionary from the cache file if it exists, if not, create an empty dictionary
    try:
        cache_file = open('ResultofFOOD.json', 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache  #return a dictionary

def read_loc_cache():
    # To read the dictionary from the cache file if it exists, if not, create an empty dictionary
    try:
        cache_file = open('ResultofLocation.json', 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache  #return a dictionary

def search_yelp(query_name, query_location):
    PARAMETERS = {'term': query_name,'radius': 10000,'location': query_location, 'limit': 50}
    response = requests.get(url = YELP_BASEURL,params = PARAMETERS,headers = HEADERS)
    res_data = response.json()
    outer_list = []
    for idx in range(len(res_data["businesses"])):
        for ele in res_data["businesses"][idx]:
            inner_list = []
            inner_list.append(idx)   
            inner_list.append(res_data["businesses"][idx]["name"])
            inner_list.append(res_data["businesses"][idx]["display_phone"])    
            inner_list.append(res_data["businesses"][idx]["review_count"])
            inner_list.append(res_data["businesses"][idx]["rating"])
            if 'price' not in res_data["businesses"][idx].keys():
                inner_list.append("0")
            else:
                if res_data['businesses'][idx]['price'] = '$':
                    res_data['businesses'][idx]['price'] = 1
                    inner_list.append(res_data['businesses'][idx]['price'])
                elif res_data['businesses'][idx]['price'] = '$$':
                    res_data['businesses'][idx]['price'] = 2
                    inner_list.append(res_data['businesses'][idx]['price'])
                if res_data['businesses'][idx]['price'] = '$$$':
                    res_data['businesses'][idx]['price'] = 3
                    inner_list.append(res_data['businesses'][idx]['price'])
                if res_data['businesses'][idx]['price'] = '$$$$':
                    res_data['businesses'][idx]['price'] = 4
                    inner_list.append(res_data['businesses'][idx]['price'])
                if res_data['businesses'][idx]['price'] = '$$$$$':
                    res_data['businesses'][idx]['price'] = 5
                    inner_list.append(res_data['businesses'][idx]['price'])
            inner_list.append(res_data["businesses"][idx]["location"]['display_address'])
            inner_list.append(res_data["businesses"][idx]["coordinates"]['longitude'])
            inner_list.append(res_data["businesses"][idx]["coordinates"]['latitude'])
            inner_list.append(res_data["businesses"][idx]["url"])
            inner_list.append(res_data["businesses"][idx]["id"])
            #inner_list.append(res_data["businesses"][idx]["price"])
        outer_list.append(inner_list)
    return outer_list

def update_database(query_name):
    conn = sqlite3.connect("practice.db")
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    if len(query_name) == 0:
        read_clients = pd.read_csv('/Users/pkuo/Desktop/SI507_finalProject/FInalcode/FinalProject/loc.csv')
        read_clients.to_sql('RESTAURANT_RESULT', conn, if_exists='replace', index = False) # if_exist, it will replace the old value, if not exist, it will append
    elif len(query_name) != 0:
        read_clients = pd.read_csv('/Users/pkuo/Desktop/SI507_finalProject/FInalcode/FinalProject/food.csv')
        read_clients.to_sql('FOOD_RESULT', conn, if_exists='replace', index = False) # if_exist, it will replace the old value, if not exist, it will append

# phase 3, write the search result to json file with cache
    # read the cache first
def path_decision(query_name, query_location):
    if len(query_name) == 0:
        search_result = search_yelp(query_name, query_location)
        cache_dict = read_loc_cache()
        if query_string not in cache_dict.keys():
            print("fetching data from API")
            cache_dict[query_string] = search_result
            #print(cache_dict[query_string])
            #print(cache_dict)
            write_to_Loc_cache(cache_dict)
            ## write to csv
            filenameC = "loc.csv"
            write_to_csv(search_result,filenameC)
        else:
            print("readling from cache ")
            #print(cache_dict[query_string])
    else:
        search_result = search_yelp(query_name, query_location)
        cache_dict = read_rest_cache()
        if query_string not in cache_dict.keys():
            print("fetching data from API")
            cache_dict[query_string] = search_result
            #print(cache_dict[query_string])
            #print(cache_dict)
            write_to_Food_cache(cache_dict)
            ## write to csv
            filenameC = "food.csv"
            write_to_csv(search_result,filenameC)
        else:
            print("readling from cache ")
            #print(cache_dict[query_string])
    update_database(query_name)
    
    return cache_dict


### for youtube case

def yt_search():
    link = ""
    link_list = []
    result =  path_decision(query_name, query_location)
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    name_list = []
    #print out the restaurant name for usr to choose
    for idx, ele in enumerate(result):
        name_list.append(ele[0])
        print(idx+1, ele[0])

    choose_restaurant = input("which restaurant do you want? Please enter the number")
    time.sleep(1)
    youtube_request = youtube.search().list(part='snippet',q=name_list[int(choose_restaurant)-1],maxResults="2") # maxResult= 0~ 50 default 5 maxResults="2"
    youtube_response = youtube_request.execute()
    for idx in range(len(youtube_response)-2):
        for ele in youtube_response['items'][idx]['snippet']['thumbnails']['default']['url']:
            link += ele
        link_list.append(link.split('/')[-2])
    open_youtube(link_list)


def open_youtube(link_list):
    
    while True:
        ans = input("would you like to open the relative videos on the YouTube? Yes or No ? ")
        if ans.strip(" ").lower() == "yes":
            for ele in link_list:
                webbrowser.open_new("{}v={}".format(YtWatchhUrl,ele))
            break
        elif ans.strip(" ").lower() == "no":
            print("OK! Thank you, let's go to next step!!")
            break
        else:
            print("invalid input! Plsase try again")


# This section for GOOGLE MAP -- show the relative location on a static map
GOOGLEMAP_BASE_URL = "https://maps.googleapis.com/maps/api/staticmap?"

# parameters
#CITY = query_location

def open_static_map(UrlLink):
    
    while True:
        ans = input("would you like to know the relative location on the Map? Yes or No ? ")
        if ans.strip(" ").lower() == "yes":
            webbrowser.open_new(UrlLink)
            break
        elif ans.strip(" ").lower() == "no":
            print("OK! Thank you, let's go to next step!!")
            break
        else:
            print("invalid input! Plsase try again")

            
def count_query_list(alist):

    for idx, ele in enumerate(alist):
        if 40 <= len(alist):
            if idx in range(0,10):
                astring = f"&markers=label:{symbol_list[(idx)]}|{ele}"
                query_list0.append(astring)
            if idx in range(10,20):
                astring = f"&markers=label:{symbol_list[(idx)]}|{ele}"
                query_list1.append(astring)
            if idx in range(20,30):
                astring = f"&markers=label:{symbol_list[(idx)]}|{ele}"
                query_list2.append(astring)
            if idx in range(30,40):
                astring = f"&markers=label:{symbol_list[(idx)]}|{ele}"
                query_list3.append(astring)
            if idx in range(40,51):
                astring = f"&markers=label:{symbol_list[(idx)]}|{ele}"
                query_list4.append(astring)
        elif 30 <= len(alist) < 40:
            if idx in range(0,10):
                astring = f"&markers=label:{symbol_list[(idx)]}|{ele}"
                query_list0.append(astring)
            if idx in range(10,20):
                astring = f"&markers=label:{symbol_list[(idx)]}|{ele}"
                query_list1.append(astring)
            if idx in range(20,30):
                astring = f"&markers=label:{symbol_list[(idx)]}|{ele}"
                query_list2.append(astring)
            if idx in range(30,40):
                astring = f"&markers=label:{symbol_list[(idx)]}|{ele}"
                query_list3.append(astring)
        elif 20 <= len(alist) < 30:
            if idx in range(0,10):
                astring = f"&markers=label:{symbol_list[(idx)]}|{ele}"
                query_list0.append(astring)
            if idx in range(10,20):
                astring = f"&markers=label:{symbol_list[(idx)]}|{ele}"
                query_list1.append(astring)
            if idx in range(20,30):
                astring = f"&markers=label:{symbol_list[(idx)]}|{ele}"
                query_list2.append(astring)
        elif 10 <= len(alist) < 20:
            if idx in range(0,10):
                astring = f"&markers=label:{symbol_list[(idx)]}|{ele}"
                query_list0.append(astring)
            if idx in range(10,20):
                astring = f"&markers=label:{symbol_list[(idx)]}|{ele}"
                query_list1.append(astring)
        elif 0 <= len(alist) < 10:
            astring = f"&markers=label:{symbol_list[(idx)]}|{ele}"
            query_list0.append(astring)  

    if len(alist) < 10:
        final_list.append(query_list0)
    elif 10 <=len(alist) < 20:
        final_list.append(query_list0)
        final_list.append(query_list1)
    elif 20 <=len(alist) < 30:
        final_list.append(query_list0)
        final_list.append(query_list1)
        final_list.append(query_list2)
    elif 30 <=len(alist) < 40:
        final_list.append(query_list0)
        final_list.append(query_list1)
        final_list.append(query_list2)
        final_list.append(query_list3)
    elif 40 <=len(alist):
        final_list.append(query_list0)
        final_list.append(query_list1)
        final_list.append(query_list2)
        final_list.append(query_list3)
        final_list.append(query_list4)
    return final_list

def show_related_loc(query_name, query_location):
    result =  path_decision(query_name, query_location)
    loc_list=[]
    name_list = []
    query_word = ""
    for idx, ele in enumerate(result[query_string]):
        loc= ""
        loc = str(result[query_string][idx][6]) + "," + str(result[query_string][idx][5])
        loc_list.append(loc)
        name_list.append(result[query_string][idx][0])
    result_list = count_query_list(loc_list)
    for idx1, listele in enumerate(result_list):
        for idx, ele in enumerate (listele):
            query_word += ele
            if idx % 10 == 0:
                print(f'This is shown in {idx1+1} page')
            print(symbol_list[idx], name_list[idx+(idx1*10)]) 
        URL = GOOGLEMAP_BASE_URL + "center=" + query_location + "&zoom=13" + "&size=1344x768&scale=2&key=" + MAP_API_KEY +"&maptype=roadmap" + query_word
        print(URL)
        open_static_map(URL)
        URL = ""
        query_word = ""
        return loc_list
# for direction on the google map





'''
def go_direction(query_name, query_location, query_string):
    dict_result = path_decision(query_name, query_location)
    for idx, ele in enumerate(dict_result[query_string]):
        print(idx+1, ele[0])
    while True:
        usr_res = input("Yes or no?")
        if usr_res.strip(" ").lower() == 'yes':
            usr_res = input("Which you would you like to direct to? Enter the number! ")
            if bool(usr_res.strip(" ").isnumeric) =
        if usr_res.strip(" ").isnumeric and  1 <= usr_res.strip(" ") <= len(dict_result[query_string]):
            loc = dict_result[query_string][int(usr_res)-1][6]
            lat = dict_result[query_string][int(usr_res)-1][5]
            coord = str(loc) + "," + str(lat)
            result = map_url + "&query=" + coord
            print(result)
            webbrowser.open_new(result)
            break
        elif usr_res.strip(" ").lower() == 'no':
            print("skip this step!")
            exit()
        else:
            print("invalid input")
'''
query_name = input("please input the food/restaurant")
query_name = query_name.lower().strip(" ")
time.sleep(1)
query_location = input("please input the location")
query_location = query_location.lower().strip(" ")
query_string = query_name + query_location
time.sleep(1)

#result = search_yelp(query_name, query_location)
#with open("test1.json", "w") as obj:
#    json.dump(result, obj)
path_decision(query_name, query_location)
'''
dict_result = path_decision(query_name, query_location)
loc_list = show_related_loc(query_name, query_location)
#show_related_loc(query_name, query_location)
go_direction(query_name, query_location, query_string)

def interactive_promt():
    while True:   
        query_name = input("please input the food/restaurant")
        query_name = query_name.lower().strip(" ")
        time.sleep(1)
        query_location = input("please input the location")
        query_location = query_location.lower().strip(" ")
        query_string = query_name + query_location
        time.sleep(1)

if __name__=="__main__":
    interactive_prompt()
'''


## draw plot


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


def draw_radarplot(alist):

    cate = ["AverageRating", "Review", "Price"]
    fig = go.Figure()
    for i in range(len(alist)):
        fig.add_trace(go.Scatterpolar(r=[alist[i][2], alist[i][3], alist[i][4]],theta=cate, fill='toself',name=alist[i][0]))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True,range=[0, 5])),showlegend=True)

    fig.show()

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
    query_string1 = '''SELECT F.RestaurantName, F.PhoneNumber, F.Rating, F.ReviewCount, F.Price FROM FOOD_RESULT 
    AS F JOIN RESTAURANT_RESULT AS R  ON F.RefId = R.RefId 
    '''
    init_list = search_condition()
    b_word = search_order()
    c_word = search_number()
    init_list.append(b_word) 
    init_list.append(c_word) 
    query_string2 = f'WHERE {init_list[0]} > {init_list[2]} ORDER BY {init_list[1]} {init_list[3]} LIMIT {init_list[4]}'
    
    return query_string1 + query_string2

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

