const mongo = require('mongodb');
const dbHost = '127.0.0.1';
const dbPort = 27017;

const DB = mongo.Db;
const Connection = mongo.Connection;
const Server = mongo.Server;
let db = new DB('local', new Server(dbHost, dbPort), {safe: true});

db.open((err, conn) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log('db state: ', db._state);
  const item = { name: 'Nick' };
  conn.collection('messages').insert(item, (err, item) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
    console.info('created/inserted: ', item);
  });

  conn.collection('messages').findOne(item, (err, item) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
   console.info('findOne: ', item);
   db.close();
   process.exit(0);
  });
});
