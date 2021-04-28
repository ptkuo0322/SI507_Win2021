import json
import requests
from googleapiclient.discovery import build
import webbrowser 

#API keys
api_key = 'AIzaSyDi9NtuLf43xi37SiMjPF6BwCgQtHVrY3o'

# Setting for youtube API
youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.search().list(part='snippet',q="Mani Osteria & Bar", maxResults="2")
response = request.execute()
print(response)
print(request)


with open('youtube.json', 'w') as outfile:
    json.dump(response, outfile)


# open new windows for related videos in youtube
rul2 = "https://www.youtube.com/watch?"
id = ["--t80sSkwbA","AtaEDl8o1Jg"]
for ele in id:
    webbrowser.open_new("{}v={}".format(rul2,ele))
