
# coding: utf-8

# In[1]:


import requests
import json
import pandas as pd
import time
from config import username, api_key


# In[5]:


def flightmapdata(flightID):

    baseurl = f"http://{username}:{api_key}@flightxml.flightaware.com/json/FlightXML2/"

    addurl = f"DecodeFlightRoute?faFlightID={flightID}"

    fxmlurl = baseurl + addurl
    
    response = requests.get(fxmlurl).json()
    
    return response['DecodeFlightRouteResult']['data']


# In[7]:


#response = requests.get(fxmlurl).json()
#print(response)
#print(json.dumps(response, indent=4, sort_keys=True))

