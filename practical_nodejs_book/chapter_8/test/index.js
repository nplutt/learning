const superagent = require('superagent');
const expect = require('expect.js');
const describe = require('mocha').describe;
const it = require('mocha').it;

describe('express rest api server', () => {
  let id;
  let basePath = 'http://localhost:3000/collections/test';

  it('post object', (done) => {
    superagent.post(basePath)
      .send( { name: 'Nick', email: 'nplutt@gmail.com '})
      .end((err, res) => {
        expect(err).to.equal(null);
        expect(res.body.length).to.equal(1);
        expect(res.body[0]._id.length).to.equal(24);
        id = res.body[0]._id;
        done();
      });
  });

  it('retrieves an object', (done) => {
    superagent.get(basePath + '/' + id)
      .end((err, res) => {
        expect(err).to.equal(null);
        expect(res.body.length).to.equal(1);
        expect(res.body[0]._id.length).to.equal(24);
        id = res.body[0]._id;
        done();
      });
  });

  it('retrieves a collection', (done) => {
    superagent.get(basePath)
      .end((err, res) => {
        expect(err).to.eql(null);
        expect(res.body.length).to.be.above(0);
        expect(res.body.map(function (item){
          return item._id;
        })).to.contain(id);
        done();
      });
  });

  it('updates an object', (done) => {
    superagent.put(basePath + id)
      .send({name: 'James', email: 'james@gmail.com'})
      .end((err, res) => {
        expect(err).to.eql(null);
        expect(typeof res.body).to.eql('object');
        expect(res.body.msg).to.eql('success');
        done();
      });
  });

  it('checks an updated object', (done) => {
    superagent.get('http://localhost:3000/collections/test/'+id)
      .end((err, res) => {
        expect(err).to.eql(null);
        expect(typeof res.body).to.eql('object');
        expect(res.body._id.length).to.eql(24);
        expect(res.body._id).to.eql(id);
        expect(res.body.name).to.eql('Peter');
        done();
      });
  });

  it('removes an object', (done) => {
    superagent.del('http://localhost:3000/collections/test/'+id)
      .end((err, res) => {
        expect(e).to.eql(null);
        expect(typeof res.body).to.eql('object');
        expect(res.body.msg).to.eql('success');
        done();
      });
  });
});