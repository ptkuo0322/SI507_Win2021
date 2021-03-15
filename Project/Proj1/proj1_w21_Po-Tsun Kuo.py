import requests
import json
### need to improt webbrowser module for launching the url link 
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
        else:   #### use try/except to deal with the situation that KeyError happens when we provide json argument
                #### maybe there are more simpler way to do this
            try:
                self.title = json["collectionName"]
            except KeyError:
                self.title = title
            try:    
                self.author = json["artistName"]
            except KeyError:
                self.author = author
            try:    
                self.release_year = json["releaseDate"][0:4]
            except KeyError:
                self.release_year = release_year
            try:    
                self.url = json["collectionViewUrl"]
            except KeyError:
                self.url = url   

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
                #### use try/except to deal with the situation that KeyError happens when we provide json argument
                #### maybe there are more simpler way to do this
            try:
                self.title = json["trackName"]
            except KeyError:
                self.title = title
            try:
                self.author = json["artistName"]
            except KeyError:
                self.author = author
            try:
                self.release_year = json["releaseDate"][0:4]
            except KeyError:
                self.release_year = release_year
            try:
                self.url = json["trackViewUrl"]
            except KeyError:
                self.url = url
            try:
                self.album = json["collectionName"]
            except KeyError:
                self.album = album
            try:
                self.genre = json["primaryGenreName"]
            except KeyError:
                self.genre = genre
            try:
                self.track_length = json["trackTimeMillis"]         
            except KeyError:
                self.track_length = track_length

    def info(self):
        return f"{super().info()} [{self.genre}]"

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
                #### use try/except to deal with the situation that KeyError happens when we provide json argument
                #### maybe there are more simpler way to do this
            try:
                self.title = json["trackName"]
            except KeyError:
                self.title = title
            try:
                self.author = json["artistName"]
            except KeyError:
                self.author = author
            try:
                self.release_year = json["releaseDate"][0:4]
            except KeyError:
                self.release_year = release_year
            try:
                self.url = json["trackViewUrl"]
            except KeyError:
                self.url = url
            try:
                self.rating = json["contentAdvisoryRating"]
            except KeyError:
                self.rating = rating
            try:
                self.movie_length = json["trackTimeMillis"]         
            except KeyError:
                self.movie_length = movie_length
    def info(self):
        return f"{super().info()} [{self.rating}]"

    def length(self):
        return round((float(self.movie_length)/60000))




######## for part3 and part4 ##########

#### we can define the search limit between 1 ~ 200
search_limit = 50

def FetchInfo(usr_input):
    ''' Constructs the query string and executes requests to retrieve data based on requirements
    
    Parameters
    ----------
    String
        the query keywords that people want to search
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''

    if usr_input == "exit":
        print("bye!")
        quit()
    else:
        baseurl = "https://itunes.apple.com/search"
        params = {"term":usr_input, "limit":search_limit}
        response = requests.get(baseurl, params=params)
        json_list= []
        json_list.append(json.loads(response.text))
        return json_list

#### CategorizeGroups function would parse the list obtained by our query and categorize them into three group: song, movie, other_media
def CategorizeGroups(Catlist):
    ''' Parse the input data list obtained by our query [FetchInfo function] and 
    categorize the element of the that list into three group of lists: Song_list, Movie_list, Other_list

    Parameters
    ----------
    list
        A list that be passed through to parse it into three group of list depended on its kind
    
    Returns
    -------
    string
        the desired information in the specific form and begin with the index number, starting at 1, line by line
    '''

    Song_list = []
    Movie_list = []
    Other_list = []
    i = 0

    for i in range(Catlist[0]["resultCount"]):
        try:
            if Catlist[0]["results"][i]["kind"] == "song":
                Song_list.append(Catlist[0]["results"][i])
            elif "movie" in Catlist[0]["results"][i]["kind"]:
                Movie_list.append(Catlist[0]["results"][i])
            else:
                Other_list.append(Catlist[0]["results"][i])
        except KeyError: 
            #### try/eccept here is to deal with the info that do not have the key :Catlist[0]["results"][i]
            Other_list.append(Catlist[0]["results"][i])
    
    return SongGroups(Song_list, 0), MovieGroups(Movie_list, len(Song_list)), OtherMediaGroups(Other_list, len(Song_list)+len(Movie_list))


#### SongGroups function would print out the song group data in the specific form preceded by a number, starting at 1
def SongGroups(SongList, x=0):
    ''' Print out the data of song group line by line, formatted in the specific form preceded by a number, starting at 1
    
    Parameters
    ----------
    list
        the list that be passed through the Song class to get the desire formatted information

    integer
        the interger to indicate the starting number of the the data in song group, it is default as 0
    
    Returns
    -------
    None
    
    '''
    SongUrl = []
    print("SONGS")
    x = 0
    for i in range(len(SongList)):
        data = Song(json=SongList[i])
        print(i+1, data.info())
    return None

#### MovieGroups function would print out the movie group data in the specific form preceded by a number, after the SongGroup
def MovieGroups(MovList, x):
    ''' Print out the data of movie group line by line, formatted in the specific form preceded by a number, right after the Song group
    
    Parameters
    ----------
    list
        the list that be passed through the Movie class to get the desire formatted information

    integer
        the interger to indicate the starting number of the the data in movie group

    Returns
    -------
    None
    
    '''
    print("MOVIES")
    for i in range(len(MovList)):
        data = Movie(json=MovList[i]) 
        print(x+i+1, data.info())
    return None

#### OtherMediaGroups function would print out the other_media group data in the specific form preceded by a number, after the MovieGroup
def OtherMediaGroups(Otherlist, x):
    ''' Print out the data of other media group line by line, formatted in the specific form preceded by a number, right after the movie group
    
    Parameters
    ----------
    list
        the list that be passed through the Media class to get the desire formatted information

    integer
        the interger to indicate the starting number of the the data in media group


    Returns
    -------
    None
    
    '''
    print("OTHER MEDIA")
    for i in range(len(Otherlist)):
        data = Media(json=Otherlist[i])
        print(x+i+1, data.info())
    return None
        


#### CategorizeGroupsUrl function would generate the total list(combination of the Song_list, Movie_list, Other_list in order)
#### which contain the required URL link info
def CategorizeGroupsUrl(Catlist):
    ''' Construct the list that contains the Song_list, Movie_list, and Other_list. In the list, 
    it contains the reuqired URL link information, which would be used to direct people to the website
    
    Parameters
    ----------
    list
        the list for parsing to get Song_list, Movie_list, and Other_list


    
    Returns
    -------
    list
        a list of tuples that constain the desired URL link information
    '''
    Song_list = []
    Movie_list = []
    Other_list = []
    total_list = []

    for i in range(Catlist[0]["resultCount"]):
        try:
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

#### ShowUrl function would parese the list to get the URL link
#### if no URL link available, then, it would print out the message to inform the people
def ShowUrl(Alist, idx):
    ''' Parse the list with the index number to get the URL link
    if URL is link available, then, it would launch the URL link and direct people to the website
    if no URL link available, then, it would print out the message to inform the people
    
    Parameters
    ----------
    list
        the list for parsing to get the URL information

    integer
        the index of the list, help slice the exact URL element in the list


    Returns
    -------
    None
        if NO URL link is available

    function
        it would direct people to the website via their browser
    '''
    target = Alist[idx]
    try:
        if target['kind'] == "song":
            url = Song(json= target).url
        elif "movie" in target["kind"]:
            url = Movie(json=target).url
        else:
            url = Media(json=target).url
    except KeyError:
        #### try/eccept here is to deal with the info that do not have the key : target['kind']
        url = Media(json=target).url
    if url == "No URL":
        print("\nSorry!, No URL link can be provided this time!\n")
        return None
    else:
        print(f"Launching{url} in web browser")
        return webbrowser.open_new(f"{url}")


if __name__ == "__main__":

    # your control code for Part 4 (interactive search) should go here
    usr_input = input('Enter a search term, or "exit" to quit: ') 
    a = FetchInfo(usr_input)
    CategorizeGroups(a) 
    while True:
        usr_input = input('Enter a number for more info, or another search term, or "exit": ')
        if usr_input == "exit":
            print("bye! ")
            quit()
        elif usr_input.isnumeric() and int(usr_input) in range(search_limit+1):
            index_number = int(usr_input)-1
            ShowUrl(CategorizeGroupsUrl(a), index_number)
            break
        else:
            a = FetchInfo(usr_input)
            CategorizeGroups(a)