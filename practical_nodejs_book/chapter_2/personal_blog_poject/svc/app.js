const express = require('express');
const cookieParser = require('cookie-parser');
const bodyParser = require('body-parser');
const db = require('./db/db');
const logHandler = require('./handlers/errorLogging');
const errorHandler = require('./handlers/errorHandling');
const index = require('./routes/index');

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());

app.use('/', index);

app.use(logHandler);
app.use(errorHandler);

module.exports = app;