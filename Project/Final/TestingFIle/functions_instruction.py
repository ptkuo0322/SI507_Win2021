read_loc_cache():
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

write_to_Loc_cache(cache_dict):
    ''' output the data searched by location to json file
    
    Parameters
    ----------
    cache_dict
        the searched data stored in dictionary format

    Returns
    -------
    none
    '''
write_to_Food_cache(cache_dict):
    ''' output the data searched by food or restaurant 
         along with location to json file
    
    Parameters
    ----------
    cache_dict
        the searched data stored in dictionary format

    Returns
    -------
    none
    '''
write_to_csv(result, filename):
    ''' output the search result with headers to csv file 
    
    Parameters
    ----------
    result
        the search result
    
    filename
        the csv file

    Returns
    -------
    none
    '''

read_rest_cache():
    ''' read the dictionary from the cache file if it exists, 
        if not, create an empty dictionary
    
    Parameters
    ----------
    None

    Returns
    -------
    dictonary 
        the data in dictionary format that read from json file
    '''
read_loc_cache():
    ''' read the dictionary from the cache file if it exists, 
        if not, create an empty dictionary
    
    Parameters
    ----------
    None

    Returns
    -------
    dictonary 
        the data in dictionary format that read from json file
    '''

search_yelp(query_name, query_location):
    ''' search the food/restaurant information on Yelp
    
    Parameters
    ----------
    query_name
        either restaurant name or food name 

    Returns
    -------
    outer_list 
        a list with specific information about the search results
    '''

update_database(query_name):
    ''' update the data stored in SQL database
    
    Parameters
    ----------
    query_name
        either restaurant name or food name 

    Returns
    -------
    none 
        
    '''

path_decision(query_name, query_location):
    ''' update the cache and csv files based on the query information
    
    Parameters
    ----------
    query_name
        either restaurant name or food name 

    query_location
        the places such as cities, countries or so

    Returns
    -------
    cache_dict
        the dictionary with search results 
    '''
yt_search():
        ''' search the related videos on Youtube and display on the browsers
    
    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
open_youtube(link_list):
    ''' ask the user whether to open the videos on YouTube
    
    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
open_static_map(UrlLink):
    ''' ask the user whether to show the search results on static google map
    
    Parameters
    ----------
    UrlLink
        the url that links to google map

    Returns
    -------
    None
    '''
count_query_list(loc_list):
    ''' construct the information in specific format for static google API
    
    Parameters
    ----------
    loc_list
        the list that contains all the location information of the search results

    Returns
    -------
    final_list
        the list contains the query information for static map API
    '''
show_related_loc(query_name, query_location):
    ''' display the searched restaurants/foods with relative location 
        in both command line prompt and figure format
    
    Parameters
    ----------
    query_name
        either restaurant name or food name 

    query_location
        the places such as cities, countries or so

    Returns
    -------
    loc_list
        the list contains the location information about the searched results
    '''
go_direction(query_name, query_location, query_string):
    ''' display the direction of the searched result on google map
    
    Parameters
    ----------
    query_name
        either restaurant name or food name 

    query_location
        the places such as cities, countries or so
    
    query_string
        the string constructed by query_name and query_location

    Returns
    -------
    none
    '''

draw_barplot(alist):
    ''' draw the bar plot
    
    Parameters
    ----------
    alist
        the list contains the information for bar plots
        
    Returns
    -------
    none
    '''

draw_radarplot(alist):
    ''' draw the radar plot
    
    Parameters
    ----------
    alist
        the list contains the information for radar plots
        
    Returns
    -------
    none
    '''
search_condition():
    ''' construct the query information for SQL database
    
    Parameters
    ----------
    None
        
    Returns
    -------
    query_list
        the query list for SQL database
    '''
search_order():
    ''' construct the query information for SQL database
    
    Parameters
    ----------
    None
        
    Returns
    -------
    query_word
        the query word for SQL database
    '''
search_number():
    ''' construct the query information for SQL database
    
    Parameters
    ----------
    None
        
    Returns
    -------
    query_word
        the query word for SQL database
    '''

sql_query():
    ''' construct the ultimate query information for SQL database
    
    Parameters
    ----------
    None
        
    Returns
    -------
    query_term
        the ultimate query word for SQL database
    '''
array_output(alist):
    ''' display the SQL data in specific format(2D-array)
    
    Parameters
    ----------
    alist
        the list contains SQL data
        
    Returns
    -------
    None
    '''

turn_to_list(alist):
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

sql_execute(query_term):
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