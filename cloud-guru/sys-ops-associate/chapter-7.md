# Automation

## CloudFormation

#### Exam Tips
* CloudFormation allows you to manage, configure and provision AWS infrastructure as
code.
* Remember the main sections in the template are:
  - Parameters: input custom values
  - Conditions: e.g. provision resources based on environments
  - Resources: mandatory, the aws resources to create
  - Mappings: create custom mappings like Region: AMI
  - Transforms: reference code locates in S3 e.g. lambda for or reusable snippets
  of cloudformation code
  
## Elastic Beanstalk

#### What is Elastic Beanstalk?
* It is a service for deploying and scaling web application developed in many popular
languages into widely used application server platforms like Apache, Nginx, Passenger,
IIS.
* Users can focus on writing code and don't need to worry about any of the underlying
infrastructure needed to run the application.
* You ipload the code and Elastic Beanstalk will handle the deployment, capacity
provisioning, load balancing, auto-scaling, and application health.
* You retain full control of the underlying AWS resources powering your application 
and you pay only for the AWS resources required to store and run your applications.
* Fastest and simplest way to deploy your application in AWS.
* Automatically scales your application up and down.
* You can select the EC2 instance type that is optimal for your application.
* You can either retain full administrative control over the resources powering your
application, or have Elastic Beanstalk do it for you.
* Automatically manages platform updates.
* Monitor and manage application via a dashboard
* Integrated with CloudWatch and X-Ray

## AWS OpsWorks

#### What is OpsWorks?
* Is a service that allows you to automate your server configuration using Puppet 
or Chef. 
* Using managed instances instead of either puppet or chef
* Enables configuration management for your OS and applications
* Allows you to automate server config using code
* Works with existing Chef and Puppet code

