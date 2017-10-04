const express = require('express');
const cookieParser = require('cookie-parser');
const bodyParser = require('body-parser');
const logHandler = require('./handlers/errorLogging');
const errorHandler = require('./handlers/errorHandling');
const authHandler = require('./handlers/sessionHandler');
const index = require('./routes/index');
const signUp = require('./routes/signUp');
const login = require('./routes/login');

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(authHandler());

app.use('/', index);
app.use('/signup', signUp);
app.use('/login', login);

app.use(logHandler);
app.use(errorHandler.badRequestErrorHandler);
app.use(errorHandler.statusCodeErrorHandler);

module.exports = app;