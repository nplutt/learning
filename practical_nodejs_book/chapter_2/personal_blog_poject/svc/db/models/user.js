const mongoose = require('mongoose');
const bcrypt = require('bcrypt-nodejs');
const validator = require('validator');

const userSchema = mongoose.Schema({
  email: { type: String, validate: [validator.isEmail, 'Invalid email'] },
  password: { type: String, min: 8, max: 16 }
});

userSchema.methods.generateHash = function(password) {
  return bcrypt.hashSync(password, bcrypt.genSaltSync(8), null);
};

module.exports = mongoose.model('User', userSchema);