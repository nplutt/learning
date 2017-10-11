const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const logger = require('morgan');

let app = express();

app.use(bodyParser.urlencoded());
app.use(bodyParser.json());
app.use(logger());

const dbUrl = process.env.DB_HOST;
const db = mongoose.connect(dbUrl, { useMongoClient: true });

let id = mongoose.Schema.ObjectId;

app.param('collectionName', (req, res, next, collectionName) => {
  req.collection = db.collection(collectionName);
  return next();
});

app.get('/', (req, res, next) => {
  res.send('Select a collection, e.g. /collection/messages');
});

app.get('collections/:collectionName', (req, res, next) => {
  req.collection.find({}, {
    limit: 10,
    sort[['_id', -1]]
  }).toArray((err, results) => {
    if (err) return next(err);
    res.send(results);
  });
});

app.post('collections/:collectionName', (req, res, next) => {
  req.collection.insert(req.body, {}, (err, results) => {
    if (err) return next(err);
    res.send(results);
  });
});

app.get('collections/:collectionName/:id', (req, res, next) => {
  req.collection.findOne({
    _id: id(req.params.id)
  }, (err, result) => {
    if (err) return next(e);
    res.send(result);
  });
});