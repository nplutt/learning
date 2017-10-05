The original ask of this chapter was to make a personal blog, however since I've already done 
authentication and an angular2 application served out of S3 I decided to make a simpler app.  The
application does the following:
- Serves an angular 2 application from an S3 bucket
- Authenticates users using express sessions and mongo to store the sessions
- Stores new users in mongodb, uses mongoose to interact with the database

