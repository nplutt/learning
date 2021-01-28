# Deployment and Operations Management

## Types of Deployments

#### Rolling Deployment
1. Create new launch configuration with the updated ami
2. Start terminating old EC2 instances

#### A/B Testing
1. Create two autoscaling groups
2. Send 90% of traffic to old and 10% to new using Route53

#### Canary Release
1. Deploy x number of new servers to the current cluster
2. Wait and see how those perform 
3. If they perform well then roll out the release to the rest of the cluster

#### Blue Green Deployment
1. Create new autoscaling group and new load balancer for the new servers
2. Switch Route53 over to point at the new servers while keeping the old servers alive
3. If all goes well scale down the old cluster
4. If it goes bad then update Route53 to point at the old cluster

#### Blue Green Contraindication
* Data store schema is too tightly coupled to the code changes
* The upgrade requires special upgrade routines to be run during deployment
* Off the shelf products may not be compatible


## Continuous Integration and Deployment

#### CI, CD, and CD too
* Continuous Integration: Merge code changes back to main branch as frequently as possible with automated testing as you go
* Continuous Delivery: You have automated your release process to the point you can deploy at a click of a button
* Continuous Deployment: Each code change that passes all stages of the release process is realeased to production with no human intervention required

#### CI/CD Considerations
* Objective is to create smaller, incremental compartmentalized improvements and features
* Lowers deployment risk and tries to limit negative impact
* Test automation must be strong
* Feature toggle patterns useful for dealing with in-progress features not ready for release (versus more traditional branching strategies)
* Microservice architectures lend themselves well to CI/CD practices


## Elastic Beanstalk
* Orchestration service to make it push button easy to deploy scalable web landscapes
* Wide range of supported platforms - from Docker to PHP to Java to NodeJS
* Multiple environments within application (dev, qa, prod, etc.)
* Great for ease of deployment, but not great if you need lots of control and flexibility

#### Elastic Beanstalk Deployment Options
| Deployment Option | What | Deployment Time | Downtime? | Rollback Process |
| ----------------- | ---- | --------------- | --------- | ---------------- |
| All at once | New application version is deployed to existing instances all at once, potentially resulting in downtime | 1 | Yes | Manual |
| Rolling | One by one, new application version is deployed to existing instances in batches | 2 | No | Manual |
| Rolling with Additional Batch | Launch new version instances prior to taking any old version instances out of service | 3 | No | Manual |
| Immutable | Launch a full set of new version instances in separate auto-scaling group and only cuts over when health check is passed | 4 | No | Terminate New Instances |
| Traffic Splitting | Percent of client traffic is routed to new instance for purpose of canary testing | 4  | No | Reroute DNS and Term New Instances |
| Blue/Green | CNAME DNS entry changed when new version is fully up, leaving old version in place until new is fully verified | 4 | No | Swap URL |
 
 
 ## Cloudformation
 * Infrastructure as code
 * Using JSON or YAML, you can model and provision entire landscapes
 * Repeatable, automatic deployments and rollbacks
 * Nest common components for re-usability
 * Supports over 300 resource types
 * Want more? Supports custom resources via SNS or Lambda.
 
 #### Cloudformation Concepts
 | What | Function |
 | ---- | -------- | 
 | Templates | The JSON or YAML text file that contains the instructions for building out the AWS environment |
 | Stacks | The entire environment described by the template and created, updated, and deleted as a single unit |
 | Change Sets | A summary of proposed changes to your stack that will allow you to see how those changes might impact your existing resources before implementing them |
 
 #### Stack Policies 
 * Protect specific resources within your stack from being unintentionally deleted or updated
 * Add a Stack Policy via the console or CLI when creating a stack
 * Adding a Stack Policy to an existing stack can only be done via CLI
 * Once applies, a Stack Policy cannot be removed but it can be modified via CLI
 
 #### CloudFormation Best Practices
 * AWS provides Python "helper scripts" which can help you install software and start services on your EC2 instances
 * Use CloudFormation to make changes to your landscape rather than going directly into the resources
 * Make use of Change Sets to identify potential trouble spots in your updates
 * Use Stack Policies to explicitly protect sensitive portions of your stack
 * Use a version control system to track changes to templates 
 
 
 ## API Gateway
 * Managed, high availability service to front-end REST APIs
 * Backed with custom code via Lambda, as a proxy for another AWS Service or any other HTTP API on AWS or elsewhere
 * Regionally based, private or edge optimized
 * Support API Keys and Usage Plans for user identifications, throttling or quota management
 * Using CloudFront behind teh scenes and custom domains and SNI are supported
 * Can be published as products and monetized on AWS marketplace
 
 
 ## Management Tools
 
 #### AWS Config
 * Allows you to assess, audit and evaluate configurations of your AWS resources
 * Very useful for Configuration Management as part of an ITIL program
 * Creates a baseline of various configuration settings and files then can track variations against that baseline
 * AWS Config Rules can check resources for certain desired conditions and if violations are found, the resources is flagged as "noncompliant"
 
 Example Config Rules:
 * Is backup enabled on RDS?
 * Is CloudTrail enables on the AWS account?
 * Are EBS volumes always encrypted?
 
#### AWS OpsWorks
* Managed instances of Chef and Puppet - two very popular automations platforms
* Provide configuration management to deploy code, automate tasks, configure instances, perform upgrades, etc.
* Has three offerings: OpsWorks for Chef Automate, OpsWorks for Puppet Enterprise and OpsWorks Stacks
* OpsWorks for Chef Automate and Puppet Enterprise are fully managed implementations of each respective platform
* OpsWorks Stacks is an AWS creation and uses an embedded Chef solo client installed on EC2 instance to run Chef recipes
* OpsWorks Stacks support EC2 instances and on-prem servers as well with an agent

#### AWS OpsWork Stacks
* Stacks are collections of resources needed to support a service or application
* Layers represent different components of the application delivery hierarchy
* EC2 instances, RDS instances, and ELBs are examples of Layers
* Stack can be cloned - but oly withing the same region
* OpsWorks is a global service. But when you create a stack, you must specify a region and that stack can only control resources in that region.


## AWS System Manager
* Centralized console and toolset for a wide variety of system management tasks
* Designed for managing a large fleet of systems - tens or hundreds
* SSM Agent enables System Manager features and support all OSs supported by OS as well as back to Windows Server 2003 and Rasbian
* SSM Agent installed by default on recent AWS-provided base AMIs for Linux and Windows
* Manages AWS-based and on-premises based systems via the agent

| Service | Description | Example |
| ------- | ----------- | ------- |
| Inventory | Collect OS, application and instances metadata about instances | Which instances have Apache HTTP Server 2.2.x or earlier? |
| State Manager | Create states that represent a certain configuration is applied to instances | Keep track of which instances have been updates to the current stable version of Apache HTTP Server |
| Logging | CloudWatch Log agent and stream logs directly to CloudWatch from instances | Stream logs of our web servers directly to CloudWatch for monitoring and notification |
| Parameter Store | Shared secure storage for config data, connections strings, passwords, etc. | Store and retrieve RDS credentials to append to a config file upon boot |
| Insight Dashboards | Account-level view of Cloudtrail, Config, Trust Advisor | Single viewport for any exceptions on config compliance |
| Resource Groups | Group resource through tagging for organization | Create a dashboard for all assets belonging to production ERP landscape |
| Maintenance Windows | Define schedules for instances to patch update apps, run scripts and more. | Define hours of 00:00 to 02:00 as maintenance windows for Patch Manager |
| Automation | Automating routine maintenance tasks and scripts | Stop DEV and QA instance every Frinday and restart Monday morning |
| Run Command | Run commands and scripts without logging in via SSH or RDP | Run a shell script on 53 different instances at the same time |
| Patch Manager | Automates process of patching instances for updates | Keep a fleet at teh same patch level by applying new security patches during next Maintenance Window |

#### AWS System Manager Documents 
| Type | Used With | Purpose |
| ---- | --------- | ------- |
| Command Document | Run Command State Manager | Run Command uses command documents to execute commands. State manager uses command documents to apply a configuration. These actions can be run on one or more targets at any point during the lifecycle of an instance |
| Policy Document | State Manager | Policy documents enforce a policy on your targets. If the policy document is removed, the policy actions (for example, collecting inventory) no longer happens |
| Automation Document | Automation | Use automation documents when performing common maintenance and development tasks such as creating or updating an Amazon Machine Image |


## Business Applications and End-User Computing

#### Amazon WorkSpaces and AppStream
* WorkSpaces: Desktop as a service that you remote into just as if it was a normal PC
* AppStream: Encapsulates applications and allows you to access those applications via a web browser

Notes:
* Full managed desktop as a service (WorkSpaces) and application hosting (AppStream)
* Everything lives on AWS infrastructure and can be tightly managed and controlled
* Use Case: Highly regulated industries where security and confidentiality is a concern. Can be used to keep all data in a protected VPC and off local PCs.
* Use Case: Remote or seasonal workers such as a distributed call center. Given remote workers virtual desktops or hosted applications and let them use their own PCs.
* Use Case: Allow customers to demo your product

#### Amazon Connect and Amazon Chime
Amazon Connect:
* Fully managed cloud-based contact center solution with configurable call handling, inbound and outbound telephony, interactive voice response, chatbot technology and analytics
* Can integrate with other enterprise applications like Customer Relationship Management (CRM systems)

Amazon Chime:
* Online meeting and video conferencing service
* Supports usual conferencing features like desktop sharing, group chat and session recording

#### Amazon WorkDocs and Amazon WorkMail
Amazon WorkDocs:
* Online document storage and collaboration platform
* Supports version management, sharing documents and collaborative edits

Amazon WorkMail:
* Fully managed email and calendar as a service
* Compatible with Outlook, IMAP, Android and iOS mail clients

#### Amazon WorkLink and Alex for Business
Amazon WorkLink:
* Provide secure access to internal web applications for mobile devices
* When mobile user requests an app, it's rendered on a secure machine then the image is sent to the mobile client

Alexa for Business:
* Deploy Alexa functionality and skills internally in your enterprise
* Management functionality more appropriate for an enterprise organization than buying and provisioning individual Alexa devices


## Machine Learning Landscape

Amazon Comprehend
* What: natural Language Processing (NLP) service that finds insight and relationships within text
* When Sentiment analysis of social media posts

Amazon Forecast
* What: Combines time-series data with other variables to deliver highly accurate forecasts
* When: SForecast seasonal demand for a specific shirt

Amazon Lex
* What: Build conversational interfaces that can understand the intent and context of natural speech
* When: Create a customer service chatbot to automatically handle routine requests

Amazon Personalize
* What: Recommendation engine as a service based on demographic and behavioral data
* When: Provide potential upsell products at checkout during a web transaction

Amazon Polly
* What: text to speech service supporting multiple languages, accents and voices
* When: Provide dynamically generated personalize voice response for inbound callers

Amazon Rekognition
* What: Image and vide analysis to parse and recognize objects, people, activities and facial expressions
* When: Provide an additional form of employee authentication through facial recognition as they can an access badge

Amazon Textract
* What: Extract text, context and metadata from scanned documents
* When: Automatically digitize and process physical paper forms

Amazon Transcribe:
* What: Speech to text as a service
* When: Automatically create transcripts of recorded presentations

Amazon Translate
* What: Translate text to and from many different languages
* When: Dynamically create localized web content for users based on their geography


## Exam Tips



