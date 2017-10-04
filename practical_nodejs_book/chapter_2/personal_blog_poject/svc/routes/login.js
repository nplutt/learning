const express = require('express');
const router = express.Router();
const User = require('../db/models/user');


router.post('/', (req, res, next) => {
  User.findOne({ email: req.body.email }, (err, user) => {
    if (err) { next(err); }
    if (!user || !user.validPassword(req.body.password)) {
      res.sendStatus(400);
    } else {
      req.session.save((err) => { next(err) });
      res.sendStatus(200);
    }
  });
});

module.exports = router;