const express = require('express');
const cookieParser = require('cookie-parser');
const bodyParser = require('body-parser');
const logHandler = require('./handlers/errorLogging');
const errorHandler = require('./handlers/errorHandling');
const authHandler = require('./handlers/sessionHandler');
const index = require('./routes/index');
const signUp = require('./routes/signUp');


const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(authHandler());

app.use('/', index);
app.use('/signup', signUp);

app.use(logHandler);
app.use(errorHandler);

module.exports = app;