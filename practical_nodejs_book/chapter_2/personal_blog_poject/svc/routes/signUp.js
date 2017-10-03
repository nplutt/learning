const express = require('express');
const router = express.Router();
const User = require('../db/models/user');
const errors = require('../handlers/errors');


router.get('/', (req, res, next) => {
  const user = new User(req.body);
  user.save((err) => {
    if (err) {
      if (err.type === ValidationError) {
        next(new errors.BadRequestError())
      } else {
        next(new errors.ExpressError())
        }
    } else {
      res.statusCode = 201
    }
  })
});

module.exports = router;