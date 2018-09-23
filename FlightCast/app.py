import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import json

from flask import Flask, render_template, redirect, jsonify
from FlightMap import flightmapdata
from FlightSearch import flightsearchdata

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/flightsearch")
def flightsearch():

    flightdata = flightsearchdata('CLT','ATL','09/19/2018')

    return render_template("flightsearch.html", flightdata=flightdata)



@app.route("/flightmap/<flightid>")
def flightmap(flightid):

    #flightid = "AAL745-1534829157-airline-0092"

    #flightid = "AAL846-1537334758-airline-0217"

    waypoints = flightmapdata(flightid)

    return render_template("flightmap.html", waypointsdata=waypoints)



@app.route("/airportdata")
def airportdata():

    engine = create_engine("sqlite:///airports.db")
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Airports = Base.classes.airports
    session = Session(engine)

    airportlist = session.query(Airports).filter(Airports.ICAO.like('K%')).filter(Airports.Name.like('%international%')).order_by(Airports.Name).all()

    def row2dict(row):
        d = {}
        for column in row.__table__.columns:
            
            if str(column.type) == "TEXT":
                d[column.name] = str(getattr(row, column.name)).replace("'","").replace("\\N","")
            else:
                d[column.name] = getattr(row, column.name)

        return d

    data = []

    for airport in airportlist:
        data.append(row2dict(airport))
    
    airportdata = json.dumps(data)

    return render_template("airportdata.html", airportdata=data)


@app.route("/aboutus")
def aboutus():

    return render_template("aboutus.html")

    

if __name__ == "__main__":
    app.run(debug=True)