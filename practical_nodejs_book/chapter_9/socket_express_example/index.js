const http = require('http');
const express = require('express');
const path = require('path');
const logger = require('morgan');
const bodyParser = require('body-parser');

const routes = require('./routes/index.js');
const app = express();

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', routes);

const server = http.createServer(app);
const io = require('io').listen(server);

io.sockets.on('connection', (socket) => {
  socket.on('messageChange', (data) => {
    console.info(data);
    socket.emit('receive',
      data.message.split('').reverse().join('')
    );
  });
});

// Websockets can use ports 80 for http and 443 for https

app.set('port', 3000);
server.listen(app.get('port'), () => {
  console.log('Express server listening on port: ', app.get('port'));
});

