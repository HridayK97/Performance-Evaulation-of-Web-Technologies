var http = require('http')

function fib (n) {
  if (n < 2) {
    return 1;
  } else {
    return fib(n - 2) + fib(n - 1);
  }
}

var server = http.createServer(function(req, res) {
    data=fib(10);
    res.writeHead(200);
    res.end(data + "\n");
  
});
server.listen(8080);
console.log("server online at http://localhost:8080/")