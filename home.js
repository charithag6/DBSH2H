function requestCSV(f, c) {
  return new CSVAJAX(f, c);
}
function CSVAJAX(filepath, callback) {
  this.request = new XMLHttpRequest();
  this.request.timeout = 10000;
  this.request.open("GET", filepath, true);
  this.request.parent = this;
  this.callback = callback;
  this.request.onload = function () {
    var d = this.response.split("\n");
    var i = d.length;
    while (i--) {
      if (d[i] !== "") d[i] = d[i].split(",");
       else d.splice(i, 1);
    }
    this.parent.response = d;
    if (typeof this.parent.callback !== "undefined") this.parent.callback(d);
  };
  this.request.send();
}
var foo = requestCSV("countries_info.csv",callback());
console.log(foo);
