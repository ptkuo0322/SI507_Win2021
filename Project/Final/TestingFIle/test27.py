instruction = '''This program provide two ways to search for food/restaurant in the United state
choice 1: 
'''

while True: 
    while True:   
        query_name = input("please input the food/restaurant")
        query_name = query_name.lower().strip(" ")
        if query_name == 'exit':
            print("Goodbye! Thank you!")
            exit()
    #time.sleep(0.5)
        query_location = input("please input the location")
        query_location = query_location.lower().strip(" ")
        if query_location == 'exit':
            print("Goodbye! Thank you!")
            exit()
        elif query_location == "":
            print("location is required")
            break
        query_string = query_name + query_location
        #print(query_string)
        result = path_decision(query_name, query_location)
        yt_search(query_string)
        show_related_loc(query_name,query_location)
        go_direction(query_name, query_location,query_string)
    print("midpoint")
    while True:
        
        break
        if usr.isnumeric():
            print("AAAAAA")
            break
        else:
            print("invalid for section2")
    while True:
        usr = input("enter a number1")
        if usr.isnumeric():
            print("AAAAAA")
            break
        else:
            print("invalid for section3")
    print("end")
    break
    #time.sleep(0.5)

#path_decision(query_name, query_location) # search the yelp and update the sql and ger the list
#yt_search(query_string) # search the video on YOutube
#result = show_related_loc(query_name,query_location) # generate the linklist for open_static_map
#go_direction(query_name, query_location,query_string) # choose one of the option and direct to it
'''
r = sql_query() # output the query string for sql database
print(r)
r1 = sql_execute(r) # launch the search sql and return list in list [[] []]
print(r1)
r2 = array_output(r1) # print in the desire format
'''
#r3 = scale_convert(r1)
#draw_radarplot(r1) #draw the radar plot
#draw_barplot(r1) # draw the barplot

##==============used====================
#query_name = input("please input the food/restaurant")
#query_name = query_name.lower().strip(" ")
#time.sleep(1)
#query_location = input("please input the location")
#query_location = query_location.lower().strip(" ")
#query_string = query_name + query_location
#time.sleep(1)