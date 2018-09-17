from flask import Flask, render_template, redirect
from FlightMap import flightmapdata

app = Flask(__name__)

@app.route("/")
def home():

    #locations = {"startLat":7.8731, "startLon":80.7718, "endLat":-18.7669, "endLon":46.8691 }

    return render_template("index.html")






    #return redirect("/", code=302)

@app.route("/flightmap")
def flightmap():

    waypoints = flightmapdata("AAL745-1534829157-airline-0092")

    return render_template("flightmap.html", waypointsdata=waypoints)

#AAL745-1534829157-airline-0092



if __name__ == "__main__":
    app.run(debug=True)