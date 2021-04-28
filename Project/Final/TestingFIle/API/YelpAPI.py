
# Import the modules
import requests
import json

# Define my API Key, My Endpoint, and My Header
API_KEY = 'c2GgFaTUbluwOQFNZjLY35_G8KdzPdZfxi64b2Hwz7ADbQUsR_BDBL48WYm6QCLp9MkswmS79HAazAUOJzUKS7u6S6bAfQosjFpjNG58jHZkohXL1Mq8GmsorCtlYHYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

# Define my parameters of the search
# BUSINESS SEARCH PARAMETERS - EXAMPLE

PARAMETERS = {'term': 'pizza',
            'radius': 10000,
            'location': 'Ann Arbor'}

# Request to the Yelp API
response = requests.get(url = ENDPOINT,
                        params = PARAMETERS,
                        headers = HEADERS)

# Conver the JSON String
business_data = response.json()

# print the response
print(response)
print(json.dumps(business_data, indent = 3))

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)