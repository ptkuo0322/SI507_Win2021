import json
import requests
from googleapiclient.discovery import build
import webbrowser 

#API keys
api_key = 'AIzaSyCtKEivfpctynsM0_AGoMW9kk-0VAKbxpo'

# Setting for youtube API
youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.search().list(part='snippet',q="pizza")
response = request.execute()
print(response)
print(request)
# open new windows for related videos in youtube
rul2 = "https://www.youtube.com/watch?"
id = ["29lVTotJ4XI","vnkAotfOhTw"]
for ele in id:
    webbrowser.open_new("{}v={}".format(rul2,ele))