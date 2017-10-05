const express = require('express');
const router = express.Router();


router.get('/', (req, res, next) => {
  if (!req.session.email || !req.cookies.session_id) {
    res.sendStatus(400);
  }

  res.statusCode(200);
  res.send('This is a secure endpoint!');
});

module.exports = router;