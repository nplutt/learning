const bcrypt = require('bcrypt-nodejs');
const mongoose = require('mongoose');
const validator = require('validator');

const userSchema = new mongoose.Schema({
  email: {
    type: String,
    unique: true,
    required: true,
    validate: [validator.isEmail, 'Invalid email']
  },
  password: {
    type: String,
    required: true,
    // validate: {
    //   isAsync: true,
    //   validator: function(v, cb) {
    //     setTimeout(() => {
    //       const msg = util.format('%s is not between 8 and 16 characters', v);
    //       cb(validator.isLength(v, {min: 8, max: 16}), msg);
    //     }, 5);
    //   }
    // }
  }
});

userSchema.methods.generateHash = function(password) {
  return bcrypt.hashSync(password, bcrypt.genSaltSync(8), null);
};

userSchema.methods.validPassword = function(password) {
  return bcrypt.compareSync(password, this.password);
};

module.exports = mongoose.model('User', userSchema);