import requests
import json
'''
# step 1, get the json file first
response = requests.get("https://dsl.richmond.edu/panorama/redlining/static/downloads/geojson/MIDetroit1939.geojson")
#print(response.text)
json_str = response.text
json_list = json.loads(json_str) # turn the txt file into dictionary
#print(json_list["features"][1]["properties"]["holc_grade"])
'''
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
thisDict = {}

import random as random # to import random module and named as random
random.seed(33) # initialize the random number generator and the generator needs a seed value to start with 
from matplotlib.path import Path # to import Path function from matplotlib.path module
import numpy as np # to import numpy module and named as np

# numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None), it would return evenly spaced values within a given interval
# the given interval begarin with the first argument[start] and end with second argument[stop] and spaced with the third argument[step]
# xgrid would get evenly spaced (space range:0.004) values within a given interval (-83.5, -82.8)
xgrid = np.arange(-83.5,-82.8,.004) 

# numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None), it would return evenly spaced values within a given interval
# the given interval begarin with the first argument[start] and end with second argument[stop] and spaced with the third argument[step]
# ygrid would get evenly spaced (space range:0.004) values within a given interval (42.1, 42.6)
ygrid = np.arange(42.1, 42.6, .004) 

# numpy.meshgrid(*xi, copy=True, sparse=False, indexing='xy'), it will return coordinate matrics from coordinate vector
# it would create a rectangular grid out of an array of x values and an array of y values.
xmesh, ymesh = np.meshgrid(xgrid,ygrid) 

# numpy.vstack(tup): Stack arrays in vertically sequence (row wise)
# char.chararray.flatten(order='C'): Return a copy of the array collapsed into one dimension.
# chararray.T: Return a transposed array
points = np.vstack((xmesh.flatten(),ymesh.flatten())).T 

# do the for loop for 238 times
census_list = []

for j in range(len(districts)): 
    #
    p = Path(thisDict['Coordinates'][j][0][0]) 
    
    # contains_point(self, point, transform=None, radius=0.0), Return whether the (closed) path contains the given point.
    grid = p.contains_points(points) 
    
    # numpy.where(condition[, x, y]):Return elements chosen from x or y depending on condition.
    # random.choice(): Return a randomly selected element from the specified sequence
    
    #print(j," : ", points[random.choice(np.where(grid)[0])] )

    cordinate = points[random.choice(np.where(grid)[0])]
    base_url = "https://geo.fcc.gov/api/census/area"
    params = {"lat":cordinate[1], "lon":cordinate[0]}
    response = requests.get(base_url, params=params)
    json_form = json.loads(response.text) # turn the txt file into dictionary
    #print(json_form["results"][0]["block_fips"][5:11])
    census_list.append(json_form["results"][0]["block_fips"][5:11])
thisDict["Census Tract"] = census_list
#print(thisDict["Census Tract"])

'''
#237  :  [-83.204  42.352]
base_url = "https://api.census.gov/data/2015/acs/acs5?get=NAME,B19013_001E&for=tract:*&in=state:26&key=1389aed2f7814f0cc180c4f08d39a228d892e62d"
#"https://api.census.gov/data/2015/acs/acs5?get=NAME,B00001_001E&for=tract:*&in=state:01&key=1389aed2f7814f0cc180c4f08d39a228d892e62d" 
response = requests.get(base_url)
json_list = json.loads(response.text)
print(json_list)
'''
