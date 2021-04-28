##--------------------------want
query_name = input("please input the food/restaurant")
query_name = query_name.lower().strip(" ")
#time.sleep(1)
query_location = input("please input the location")
query_location = query_location.lower().strip(" ")
query_string = query_name + query_location
#time.sleep(1)

path_decision(query_name, query_location) # search the yelp and update the sql and ger the list
#yt_search(query_string) # search the video on YOutube
#result = show_related_loc(query_name,query_location) # generate the linklist for open_static_map
#go_direction(query_name, query_location,query_string) # choose one of the option and direct to it

#r = sql_query() # output the query string for sql database
#print(r)
#r1 = sql_execute(r) # launch the search sql and return list in list [[] []]
#print(r1)
#r2 = array_output(r1) # print in the desire format

#r3 = scale_convert(r1)
#draw_radarplot(r1) #draw the radar plot
#draw_barplot(r1) # draw the barplot
 
##--------------------------want


## problem 

#dict_result = path_decision(query_name, query_location)
#loc_list = show_related_loc(query_name, query_location)
#go_direction(query_name, query_location, query_string)



