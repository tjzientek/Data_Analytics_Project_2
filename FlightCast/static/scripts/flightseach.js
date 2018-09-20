d3.select("tbody")
    .selectAll("tr")
    .data(obj)
    .enter()
    .append("tr")
    .html(function(d) {
        var dep = new Date(`${d.filed_departuretime}` *1000).toLocaleString();
        var arr = new Date(`${d.estimatedarrivaltime}` *1000).toLocaleString();
        return `<td>${d.ident}</td><td>${d.aircrafttype}</td><td>${d.originCity}</td>
        <td>${d.destinationCity}</td>
        <td>${dep}</td>
        <td>${arr}</td>
        <td><a href="/flightmap/${d.faFlightID}">Map it</a></td>`;
 });