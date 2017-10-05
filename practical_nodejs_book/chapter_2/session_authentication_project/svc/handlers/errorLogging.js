function logHandler(err, req, res, next) {
  console.error(err);
  next(err);
}

module.exports = logHandler;