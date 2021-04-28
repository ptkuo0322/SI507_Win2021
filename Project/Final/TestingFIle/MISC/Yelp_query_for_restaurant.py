# Import the modules
import requests
import json
import pandas as pd
import csv 
import sqlite3
from pandas import DataFrame

# Define my API Key, My Endpoint, and My Header
API_KEY = 'c2GgFaTUbluwOQFNZjLY35_G8KdzPdZfxi64b2Hwz7ADbQUsR_BDBL48WYm6QCLp9MkswmS79HAazAUOJzUKS7u6S6bAfQosjFpjNG58jHZkohXL1Mq8GmsorCtlYHYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search/phone'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

# Define my parameters of the search
# BUSINESS SEARCH PARAMETERS - EXAMPLE

query_string1 = input("please input the phone number (include country code)")


PARAMETERS = {'term': query_string1}

# Request to the Yelp API
response = requests.get(url = ENDPOINT,
                        params = PARAMETERS,
                        headers = HEADERS)


# Conver the JSON String
business_data = response.json()

print(business_data)