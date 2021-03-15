import requests
import json
import webbrowser
#########################################
##### Name: Po-Tsun Kuo             #####
##### Uniqname:  ptkuo@umich.edu    #####
#########################################

class Media:

    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", json=None): 
        self.json = json
        if json == None:
            self.title = title
            self.author = author
            self.release_year = release_year
            self.url = url
        else:
            self.title = json["collectionName"]
            self.author = json["artistName"]
            self.release_year = json["releaseDate"][0:4]
            self.url = json["collectionViewUrl"]

    def info(self):
            return f"{self.title} by {self.author} ({self.release_year})"
    
    def length(self):
        return 0



# Other classes, functions, etc. should go here
class Song(Media):

    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", album="No Album", genre="No Genre", track_length=0, json=None):
        self.json = json
        if json == None:
            super().__init__(title, author, release_year, url)
            self.album = album
            self.genre = genre
            self.track_length = track_length
        else:
            self.title = json["trackName"]
            self.author = json["artistName"]
            self.release_year = json["releaseDate"][0:4]
            self.url = json["trackViewUrl"]
            self.album = json["collectionName"]
            self.genre = json["primaryGenreName"]
            self.track_length = json["trackTimeMillis"]
            
    def info(self):
        return f"{self.title} by {self.author} ({self.release_year}) [{self.genre}]"

    def length(self):
        return round((float(self.track_length)/1000))



class Movie(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", rating="No Rating", movie_length=0, json=None):
        self.json = json
        if json == None:
            super().__init__(title, author, release_year, url)
            self.rating = rating
            self.movie_length = movie_length
        else:
            self.title = json["trackName"]
            self.author = json["artistName"]
            self.release_year = json["releaseDate"][0:4]
            self.url = json["trackViewUrl"]
            self.rating = json["contentAdvisoryRating"]
            self.movie_length = json["trackTimeMillis"]

    def info(self):
        return f"{self.title} by {self.author} ({self.release_year}) [{self.rating}]"

    def length(self):
        return round((float(self.movie_length)/60000))


######## for part3 ##########
search_limit = 50


def FetchInfo(usr_input):
    if usr_input == "exit":
        quit()
    else:
        baseurl = "https://itunes.apple.com/search"
        params = {"term":usr_input, "limit":search_limit}
        response = requests.get(baseurl, params=params)
        json_list= []
        json_list.append(json.loads(response.text))
        return json_list

def SongGroups(SongList, x=0):
    print("SONG")
    x = 0
    for i in range(len(SongList)):
        data = Songtitle="No Title", author="No Author", release_year="No Release Year", url="No URL", album="No Album", genre="No Genre", track_length=0, json=None SongList[i])
        print(i+1, data.info())
        
def MovieGroups(MovList, x):
    print("MOVIE")
    for i in range(len(MovList)):
        data = Song(title="No Title", author="No Author", release_year="No Release Year", url="No URL", rating="No Rating", movie_length=0, json=MovList[i])
        print(x+i+1, data.info())

def OtherMediaGroups(Otherlist, x):
    print("OTHER MEDIA")
    for i in range(len(Otherlist)):
        data = Media("title", "author", "release_year", "url", Otherlist[i])
        print(x+i+1, data.info())
        
def CategorizeGroups(Catlist):
    Song_list = []
    Movie_list = []
    Other_list = []
    total_list = []
    i = 0

    for i in range(Catlist[0]["resultCount"]):
        try:
            #print(alist[0]["results"][i]["kind"])
            if Catlist[0]["results"][i]["kind"] == "song":
                Song_list.append(Catlist[0]["results"][i])
            elif "movie" in Catlist[0]["results"][i]["kind"]:
                Movie_list.append(Catlist[0]["results"][i])
            else:
                Other_list.append(Catlist[0]["results"][i])
        except KeyError:
            Other_list.append(Catlist[0]["results"][i])
    
    return SongGroups(Song_list, 0), MovieGroups(Movie_list, len(Song_list)), OtherMediaGroups(Other_list, len(Song_list)+len(Movie_list))

def CategorizeGroupsUrl(Catlist):
    Song_list = []
    Movie_list = []
    Other_list = []
    total_list = []

    for i in range(Catlist[0]["resultCount"]):
        try:
            #print(alist[0]["results"][i]["kind"])
            if Catlist[0]["results"][i]["kind"] == "song":
                Song_list.append(Catlist[0]["results"][i])
            elif "movie" in Catlist[0]["results"][i]["kind"]:
                Movie_list.append(Catlist[0]["results"][i])
            else:
                Other_list.append(Catlist[0]["results"][i])
        except KeyError:
            Other_list.append(Catlist[0]["results"][i])
    total_list = Song_list + Movie_list + Other_list
    return total_list

def ShowUrl(Alist, idx):
    target = Alist[idx]
    try:
        if target['kind'] == "song":
            url = Song("title", "author", "release_year", "url", "album", "genre", "track_length", target).url
        elif "movie" in target["kind"]:
            url = Movie("title", "author", "release_year", "url", "rating", "movie_length", target).url
        else:
            url = Media("title", "author", "release_year", "url", target).url
    except KeyError:
        url = Media("title", "author", "release_year", "url", target).url
    print(f"Launching{url} in web browser")
    return webbrowser.open_new(f"{url}")


if __name__ == "__main__":
    

    # your control code for Part 4 (interactive search) should go here
    
    usr_input = input('Enter a search term, or "exit" to quit: ') # justin
    a = FetchInfo(usr_input)
    CategorizeGroups(a) # show justin
    while True:
        usr_input = input('Enter a number for more info, or another search term, or "exit": ') #beatles #6
        if usr_input == "exit":
            print("bye! ")
            quit()
        elif usr_input.isnumeric() and int(usr_input) in range(search_limit):
            index_number = int(usr_input)-1
            ShowUrl(CategorizeGroupsUrl(a), index_number)
            break
        else:
            a = FetchInfo(usr_input)
            CategorizeGroups(a) #show beatles
            