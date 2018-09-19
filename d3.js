var airports= []

d3.select("body")
  .selectAll("option")
  .data(airports)
  .enter()
  .append("select")
  .html(function(d) {
    return `<option${d.city}</option><option${d.city}</option>`;
