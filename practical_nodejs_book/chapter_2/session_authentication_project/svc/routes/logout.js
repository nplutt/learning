const express = require('express');
const router = express.Router();


router.get('/', (req, res, next) => {
  if (req.session.email && req.session.session_id) {
    res.clearCookie('session_id');
    res.sendStatus(200)
  } else {
    res.sendStatus(400);
  }
});

module.exports = router;