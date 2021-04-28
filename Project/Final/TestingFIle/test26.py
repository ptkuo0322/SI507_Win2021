
instruction = '''This program provides two way of search:
---------------------------------------------------------------------------------
1. Instant search on Yelp for specific type of food or restaurant
2. Search the Restaurants existing in the database based on Reviews/Rating/Price
---------------------------------------------------------------------------------
note: option 1 is able to expand the database used in option2.
'''
instructionforone:'''
this option allows you to search the Food or restaruant On Yelp. 
You are required to enter the following information:
-------------------------------------------------------------------------------------------
    -- Food/Restaurant (optional)
    -- Location (required)
-------------------------------------------------------------------------------------------

    You would be able to see the following information:

-------------------------------------------------------------------------------------------
    -- The search results in text format
    -- The related videos about search results on YouTube
    -- The location information of the search results on static google map
    -- The direction to the search results on google map
-------------------------------------------------------------------------------------------

    Also, you can type "exit" to quit anytime
'''

instructionfortwo:'''
This option allows you to search and compare the restaruant in particular state of USA
You are required to enter the following information:
-------------------------------------------------------------------------------------------
    -- State in abbreivation. e.g. MI, TX, OH...
    -- Filtering condition
    -- number of search result you wish (The final results may be less than you expected)
    -- Order of the search result
-------------------------------------------------------------------------------------------

    You would be able to see the following information:

-------------------------------------------------------------------------------------------
    -- The search results in text format
    -- The search results in figure format(bar chart, radar chart)
-------------------------------------------------------------------------------------------
    Also, you can type "exit" to quit anytime
'''

print(instruction)


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

def interactive_promt():
    ''' the active interface between user and the program
    Parameters
    ----------
    none 
    Returns
    -------
    none
    '''
    print(instruction)
    while True: 
        decision = input("what kind of search do you want? Search on Yelp = 1, Search on database = 2, or exit ")
        if decision == "1":
            print(instructionforone)
            time.sleep(1)

            query_name = input("please input the food/restaurant")
            query_name = query_name.lower().strip(" ")
            query_location = input("please input the location")
            query_location = query_location.lower().strip(" ")
            if query_name == 'exit' or query_location == 'exit':
                print("Goodbye! Thank you!")
                exit()
            else:
                query_string = query_name + query_location
                result = path_decision(query_name, query_location)
                array_output(result)
                time.sleep(0.5)
                yt_search(query_name, query_location, query_string)
                time.sleep(0.5)
                show_related_loc(query_name,query_location,query_string)
                time.sleep(0.5)
                go_direction(query_name, query_location,query_string)
                time.sleep(0.5)

        elif decision =='2':
            print(instructionfortwo)
            time.sleep(1)

            query_word = sql_query_for_historical_data()
            sql_result = sql_execute(query_word)
            array_output(result)
            time.sleep(0.5)
            draw_barplot(result)
            time.sleep(0.5)
            draw_radarplot(result)
            time.sleep(0.5)

        elif decision =='exit':
            print("Thank you! Hope you find your desire restaruant! Goodbye!")
            exit()
        else:
            print("Invalid Input! Please try again")
            time.sleep(0.5)
        

if __name__== "__main__":
    interactive_prompt()