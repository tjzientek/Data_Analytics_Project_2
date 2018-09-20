




d3.select("body")
  .selectAll("#origin")
  .data(airports)
  .enter()
  .append("select")
  .html(function(d) {
    return `<option${d.city}</option><option${d.city}</option>`;

d3.select("body")
    .selectAll("#destination")
    .data(airports)
    .enter()
    .append("select")
    .html(function(d) {
      return `<option${d.city}</option><option${d.city}</option>`;
  