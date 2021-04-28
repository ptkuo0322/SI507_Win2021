# importing required modules
import requests
import webbrowser 

# Enter your api key here
API_KEY = "AIzaSyBaCdZ4_5GiifOCE4PXGhyno6AwpVsCE-U"


# This part is for Google Maps Static API
BASE_URL = "https://maps.googleapis.com/maps/api/staticmap?"

# parameters
ZOOM = 12
CITY = "AnnArbor"
work = "42.2988,-83.6910"

# updating the URL
URL = BASE_URL + "center=" + CITY + "&zoom=" + str(ZOOM) + "&size=2180x108000&key=" + API_KEY +"&maptype=roadmap" + "&markers=color:blue|label:S|42.2988,-83.6910" + "&markers=size:large|color:red|label:S|42.3084,-83.6893"
result = requests.get(URL)
print("This is for Google Maps Static API")
print(result)
print(URL)
print("This is for Google Maps Static API")

# This part is for Google Maps URLs 
# base url
url = "https://www.google.com/maps/search/?api=1"

# get response
r = url + "&query=" + work 
results = requests.get(r)
print("This is for Google Maps URLs")
print(results)
print(r)
print("This is for Google Maps URLs")
#webbrowser.open_new(r)

