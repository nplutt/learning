# Policies and Standards Automation

## AWS Service Catalog
A brief overview:
* It enables organizations to create and manage catalogs of products that are approved for use on AWS
* It has an API that provides programmatic control over all end user actions as an alternative to the AWS console
* It allows you to create your own custom interfaces and apps
* It allows admins to create and distribute application stacks called products
* Products can be grouped into folders called portfolios
* Users can then launch an manage products themselves without requiring access to the AWS services or AWS console
* Users only see the products they are supposed to see

## AWS Trusted Advisor
A service that provides you with real time guidance to ensure your AWS resources are provisioned and managed correctly, and are following AWS best practices

#### Categories
* Cost optimization - are you paying too much
* Performance - service utilization
* Security - is the account secure
* Fault Tolerance - are you ready for an incident
* Service Limits - are you close to breaching any service limits

## AWS Systems Manager
A management service that assists with:
* Collecting software inventory
* Applying OS patches
* Creating system images
* Configuring operating systems
* Manage hybrid cloud systems from a single interface
* Reducing costs

#### Features
* Run command
* State Manager
* Inventory 
* Maintenance Windows
* Patch Manager
* Automation
* Parameter Store

## AWS Organizations
Policy based management for multiple accounts
* Can programmatically create new accounts
* Create and maintain groups of accounts
* Set policies on those groups

## AWS Secrets Manager
A service to help you protect secrets needed to access your applications, services and IT resources
* It encrypts secrets at rest using your own encryption keys stored in KMS
* Secrets can be database credentials, passwords, third party API keys or even text
* You can store and control access to them with the Secrets Manager Console/CLI/API/SDK
* Hard coded credentials in code are replaced with an API call to Secrets Manager
* Secrets can be rotated automatically according to your own schedule

## Amazon Macie
A security service that uses machine learning to automatically discover, classify, and protect sensitive data in AWS
* Can recognize any PII
* Provides dashboard
* Monitors data access activity for anomalies
* Generates detailed alerts when it detects risk on unauthorized access or accidental data leaks
* It currently protects data in S3, with more AWS data stores planned for the future
* It gives you superior visibility of data
* Simple to setup and easy to manage

## AWS Certificate Manager
Easily provision, manage, and deploy SSL/TLS certificates
* Centrally managed certificates in AWS
* Audit the use of each certificate in CloudTrail logs
* Private certificate authority
* AWS integrations
* Import 3rd party certificates from other CAs



