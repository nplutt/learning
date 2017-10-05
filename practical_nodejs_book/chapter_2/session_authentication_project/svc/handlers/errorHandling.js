function badRequestErrorHandler(err, req, res, next) {
  if (err.name === 'MongoError') {
    if (err.message.indexOf('duplicate key error') > -1) {
      err.statusCode = 400;
    }
  }

  if (err.name === 'ValidationError') {
    err.statusCode = 400;
  }

  next(err);
}

function statusCodeErrorHandler(err, req, res, next) {
  switch(err.statusCode) {
    case 400:
      res.sendStatus(400);
      break;
    case 401:
      res.sendStatus(401);
      break;
    case 403:
      res.sendStatus(403);
      break;
    case 404:
      res.sendStatus(404);
      break;
    default:
      res.sendStatus(500);
  }
}

module.exports = {
  badRequestErrorHandler: badRequestErrorHandler,
  statusCodeErrorHandler: statusCodeErrorHandler
};
