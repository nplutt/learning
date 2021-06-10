# High Availability, Fault Tolerance and Disaster Recovery

## AWS Single Sign On
A cloud service that makes it easy to centrally manage single sign on access to multiple AWS accounts and business applications

#### Features
* Integrates with AWS Organizations: easily manage access to all of your AWS accounts
* Create/Manage Users & Groups: provide tiered level access based on user accounts or group membership all in the AWS console
* SSO Access to Cloud Applications: easily manage access to your cloud applications without any third party solutions required
* Use Existing Corporate Identities: Integrate with Microsoft AD through the AWS Directory Service for easy setup

#### Relevance
* Highly available - an AWS cloud service so high availability is default
* Fault tolerant - you aren't managing the hardware or software, no risk of failure

## AWS CloudFront
A fast CDN that securely delivers data, videos, applications and APIs to customers globally

## AutoScaling and Lifecycle Hooks
Scale your EC2 instance capacity automatically according to your defined conditions

#### Auto Scaling Benefits
* High availability
* Better fault tolerance
* Better cost management

#### The Auto Scaling Lifecycle
1. Starts when the auto scaling group launches an instance
1. Ends when you terminate the instance
1. Ends when the auto scaling group takes the instance out of service and terminates it

#### How Lifecycle Hooks Work
1. Auto scaling responds to a scale out event by launching an instance
1. Auto scaling puts the instance in the Pending:Wait state
1. Auto scaling sends a message to the notification target defined for the hook, along with information and a token
1. Waits until you tell it to continue or the timeout ends
1. You can now perform your custom action, install software, etc
1. By default the instance will wait for an hour and will change state to Pending:Proceed, then if will enter the InService state

#### Notes
* You can change the heartbeat timeout, or you can define it when you create the lifecycle hook in the CLI with the hearbeat-timeout parameter
* You can call the complete-lifecycle-action command to tell the Auto Scaling group to proceed
* You can call the record-lifecycle-action-heartbeat command to add more time to the timeout
* 48 hours is the maximum you can keep a server in a wait state, regardless of heartbeats

#### Cool downs
* Cool downs help ensure the autoscaling group doesn't launch/terminate more instances than needed
* Cool downs start when an instance enters the InService state, so if an instance is left in the Pending:Wait state as you perform functions on it, auto scaling will still wait before adding any additional servers

#### Abandon or Continue
* At the conclusion of an lifecycle hook, an instance can result in one of two states: Abandon or Continue
* Abandon will cause auto scaling to terminate the instance and if necessary launch a new one
* Continue will put the instance into service

#### Spot Instances
* Can use lifecycle hooks with spot instances
* This does not prevent an instance from terminating due to a change in the spot price
* When a spot instance terminates you must till complete the lifecycle action

## Amazon Route53
A highly available and scalable cloud DNS service

#### Features
* Highly Available DNS: Built using AWS's highly available infrastructure. DNS is distributed and Amazon state they will use reasonable efforts to make Route53 100% available.
* Interface with EC2 and S3: Connect your DNS records to load balancers and S3 buckets
* Makes you fault tolerant: Provides multiple routing types to ensure your customers get a great experience, such as latency based routing and weighted round robin

#### Routing Policies
* Failover routing policy
* Geolocation routing policy
* Geoproximity routing policy
* Latency routing policy
* Multivalue answer routing policy
* Weighted routing policy

## Amazon RDS
Amazon Relational Database Service lets you create, run and scale relational databases in the cloud.

* All databases can scale up their storage while live except Microsoft SQL Server

## Amazon Aurora

#### Overview
* Fast and reliable
* Simple
* Cost effective
* 5x throughput of MySQL on same hardware
* Storage is fault tolerant and self healing
* Disk failures are repaired in background
* Detect crashes and restarts
* No crash recovery or cache rebuilding required
* Automatic failover to one of up to 15 read replicas
* Storage autoscaling from 10GB to 64 TB

#### Backups & Snapshots
Backups:
* Automatic, continuous incremental backups
* Point in time restore within secods
* Up to 35 day retention period
* Stored in S3
* No impact on database performance

Snapshots:
* User initiated snapshots are stored in S3
* Kept until you explicitly delete them

#### Failure and Fault Tolerance
Database Failure:
* 6 copies of your data
* 3 availability zones
* Recovery in a healthy availability zone
* Point in time snapshot restore

Fault tolerance:
* Data is divided into 10GB segments across many disks
* Transparently handles loss
* Can lose 2 copies of data with out affecting write
* Can lose 3 copies of data with out affecting read
* All storage is self healing

#### Replicas
Amazon Aurora Replicas:
* Share underlying volume with the primary instance
* Updates made by primary are visible to all replicas
* Up to 15
* Low performance impact on primary
* Replica can be a failover target with no data loss

MySQL Read Replicas
* Primary instance data is replayed on your replica as transactions
* Up to 5
* High performance impact on primary
* Replica can be failover target with potentially minutes of data loss

#### Security
* All aurora instances must be in a VPC
* SSL AES-256 used to secure data in transit
* You can encrypt databases using AWS Key management service
* Encrypted storage, backups, snapshots, and replicas
* Note: You can't encrypt an existing unencrypted database

#### Connection Management
* Cluster endpoint: connects to the current primary DB instance for that DB cluster
* Reader endpoint: provides load balancing support for read-only connections
* Custom endpoint: Represent a set of DB instances you choose
* Instance endpoint: Connects to a specific instance within a cluster

## DynamoDB
A fully managed NoSQL database that supports key-value and document data structures

#### Details
* A fully managed, NoSQL database service
* Predictable fully manageable performance, with seamless scalability
* No visible servers
* No practical storage limits
* Fully resilient and highly available 
* Performance scales - in a linear way
* Fully integrated with IAM - rich and controllable security

#### More Details
* DynamoDB is a collection of tables
* Tables are the highest level structure within a database
* Its on tables that you specify the performance requirements
* Write capacity units - number of 1KB blocks per second
* Read capacity units - number of 4kb blocks per second
* DynamoDB uses the performance and the data quality to manage underlying resource provisioning
* Unlike SQL databases, the data structure nor schema is NOT defined at the table level

## DynamoDB Keys and Streams
* Partition key = hash attribute
* Sort Key = range attribute

#### Secondary Indexes
* A secondary index lets you query the table data using an alternate key
* You can create one or more indexes on a table
* Once created you can query the index like you do from the table
* Two kinds of indexes:
  - Global secondary index: index with partition key and sort key which can be different from those on the table
  - Local secondary index: index with the same partition key but different sort key from those on the table
  
#### Streams
* Optional feature
* Captures data modification events in DynamoDB tables
* Data about the events appear in the stream near real time in order
* Each event is represented by a stream record when:
  - A new item is added
  - An item is updated
  - An item is deleted
* You can trigger AWS Lambda when a particular event appears in the stream




