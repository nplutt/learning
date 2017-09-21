var http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  response.end('Hello World!');
}).listen(8000);

console.log('Server running at localhost:8000/');
