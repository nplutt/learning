const session = require('express-session');
const mongoStore = require('connect-mongo')(session);
const connection = require('../db/db');

function authSession() {
  return session({
    secret: process.env.SESSION_SECRET,
    saveUninitialized: false, // don't create session until something stored
    resave: false, //don't save session if unmodified
    store: new mongoStore({ mongooseConnection: connection }),
    cookie: { secure: process.env.ENVIRONMENT === 'production' }
  });
}

module.exports = authSession;