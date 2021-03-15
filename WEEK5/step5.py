import requests
import json

base_url = "https://api.census.gov/data/2015/acs/acs5?get=NAME,B19013_001E&for=tract:*&in=state:26&key=1389aed2f7814f0cc180c4f08d39a228d892e62d"
response = requests.get(base_url)
json_list = json.loads(response.text)
print(json_list)


median_income_for_review_list = [[json_list[x][1],json_list[x][-1]] for x in range(len(json_list)) ]
#print(Alist)

'''
same_census_track_list = []
for ele in thisDict["Census Tract"]:
    diff_county = []
    for eles in median_income_for_review_list:  
        if ele == eles[1]:
            diff_county.append(eles[0])
    same_census_track_list.append(diff_county)

thisDict["median_income"] = same_census_track_list
'''