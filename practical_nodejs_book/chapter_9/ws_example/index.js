const WebSocketServer = require('ws').Server;

const wss = new WebSocketServer({ port: 3000 });

wss.on('connection', (ws) => {
  ws.send('Nick Rules');
  ws.on('message', (message) => {
    console.log('recieved %s', message);
  });
});

