import requests
import json
import pandas as pd
import time
import ast
from config import username, api_key

def flightsearchdata(origin, destination, date):

    startDatetime = date + ' 00:00:00 +0000'
    endDatetime = date + ' 23:59:59 +0000'
    startEpoch = int(time.mktime(time.strptime(startDatetime, '%m/%d/%Y %H:%M:%S +0000')))
    endEpoch = int(time.mktime(time.strptime(endDatetime, '%m/%d/%Y %H:%M:%S +0000')))

    baseurl = f"http://{username}:{api_key}@flightxml.flightaware.com/json/FlightXML2/"

    addurl = f"AirlineFlightSchedules?startDate={startEpoch}&endDate={endEpoch}&origin={origin}&destination={destination}&howMany=100"

    fxmlurl = baseurl + addurl
    
    response = requests.get(fxmlurl).json()
    
    data = response["AirlineFlightSchedulesResult"]['data']
    df = pd.DataFrame.from_dict(data, orient='columns')

    idents = []
    for index, row in df.iterrows():
        if row['actual_ident'] == "":
            if [row['ident'],row['departuretime']] not in idents:
                idents.append([row['ident'],row['departuretime']])
        else:
            if [row['actual_ident'],row['departuretime']] not in idents:
                idents.append([row['actual_ident'],row['departuretime']])

    flights = []
    for ident in idents:
        addurl2 = f"FlightInfoEx?ident={ident[0]}@{ident[1]}&howMany=1&offset=0"
        fxmlurl2 = baseurl + addurl2
        idents_resp = json.dumps(requests.get(fxmlurl2).json())
        idents_resp = idents_resp.replace("[","").replace("]","")
        idents_resp2 = ast.literal_eval(idents_resp)
        flights.append(idents_resp2['FlightInfoExResult']['flights'])
        

    return flights