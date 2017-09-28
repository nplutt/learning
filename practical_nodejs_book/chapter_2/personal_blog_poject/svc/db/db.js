const mongoose = require('mongoose');
const dbUrl = process.env.DB_HOST;

mongoose.connect(dbUrl);

mongoose.connection.on('connected', () => {
  console.log('Connection to mongodb database was successfully established');
});

mongoose.connection.on('error', (err) => {
  console.error('Connection to mongodb database failed, error:' + err);
});

mongoose.connection.on('disconnect', () => {
  console.log('Connection to mongodb has been disconnected');
});

process.on('SIGINT', () => {
  mongoose.connection.close(() => {
    console.log('Connection to the database has been disconnected because of application termination');
    process.exit(0);
  });
});
