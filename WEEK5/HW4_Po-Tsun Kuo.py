#import the module first
import requests
import json
### for step 3
#import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib
#from matplotlib.patches import Polygon
#from matplotlib.collections import PatchCollection

#### step 1, get the json file first
response = requests.get("https://dsl.richmond.edu/panorama/redlining/static/downloads/geojson/MIDetroit1939.geojson")
#print(response.text)
json_str = response.text
json_list = json.loads(json_str) # turn the txt file into dictionary

### step 2 
thisDict = { 
    "Coordinates": [json_list["features"][ele]["geometry"]["coordinates"] for ele in range(len(json_list["features"]))], #add lists of coordinates from the json file for each district 
    "Holc_Grade": [json_list["features"][ele]["properties"]["holc_grade"] for ele in range(len(json_list["features"]))], # add the grades from the json file for each district 
    "Holc_Color": ['darkgreen' if json_list["features"][ele]["properties"]["holc_grade"] == "A"  else 'cornflowerblue' if json_list["features"][ele]["properties"]["holc_grade"] == "B" 
    else 'gold' if json_list["features"][ele]["properties"]["holc_grade"] == "C"  else 'maroon' 
    for ele in range(len(json_list["features"]))], #add the appropriate color for each district based on the instructions below 
    "name": [ele+1 for ele in range(len(json_list["features"]))] # the name of the district is up to you, you might use a number or other iterator 
}
#print(thisDict)

#### step 3
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
        
        plt.fill(xs,ys, facecolor='darkgreen', edgecolor='black')
        #plt.fill_between('b')
    elif colors == "cornflowerblue":
        plt.fill(xs,ys, facecolor='cornflowerblue', edgecolor='black')
    elif colors == "gold":
        plt.fill(xs,ys, facecolor='gold', edgecolor='black')
    else:
        plt.fill(xs,ys, facecolor='maroon', edgecolor='black')
plt.rcParams["figure.figsize"] = (15,15) # adjust figure size
plt.show()

#### step 4

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

# create census_list = [] for thisDict, and create county_list and tempDict for filtering out the county code in step 5
census_list = []
county_list = []
tempDict = {}
# do the for loop for 238 times
for j in range(len(districts)): 

    # A series of possibly disconnected, possibly closed, line and curve segments.
    # based one the thisDict['Coordinates'] I pass in, it would generate all the possible line and cure segements to form a possible area 
    p = Path(thisDict['Coordinates'][j][0][0]) 
    
    # contains_point(self, point, transform=None, radius=0.0), Return whether the (closed) path contains the given point.
    # it would check wether points is inside the grid
    grid = p.contains_points(points) 
    
    # numpy.where(condition[, x, y]):Return elements chosen from x or y depending on condition.
    # random.choice(): Return a randomly selected element from the specified sequence
    # print out the points which is randomly selected by the grid
    print(j," : ", points[random.choice(np.where(grid)[0])] )

    # assign the points randomly selected by the grid. it will contain the coordinate information for query
    cordinate = points[random.choice(np.where(grid)[0])]

    # do the request here, to get the census tract
    base_url = "https://geo.fcc.gov/api/census/area"

    # query params, and get the arguments based oe the cordinate[0] for lon, and  cordinate[1] for lat
    params = {"lat":cordinate[1], "lon":cordinate[0]}

    # get the response from the request.get
    response = requests.get(base_url, params=params)

    # turn the txt file into dictionary
    json_form = json.loads(response.text) 
    #print(json_form["results"][0]["block_fips"][5:11] >> just for check the output

    # appending the parsed result to the census_list for the thisDict["Census Tract"]
    census_list.append(json_form["results"][0]["block_fips"][5:11])
    

    # appending the parsed result to the county_list for the tempDict["Census Tract"]. it contains the county code for latter use
    county_list.append(json_form["results"][0]["block_fips"][2:11])

# Assign new Key:value pairs to thisDict(get the Census Tract information )
thisDict["Census Tract"] = census_list

# Assign new Key:value pairs to tempDict (get the county code for further filtering condition)
tempDict["Census Tract"] = county_list
#print(thisDict["Census Tract"])


### step5

# for step 5E, comment out this part of code
#base_url = "https://api.census.gov/data/2015/acs/acs5?get=NAME,B19013_001E&for=tract:*&in=state:26&key=..."
#response = requests.get(base_url)
#json_list = json.loads(response.text)

#median_income_for_review_list = [[json_list[x][1],json_list[x][-1],json_list[x][-2]] for x in range(len(json_list)) ]

#same_census_track_list = []
#for ele in tempDict["Census Tract"]:
#    diff_county = []
#    for eles in median_income_for_review_list:  
#        if ele[3:] == eles[1]  and ele[:3]== eles[2]:
#            diff_county.append(eles[0])
#    same_census_track_list.append(diff_county)

#thisDict["median_income"] = same_census_track_list

#with open("HW4_dict.json", "w") as fout:
#    json.dump(thisDict, fout)


# for step 5E, load the local json file
with open("HW4_dict.json", "r") as fin:
    thisDict = json.load(fin)


###step 6


def mean_income(grade_category):
    Total_income =0
    num_of_grade=0
    total_num_of_income_data=0
    for grade in thisDict["Holc_Grade"]:
        
        if grade == grade_category:
            income = thisDict["median_income"][num_of_grade]
            for j in income:
                if int(j) > 0:
                    Total_income +=int(j)
                    total_num_of_income_data+=1
        num_of_grade+=1
    mean_income = Total_income/total_num_of_income_data
    return mean_income

def median_income(grade_category):
    list_income = []
    num_of_grade = 0
    total_num_of_income_data = 0
    for grade in thisDict["Holc_Grade"]:
            if grade == grade_category:
                income = thisDict["median_income"][num_of_grade]
                for j in income:
                    if int(j) > 0:
                        list_income.append(int(j))
                        total_num_of_income_data+=1
            num_of_grade +=1
    list_income.sort()
    if total_num_of_income_data % 2 == 0:
        medain_income = 0.5*(float(list_income[total_num_of_income_data//2]) + float(list_income[(total_num_of_income_data//2)-1]))
    else:
        medain_income = list_income[total_num_of_income_data//2]
    return medain_income


A_mean_income = mean_income("A")
B_mean_income = mean_income("B")
C_mean_income = mean_income("C")
D_mean_income = mean_income("D")

A_median_income = median_income("A")
B_median_income = median_income("B")
C_median_income = median_income("C")
D_median_income = median_income("D")


print("A_mean_income is "+A_mean_income)
print("A_median_income is "+A_median_income)
print("B_mean_income is "+B_mean_income)
print("B_median_income is "+B_median_income)
print("C_mean_income is "+C_mean_income)
print("C_median_income is "+C_median_income)
print("D_mean_income is "+D_mean_income)
print("D_median_income is "+D_median_income)




### bonus 1
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.path import Path
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon, PathPatch
import matplotlib


fig, ax = plt.subplots()

income_list = []
income_list2 = []
for x in thisDict["median_income"]:
    for y in x:
        income_list.append(int(y))

for x in income_list:
    if x > 0:
        income_list2.append(x)
max_incomes = max(income_list2)
min_incomes = min(income_list2)


patches = []
for i in range(len(thisDict["Coordinates"])):
    edgcolor = thisDict["Holc_Color"][i]
    if income_list[i] <0:
        polygon = Polygon(coord_list[i][0][0], True,facecolor="black", edgecolor = edgcolor)
        patches.append(polygon)
    else: 
        intensity = (income_list[i]-min_incomes)/(max_incomes-min_incomes)
        polygon = Polygon(coord_list[i][0][0], True, facecolor=plt.get_cmap('red')(intensity) edgecolor = edgcolor)
        patches.append(polygon)

ax.add_collection(p)
ax.autoscale()
plt.show()





### bouns 2
'''
Question: How can these HW assignments be improved?

Ans: 
I think overall, it is a really great work since one of the most attractive feature of Python is that there are so many useful module for us to utilize.
The lecture time is limited, it is not able to cover all the materials that are critical/helpful for us. I think HW3/HW4 are really good practice for us 
to learn on the Internet. Not only can we learn how to read the documentation by ourselve, but also increase the learning depth. And now, after the practice,
I am more familar with the matplotlib/numpy module. This could help us to generate the figure/plots/graphic presentation in the Python. (I did the graphic presentation
in MATLAB most). This helps me can directly interact with the internet and get the information and graphicize the information within one programming language.
It is much more time-saving.

However, I think the instructions in the HW3/HW4 are not clear enough. There are so many ambiguities there, so we may spend too much time understanding the problem,
rather than focusing on how to implementing the code to solve the problems. In addition, for HW4, many of us cannot pass through the test file owing to rounding problem
or other reasons. These situations would cost students spend unecessary time debugging. This should be improved if the HW will be used in the future.