'''
#parse the query result for food (need to add cache code)
outer_list = []
for idx in range(len(business_data["businesses"])):
    for ele in business_data["businesses"][idx]:
        inner_list = []
        inner_list.append(idx)   
        inner_list.append(business_data["businesses"][idx]["name"])
        inner_list.append(business_data["businesses"][idx]["display_phone"])    
        inner_list.append(business_data["businesses"][idx]["review_count"])
        inner_list.append(business_data["businesses"][idx]["rating"])
        inner_list.append(business_data["businesses"][idx]["location"]['display_address'])
        inner_list.append(business_data["businesses"][idx]["coordinates"]['longitude'])
        inner_list.append(business_data["businesses"][idx]["coordinates"]['latitude'])
        inner_list.append(business_data["businesses"][idx]["url"])
        inner_list.append(business_data["businesses"][idx]["id"])
    outer_list.append(inner_list)

def load_cache():
    ''' To read the dictionary from the cache file if it exists, if not, create
    an empty dictionary

    Parameters
    ----------
    None

    Returns
    -------
    dict
        information store in the cache, which is a dictionary
    '''
    try:
        cache_file = open('RestaruantOrFood.json', 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache

def load_cache1():
    ''' To read the dictionary from the cache file if it exists, if not, create
    an empty dictionary

    Parameters
    ----------
    None

    Returns
    -------
    dict
        information store in the cache, which is a dictionary
    '''
    try:
        cache_file = open('RestaruantOrFood.json', 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache


cach_dict = load_cache()

if query_string not in cach_dict.keys():
    print("fetching data from API")
    cach_dict[query_string] = outer_list
else:
    print("readling from cache ")
    cach_dict = cach_dict

# create json file for cache and furture use [need to add with cache]
with open('RestaruantOrFood.json', 'w') as outfile:
    json.dump(cach_dict, outfile)

# create csv file for SQL database and furture use [need to add with cache]
headers = ['RestaurantName', 'PhoneNumber', 'ReviewCount', 'Rating','Address', 'Longitude', 'Latitude', 'UrlLink', 'id']

with open(filenameC, 'w') as outfile:
    csvwriter = csv.writer(outfile)
    csvwriter.writerow(headers)
    csvwriter.writerows(outer_list)


# This section for generate SQL database and plug in the value
conn = sqlite3.connect("FOODSEARCH.db")
conn.execute("PRAGMA foreign_keys = ON")
c = conn.cursor()
    #Read the csv file, plug in the value

read_clients = pd.read_csv(f'/Users/pkuo/Desktop/FinalProject/{filenameC}')
if len(query_name) == 0:
    read_clients.to_sql('RESTAURANT_RESULT', conn, if_exists='append', index = False) # if_exist, it will replace the old value, if not exist, it will append
elif len(query_name) != 0:
    read_clients.to_sql('FOOD_RESULT', conn, if_exists='append', index = False) # if_exist, it will replace the old value, if not exist, it will append

'''