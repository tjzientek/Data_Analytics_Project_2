import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import json

from flask import Flask, render_template, redirect, jsonify
from FlightMap import flightmapdata
from FlightSearch import flightsearchdata
from AirportData import *

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/flightsearch")
def flightsearch():

    flightdata = flightsearchdata('KCLT','KATL','09/19/2018')

    #airportdata1 = getairportdata2()

    return render_template("flightsearch.html", flightdata=flightdata)



@app.route("/flightmap/<flightid>")
def flightmap(flightid):

    waypoints = flightmapdata(flightid)

    return render_template("flightmap.html", waypointsdata=waypoints)



@app.route("/airportdata")
def airportdata():

    data = getairportdata()
    
    #airportdata = json.dumps(data)

    return render_template("airportdata.html", airportdata=data)


@app.route("/aboutus")
def aboutus():

    return render_template("aboutus.html")



if __name__ == "__main__":
    app.run(debug=True)