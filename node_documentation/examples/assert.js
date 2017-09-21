const assert = require('assert');


const object1 = {
  a: {
    b: 1
  }
};

const object2 = {
  a: {
    b: 2
  }
};

const object3 = {
  a: {
    b: 1
  }
};

const object4 = {
  a: {
    b: '1'
  }
};

// deepEqual

//assert.deepEqual(object1, object3); // passes

//assert.deepEqual(object1, object2); //fails


// deepStrictEqual
//assert.deepEqual(object1, object4); //passes

//assert.deepStrictEqual(object1, object4); //fails


//doesNotThrow
//assert.doesNotThrow(() => {
//  throw new TypeError('Wrong Value'); //throws a type error
//}, SyntaxError);

//assert.doesNotThrow(() => {
//  throw new TypeError('WrongValue'); //throws an assertion error instead of a type error
//}, TypeError, 'whoops');


//equal
//assert.equal(1, 1); // passed

//assert.equal(1, '1'); // passed

//assert.equal(1, 2); //fails

//assert.equal({a: {b: 1}}, {a: {b: 1}}); //fails 


//fail
//assert.fail(); // Throws failed assertion error


//error
//assert.error(); // Throws value if the value is truthy


//notDeepEqual
//assert.notDeepEqual(object1, object1); //fails

//assert.notDeepEqual(object2, object1); //passes


//notDeepStrictEqual


//notEqual


//notStrictEqual


//ok


//strictEqual


//throws
