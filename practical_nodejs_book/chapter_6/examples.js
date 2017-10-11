let auth = function(req, res, next) {
  //authorize a user and throw a 401 if not
  res.send(401);
  return next();
}

// next() is important and how express handles going to the next handler

//session based auth function
let auth = function(req, res, next) {
  if (req.query.token && token === SECRET_TOKEN) {
    return next();
  } else {
    return next(new Error('Unauthorized'));
  }
}

// session login for web
app.post('/login', (req, res, next) => {
  if (checkCreds(req)) {
    req.session.auth = true;
    req.redirect('/dashboard');
  } else {
    res.send(401);
  }
});



// Protect all /api/ endpoints
app.all('/api/*', auth);
app.get('/api/users', users.list);
app.post('/api/users', users.create);
