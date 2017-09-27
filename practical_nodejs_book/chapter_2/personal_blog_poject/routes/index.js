const express = require('express');
const router = express.Router();
const AWS = require('aws-sdk');

AWS.config.update({ region: process.env.REGION });
const s3 = new AWS.S3();

// Get Angular 2 Application From S3
router.get('/', (req, res, next) => {
  const params = {
    Bucket: process.env.BUCKET_NAME,
    Key: 'index.htmla'
  };

  s3.getObject(params, (err, data) => {
    if (err) {
      if (err.statusCode === 404) {
        let err = new Error('Not Found');
        err.statusCode = 404;
        next(err);
      }
    } else {
      res.send(data.Body.toString());
    }
  });
});

module.exports = router;