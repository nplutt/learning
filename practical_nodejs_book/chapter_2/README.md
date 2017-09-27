Requirements:
* An individual article page with a full text article
* An admin page for publishing and removing content
* A login page for accessing the admin page
* A post article page for publishing new content

Architecture Initial:
* Login: Session based authentication
* Database: MongoDB
* UI: Angular 2

Architecture AWS:
In order to involve this project more closely with AWS I will be using AWS services where appropriate.  
* Login: The Cognito service will be used
* Database: Instead of using MongoDB I will be using DynamoDB
* UI: Angular 2

