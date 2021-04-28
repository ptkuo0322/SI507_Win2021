import json
import requests
from googleapiclient.discovery import build
import webbrowser 

#API keys
api_key = 'AIzaSyDi9NtuLf43xi37SiMjPF6BwCgQtHVrY3o'

# Setting for youtube API
youtube = build('youtube', 'v3', developerKey=api_key)

# maxResult= 0~ 50 default 5 maxResults="2"
request = youtube.search().list(part='snippet',q="Zingerman's Delicatessen")
response = request.execute()
#print(response)
#print(request)

print(len(response))
#print(response['items'][4])
#print(response['items'][3])
link = ""
alist = []
for idx in range(len(response)-2):
    for ele in response['items'][idx]['snippet']['thumbnails']['default']['url']:
        link += ele
    alist.append(link.split('/')[-2])
print(alist)

#print(type(link))
#with open('youtube.json', 'w') as outfile:
#    json.dump(response, outfile)


# open new windows for related videos in youtube
rul2 = "https://www.youtube.com/watch?"
id = alist
for ele in id:
    webbrowser.open_new("{}v={}".format(rul2,ele))
