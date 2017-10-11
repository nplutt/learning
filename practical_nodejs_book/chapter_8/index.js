const express = require('express');
const mongoose = require('mongoose');
const objectId = require('mongoose').Types.ObjectId;
const bodyParser = require('body-parser');

let app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
// app.use(logger());

const dbUrl = process.env.DB_HOST;
const db = mongoose.connect(dbUrl, { useMongoClient: true });

mongoose.connection.on('connected', () => {
  console.log('Connection to mongodb database was successfully established');
});

let id = mongoose.Schema.ObjectId;

app.param('collectionName', (req, res, next, collectionName) => {
  req.collection = db.collection(collectionName);
  return next();
});

app.get('/', (req, res, next) => {
  res.send('Select a collection, e.g. /collection/messages');
});

app.get('/collections/:collectionName', (req, res, next) => {
  req.collection.find({}, {
    limit: 10,
    sort: [['_id', -1]]
  }).toArray((err, results) => {
    if (err) return next(err);
    res.send(results);
  });
});

app.post('/collections/:collectionName', (req, res, next) => {
  req.collection.insert(req.body, {}, (err, results) => {
    if (err) return next(err);
    res.json(results.ops);
  });
});

app.get('/collections/:collectionName/:id', (req, res, next) => {
  req.collection.findOne({
    _id: new objectId(req.params.id)
  }, (err, result) => {
    if (err) return next(err);
    res.json(result);
  });
});

app.put('/collections/:collectionName/:id', (req, res, next) => {
  req.collection.update({
      _id: new objectId(req.params.id)
    }, {$set:req.body}, {safe:true, multi:false},
    (err, result) => {
      if (err) return next(err);
      res.send((result.result.ok === 1) ? {msg:'success'} : {msg:'error'})
    }
  );
});

app.delete('/collections/:collectionName/:id', (req, res, next) => {
  req.collection.remove({
      _id: id(req.params.id)
    },
    (err, result) => {
      if (err) return next(err);
      res.send((result.result.ok === 1) ? {msg:'success'} : {msg:'error'})
    }
  );
});

app.listen(3000, () => {
  console.log('Server is running on port: ', 3000)
});