const assert = require('assert');
const expect = require('expect.js');
let expected, current;

before(() => {
  expected = ['a', 'b', 'c'];
});

describe('String split with assert', () => {
  beforeEach(() => {
    current = 'a,b,c'.split(',');
  });

  it('should return an array', () => {
    assert(Array.isArray(current));
  });

  it('should return the same array', () => {
    assert.equal(expected.length, current.length, 'arrays have equal length');
    for (let i=0; i<expected.length; i++) {
      assert.equal(expected[i], current[i], i + 'element is equal');
    }
  });
});


describe('String split with expect', () => {
  beforeEach(() => {
    current = 'a,b,c'.split(',');
  });

  it('should return an array', () => {
    expect(Array.isArray(current)).to.be.true;
  });

  it('should return the same array', () => {
    expect(expected.length).to.equal(current.length);
    for (let i=0; i<expected.length; i++) {
      expect(expected[i]).equal(current[i]);
    }
  });
});