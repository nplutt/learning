# Architecting to Scale


## Concepts

#### Loosely Coupled Architecture
* layers of abstraction
* Permits more flexibility
* Interchangeable components
* More atomic functional units

#### Horizontal vs. Vertical Scaling
| Horizontal Scaling | Vertical Scaling |
| ------------------ | ---------------- |
| Add more instances as demand increases | Add more CPU and or RAM to existing instances as demand increases |
| No downtime required to scale up or down | Requires restart to scale up or down |
| Automatic using Auto-scaling Groups | Would require scripting to automate |
| Almost unlimited | Limited by instance sizes |


## Auto Scaling

#### Types of Auto Scaling
| Scaling | What | Why |
| ------- | ---- | --- |
| Amazon EC2 Auto Scaling | DFocused on EC2 and nothing else | Setup scaling groups for EC2 instances; health checks to remove unhealthy instances |
| Application Auto Scaling | API used to control scaling for resources other than EC2 like Dynamo, ECS, EMR | Provides a common way to interact with the scalability of other services |
| AWS Auto Scaling | Provides centralized way to manage scalability for whole stacks; Predictive scaling feature | Console that can manage both the above and unified standpoint |

#### EC2 Auto Scaling Groups
* Automatically provides horizontal scaling for your landscape
* Triggered by an event or scaling action to either launch or terminate instances
* Availability, Cost and System metrics can all factor into scaling
* Four scaling options:
   - Maintain: Keep a specific or minimum number of instances running
   - Manual: Use maximum, minimum, or specific number of instances
   - Schedule: Increase or decrease instances based on schedule
   - Dynamic : Scale based on real-rime metrics of the system

#### Launch Configurations
* Specify VPC and subnets for scaled instances
* Attach to a ELB
* Define a Health Check Grace Period
* Define size of group to stay at initial size
* Or use scaling policy which can be based from metrics

#### EC2 Auto Scaling Policies
| Scaling | What | When |
| ------- | ---- | ---- |
| Target Tracking Policy | Scale based on a predefined or custom metric in relation to a target value | "When CPU utilization gets up to 70% on current instances, scale up." |
| Simple Scaling Policy | Waits until health check and cool down period expires before evaluating new need | "Let's add new instances slow and steady" |
| Step Scaling Policy | Responds to scaling needs with more sophistication and logic | "AGG! Add all the instances" |

#### Scaling Cooldown Concept for EC2
* Configurable duration that gives your scaling a chance to "come up to speed" and absorb load
* Default cooldown period is 300 seconds
* Automatically applies to dynamic scaling and optionally to manual scaling but not supported to scheduled scaling
* Can override default cooldown via scaling specified cooldown

#### AWS Application Auto Scaling 
| Scaling | What | When |
| ------- | ---- | ---- |
| target Tracking Policy | Initiates scaling events to try to track as closely as possible a given target metric | " I want my ECS hosts to stay at or below 70% CPU utilization |
| Step Scaling Policy | Based on a metric, adjusts capacity given certain defined thresholds. | "I want to increase my EC2 spot fleet by 20% everytime I add another 10,000 connections on my ELB" |
| Scheduled Scaling Policy | Initiates scaling events based on a predefined time, day or date | "Every Monday at 0800, I want to increase the Read Capacity Units of my DynamoDB table to 20,0000" |

#### AWS Predictive Scaling
Can use this to try to auto predict what scaling needs you'll have based on your app's history


## Kinesis
* Collection of services for processing streams of various data
* Data is processed in shards - with each shard able to ingest 1000 records per second
* A default limit of 500 shards, but you can request an increase to unlimited shards
* Record consists of a Partition Key, Sequence Number and Data Blow (up to 1 MB)
* Transient data store - Default retention of 24 hours but can be configured up to 7 days


## DynamoDB Scaling

#### DynamoDB Terminology
| Term | What |
| ---- | ---- | 
| Partition | A physical space where DynamoDB data is stored |
| Partition Key | A unique identifier for each record; sometimes called a hash key |
| Sort Key | In combination with a partition key, optional second part of a composite key that defines storage order; Sometimes called a Range Key |

#### DynamoDB Under the Hood
Partition Calculations:
* By Capacity: (Total RCU / 3000) + (Total WCU / 1000)
* By Size: Total Size / 10GB
* Total Partitions: Round Up from the MAX (By Capacity, By Size)

 #### Auto Scaling for DynamoDB
 * Using Target Tracking method to try to stay close to target utilization
 * Currently does not scale down if table's consumption drops to zero
 * Workaround 1: Send requests to the table until it auto scales down
 * Workaround 2: Manually reduce the max capacity to be the same as minimum capacity
 * Also supports Global Secondary Indexes - think of them like a copy of the table
 
 #### On-Demand Scaling for DynamoDB
 * Alternative to Auto-Scaling
 * Useful if you can't deal with scaling lag or truly have no idea of the anticipated capacity requirements
 * Instantly allocates capacity as needed with no concept of provisioned capacity
 *  Costs more than traditional provisioning and auto-scaling
 
 #### DynamoDB Accelorator (DAX)
 Good uses of DAX:
 * Requires fastest possible reads such as live auctions or securities trading
 * Read intensive scenarios where you want to offload the reads from DynamoDB
 * Repeated reads against a large set of DynamoDB data
 
 Bad uses of DAX:
 * Write intensive applications that don't have many reads
 * Applications where you use client caching methods
 
 
 ## CloudFront Part 2
 * Can deliver content to your users faster by caching static and dynamic content at edge locations
 * Dynamic content delivery is achieved using HTTP cookies forwarded from your origin
 * Supports Adobe Flash Media Server's RTMP protocol but you have to choose RTMP delivery method
 * Web distributions also support media streaming and live streaming but use HTTP or HTTPS
 * Origins can be S3, EC2, ELB or another web server
 * Multiple origins can be configured
 * Use behaviors to configure serving up origin content based on URL paths
 
 #### Invalidation Requests
 * Simply delete the file from the origin and wait for the TTL to expire
 * Use the AWS console to request invalidation for all content or a specific path such as /images/*
 * Use CloudFront API to submit an invalidation request
 
 
 ## SNS
 * Enables a publish/subscribe design pattern
 * Topics = A channel for publishing a notification
 * Subscription = Configuring and endpoint to recieve messages published on the topic
 * Endpoint protocols include HTTP(S), Email, SMS, SQS, Amazon Device Messaging (push notifications) and Lambda
 
 
 ## SQS
 * Reliable, highly scalable hosted message queuing service
 * Available integrations with KMS for encrypted messaging
 * Transient storage - default 4 days, max 14 days
 * Optionally supports First in First out queue ordering
 * Maximum message size of 256KB but using a special Java SQS SDK you can have messages as large as 2GB
 
 #### Amazon MQ
 * Managed implementation of Apache ActiveMQ
 * Fully managed and highly available within a region
 * ActiveMQ APU and supports JMS, NMS, MQTT, WebSocket
 * Designed as a drop-in replacement for on-premise message brokers
 * Use SQS if you are creating a new application from scratch
 * Use MQ if you want an easy low-hassle path to migrate from existing message brokers to AWS
 
 
 ## AWS Lambda, Serverless Application Manager and EventBridge
 
 #### Lambda
 * Allows you to run code on-demand without the need for infrastructure.
 * Supports multiple languages
 * Extremely useful option for creating serverless architectures
 * Code is stateless and executed on an event basis
 * No fundamental limits to scaling a function since AWS dynamically allocates capacity in relation to events
 
 #### AWS Serverless Application Model
 * Open source framework for building serverless apps on AWS
 * Uses YAML as the configuration language
 * Includes AWS CLI-like functionality to create, deploy and update serverless apps using AWS services such as Lambda, DynamoDB and API Gateway
 * Enables local testing and debugging of apps using Lambda-like emulator via Docker
 * Extension of CloudFormation so you can use everything CloudFormation can provide by way of resources and functions
 
 #### Amazon EventBridge
 * Designed to link variety of AWS and 3rd party apps to rules logic for launching other event based actions
 * eg: Datadog, PagerDuty, ZenDesk, etc...
 
 
 ## Simple Workflow Service (SWF)
 * Created distributed asynchronous systems as workflows
 * Supports both sequential and parallel processing
 * Tracks the state of your workflow which you interact and update via API
 * Best suited for human-enabled workflows like a order fulfillment or procedural requests
 * AWS recommends new applications - look at Step Functions over SWF
 
 
 ## Step Functions and Batch
 
 #### AWS Step Functions
 * Managed workflow and orchestration platform
 * Scalable and highly available 
 * Define your app as a state machine
 * Create tasks, sequential steps, parallel steps, branching paths or timers
 * Amazon State Language declarative JSON
 * Apps can interact and update the stream via Step Function API
 * Visual interface describes flow and realtime status
 * Detailed logs captured during each step
 
 #### AWS Batch
 Management tool for creating, managing and executing batch-oriented tasks using EC2 instances
 1. Create a Compute Environment: Managed or Unmanaged, Spot ot On-Demand, vCPUs
 2. Create a Job Queue with priority and assigned to a Compute Environment
 3. Create Job Definition: Script or JSON, environment variables, mount points, IAM role, container image, etc.
 4. Schedule job
 
 #### Comparisons
 | What | When | Use Case |
 | ---- | ---- | -------- |
 | Step Functions | Out-of-the-box coordination of AWS service components | Order Processing Flow |
 | Simple Workflow Service | Need to support external processes or specialized execution logic | Loan Application Process with Manual Review Steps |
 | Simple Queue Service | Messaging Queue; Store and forward patterns | Image Resize Process |
 | AWS Batch | Schedule or reocurring tasks that do not require heavy logic | Rotate Logs Daily on Firewall Appliance |
 
 
 ## Elastic MapReduce
 
 #### AWS ELastic MapReduce
 * Managed Hadoop framework for processing huge amounts of data
 * Also supports Apache Spark, HBase, Presto and Flink
 * Most commonly used for log analysis, financial analysis or extract, translate and loading (ETL) activities
 * A Step is a progromatic task for performing some process on the data (i.e. count words)
 * A Cluster is a collection of EC2 instances provisioned by EMR to run your steps
 
 
 ## Exam Tips
 Auto Scaling Groups:
 * Know the different scaling options and policies
 * Understand the difference and limitations between horizontal and vertical scaling
 * Know what a cool down period is and how it might impact your responsiveness to demand
 
 Kinesis:
 * Exam is likely to be restricted to the Data Stream use cases for Kinesis such as Data Streams and Firehose
 * Understand shard concept and how partition keys and sequences enable shards to manage data flow

DynamoDB Auto Scaling:
* Know the new and old terminology and concept of a partition, partition key and sort key in the context of DynamoDB
* Understand how DynamoDB calculates total partitions and allocates RCU and WCU across available partitions
* Conceptually know how data is stored across partitions

 CloudFront Part 2:
 * Know that both static and dynamic content are supported
 * Understand possible origins and how multiple origins can be used together with Behaviors
 * Know invalidation methods, zone apex and geo-restriction options
 
 SNS:
 * Understand a loosely coupled architecture and benefits it brings
 * Know the different types of subscription endpoints supported
 
 SQS:
 * Know the difference between Standard and FIFO queues 
 * Know difference between Pub/Sub (SNS) and Message Queueing (SQS) architecture
 
 Lambda:
 * Know what "Serverless" is in concept and how Lambda can facilitate such an architecture
 * Know the languages supprted by Lambda
 
 SWF:
 * Understand the difference and functions of a Worker and a Decider
 * Best suited for human-enabled workflows like order fulfillment or procedural requests
 
 Elastic MapReduce:
 * Understand the parts of a Hadoop landscape at a high level
 * Know what a Cluster is and what Steps are
 * Understand the roles or a Master Node, Core Nodes, and Task Nodes
 
 Step Functions:
 * Managed workflow and orchestration platform considered preferred for modern development over AWS SWS
 * Supports tasks, sequential steps, parallel steps, branching, times.
 
 AWS Batch:
 * Ideal for use cases where a routine activity must be performed at a specific interval or time of day
 * Behind the scenes, EC2 instances are provisioned as workers to perform the batch activities then terminated when done
 
 Auto Scaling:
 * Be familiar with the positioning and different purposes of EC2 Auto Scaling vs. Application Auto Scaling vs. AWS Auto Scaling
 * Know the different scaling options and policies
 * Understand the difference and limitations between horizontal and vertical scaling
 * Know what a cool down period is and how it might impact your responsiveness to demand
 
 White Papers:
 * [Web Application Hosting in the AWS Cloud](https://d1.awsstatic.com/whitepapers/aws-web-hosting-best-practices.pdf)
 * [Introduction to Scalable Gaming Patterns on AWS](https://d0.awsstatic.com/whitepapers/aws-scalable-gaming-patterns.pdf)
 * [Performance at Scale with Amazon ElastiCache](https://d0.awsstatic.com/whitepapers/performance-at-scale-with-amazon-elasticache.pdf)
 * [Automating Elasticity](https://d1.awsstatic.com/whitepapers/cost-optimization-automating-elasticity.pdf)
 * [AWS Well-Architected Framework](https://d0.awsstatic.com/whitepapers/architecture/AWS_Well-Architected_Framework.pdf)
 * [Microservice on AWS](https://d1.awsstatic.com/whitepapers/microservices-on-aws.pdf)
 * [Re:Invent Elastic Load Balancing Deep Dive](https://www.youtube.com/watch?v=9TwkMMogojY&ab_channel=AmazonWebServices)
 * [Re:Invent Scaling Up to Your First 10 Million Users](https://www.youtube.com/watch?v=w95murBkYmU&ab_channel=AmazonWebServices)
 * [Re:Invent Lean to Build a Cloud Scale WordPress Site](https://www.youtube.com/watch?v=dPdac4LL884&ab_channel=AmazonWebServices)
 
 
 ## Pro Tips
 * Elasticity will drive most benefit from the cloud
 * Think cloud first designs if you're in a green field scenario even if you're deploying on-prem
 * If you're in a brown field situation, create roadmaps for cloud-first enablers like distributed applications, federated data and SOA
 * Be careful not to let elasticity cover for poor development methods
 * Microservice concepts help achieve scalability via decoupling simplification and separation of concerns
 
 ## Challenges
 * Question 1:
    - My Answer: E
    - Correct Answer: E
    
* Question 2:
    - My Answer: A, C
    - Correct Answer: A, D