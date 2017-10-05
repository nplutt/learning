function cookieHandler(err, req, res, next) {
  if (req.cookies.session_id && !req.session.email) {
    res.clearCookie('session_id');
  }
  next();
}

module.exports = cookieHandler;