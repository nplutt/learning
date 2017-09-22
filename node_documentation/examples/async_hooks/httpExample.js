const asyncHooks = require('async_hooks');
const fs = require('fs');
const http = require('http');

const hooks = {
  init: init,
  before: function before(asyncId) { },
  after: function after(asyncId) { },
  destroy: function destory(asyncId) { }
};

const asyncHook = asyncHooks.createHook(hooks);

asyncHook.enable();

http.createServer((req, res) => {
  res.end('hello qts');
}).listen(8000);

function init(asyncId, type, triggerId) {
  fs.writeSync(1, `${type} \n`);
}


