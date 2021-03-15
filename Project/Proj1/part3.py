import json
import requests




Alist = []


######## for part3 ##########
usr_input = input('Enter a search term, or "exit" to quit: ')
baseurl = "https://itunes.apple.com/search"
params = {"term":usr_input}
response = requests.get(baseurl, params=params)
json_form = json.loads(response.text) 
alist= []
alist.append(json_form)
#print(alist[0]["results"]) #search results number of that 
Blist = []
Clist = []
Dlist = []
i = 0
for i in range(alist[0]["resultCount"]):
    try:
        #print(alist[0]["results"][i]["kind"])
        if alist[0]["results"][i]["kind"] == "song":
            Blist.append(alist[0]["results"][i])
        elif alist[0]["results"][i]["kind"] == "feature-moive":
            Clist.append(alist[0]["results"][i])
        else:
            Dlist.append(alist[0]["results"][i])
    except KeyError:
        Dlist.append(alist[0]["results"][i])
print(len(Blist))
print(len(Clist))
print(len(Dlist))

with open("part31.json", "w") as fout:
    json.dump(Blist, fout)



class Media:

    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", json=None): 
        self.json = json
        if json == None:
            self.title = title
            self.author = author
            self.release_year = release_year
            self.url = url
        else:
            self.title = json["trackName"]
            self.author = json["artistName"]
            self.release_year = json["releaseDate"][0:4]
            self.url = json["collectionViewUrl"]

    def info(self):
            return f"{self.title} by {self.author} ({self.release_year})"
    
    def length(self):
        return 0
for i in range(len(Blist)):
    data = Media(1,2,3,4,Blist[i])
    print(i+1, data.info())



#print(json_form)


#for i in range(len(thisdict)):
#    try:
#        if thisdict[i]['kind'] == "feature-movie":
#            Alist.append("movie")
#        elif thisdict[i]['kind'] == "song":
#            Alist.append("song")
#    except KeyError:
#        Alist.append("FFFFF")
#print(Alist)
