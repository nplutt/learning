const express = require('express');
const router = express.Router();
const User = require('../db/models/user');


router.post('/', (req, res, next) => {
  const user = new User(req.body);
  user.password = user.generateHash(user.password);

  user.save((err) => {
    if (err) {
      next(err);
    } else {
      res.sendStatus(201);
    }
  });

});

module.exports = router;