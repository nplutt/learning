const express = require('express');
const router = express.Router();
const AWS = require('aws-sdk');
const util = require('util');

AWS.config.update({ region: process.env.REGION });
const s3 = new AWS.S3();

// Get Angular 2 Application From S3
router.get('/', (req, res, next) => {
  const params = {
    Bucket: process.env.BUCKET_NAME,
    Key: 'index.html'
  };

  s3.getObject(params, (err, data) => {
    if (err) {
      if (err.statusCode === 401 || err.statusCode === 403) {
        console.error(util.format('Accessing the index.html file in the %s bucket failed ' +
          'due to AWS permissions', params.Bucket));
      }
      next(err);
    } else {
      res.statusCode = 200;
      res.send(data.Body.toString());
    }
  });
});

module.exports = router;