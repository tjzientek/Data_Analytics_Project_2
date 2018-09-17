import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, render_template, redirect
from FlightMap import flightmapdata

app = Flask(__name__)

@app.route("/")
def home():

    #locations = {"startLat":7.8731, "startLon":80.7718, "endLat":-18.7669, "endLon":46.8691 }

    return render_template("index.html")




@app.route("/flightsearch")
def flightsearch():

    return render_template("flightsearch.html")



@app.route("/flightmap")
def flightmap():

    waypoints = flightmapdata("AAL745-1534829157-airline-0092")

    return render_template("flightmap.html", waypointsdata=waypoints)

#AAL745-1534829157-airline-0092

@app.route("/airportdata")
def airportdata():

    engine = create_engine("sqlite:///airports.db")
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Airports = Base.classes.airports
    session = Session(engine)

    


    return render_template("airportdata.html")



if __name__ == "__main__":
    app.run(debug=True)