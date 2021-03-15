#import the module first
import requests
import json
### for step 3
#import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib
#from matplotlib.patches import Polygon
#from matplotlib.collections import PatchCollection

# step 1, get the json file first
response = requests.get("https://dsl.richmond.edu/panorama/redlining/static/downloads/geojson/MIDetroit1939.geojson")
#print(response.text)
json_str = response.text
json_list = json.loads(json_str) # turn the txt file into dictionary

#cmaps = [('Sequential', ['binary', 'Blues', 'BuGn', 'BuPu', 'gist_yarg','GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd','PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu','Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd'])]


# step 2 
thisDict = { 
    "Coordinates": [json_list["features"][ele]["geometry"]["coordinates"] for ele in range(len(json_list["features"]))], #add lists of coordinates from the json file for each district 
    "Holc_Grade": [json_list["features"][ele]["properties"]["holc_grade"] for ele in range(len(json_list["features"]))], # add the grades from the json file for each district 
    "Holc_Color": ['darkgreen' if json_list["features"][ele]["properties"]["holc_grade"] == "A"  else 'cornflowerblue' if json_list["features"][ele]["properties"]["holc_grade"] == "B" 
    else 'gold' if json_list["features"][ele]["properties"]["holc_grade"] == "C"  else 'maroon' 
    for ele in range(len(json_list["features"]))], #add the appropriate color for each district based on the instructions below 
    "name": [ele+1 for ele in range(len(json_list["features"]))] # the name of the district is up to you, you might use a number or other iterator 
}
#print(thisDict)

# step 3
districts = [x for x in thisDict["Coordinates"]] 
#print(len(districts))
color = [x for x in thisDict["Holc_Color"]]
#print(len(color))

plt.figure() # draw plot in a figure
for i in range(len(districts)): # 238
    coord = districts[i][0][0] 
    colors = color[i]
    #print(coord)
    coord.append(coord[0]) # create close coordinate for poly
    xs, ys = zip(*coord) #create lists of x and y values 
    #print(xs, ys)
    if colors == "darkgreen":
        
        plt.contourf(xs,ys, cmaps='Rdgy', edgecolor='darkgreen')
        #plt.fill_between('b')
    elif colors == "cornflowerblue":
        plt.fill(xs,ys, facecolor='cornflowerblue', edgecolor='cornflowerblue')
    elif colors == "gold":
        plt.fill(xs,ys, facecolor='gold', edgecolor='gold')
    else:
        plt.fill(xs,ys, facecolor='maroon', edgecolor='maroon')
plt.rcParams["figure.figsize"] = (15,15) # adjust figure size
plt.show()
