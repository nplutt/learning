const express = require('express');
const router = express.Router();
const validator = require('validator');


router.get('/', (req, res, next) => {
  if (!validator.isEmail(req.body.email) || !validator.isLength(req.body.password, {min: 8, max:16})) {
    let error = new Error();
    error.statusCode = 400;
    throw error;
  }
});

module.exports = router;