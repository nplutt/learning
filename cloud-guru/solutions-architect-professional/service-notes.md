# Server Migration Service
Migrates VMware vSphere, Microsoft Hyper-V/SCVMM, and Azure virtual machines to the AWS Cloud.
* Incrementally replicates your server VMs as cloud hosted AMIs
* Allows scheduling for replication on a group of servers
* AWS SMS replicates incremental changes to your on-premises servers and transfers only the delta to the cloud, you can test small changes iteratively and save on network bandwidth.
* AWS SMS supports the replication of operating system images containing Windows, as well as several major Linux distributions.

#### Limits
* 50 concurrent VM migrations per account, unless a customer requests a limit increase.
* 90 days of service usage per VM (not per account), beginning with the initial replication of a VM. We terminate an ongoing replication after 90 days unless a customer requests a limit increase.
* 50 concurrent application migrations per account, with a limit of 10 groups and 50 servers in each application

# VM Import/Export
* Enables easy import VM images from your existing environment to EC2 instances and export them back to your on-prem environment.
* To import images, use the AWS CLI to import the VM image from your VMware environment. VMware vSphere virtualization platform users can also use the AWS Management Portal for vCenter to import your VM.
* Export imported EC2 instances using the AWS CLI and specify an S3 bucket for the exported instance to be saved to.

#### Common Uses
* Migrating existing applications and workloads to EC2
* Copy VM image catalog to EC2
* Create DR repository for your VM images

# AWS Storage Gateway
Connects an on-premises software appliance with cloud-based storage to provide
seamless integration with data security features between on-prem and AWS storage
infrastructure.

Offers file-based, volume-based, and tape-based solutions:
**File Gateway:** Supports a file interface into S3 and combines a service and a virtual software appliance.
By using this solution you can store and retrieve objects in S3 using standard file protocols such as NFS 
& SMB. The software appliance is deployed into an on-prem environment as a VM and the gateway provides access 
to S3 objects as files or file share mount points. Using file gateway you get:
* Retrieve & store files using NFS version 3 or protocol 4.1
* Retrieve & store files using SMB version 2 and protocol 3
* Access data directly from AWS
* Manage data using S3 lifecycle policies

A file gateway simplifies file storage in Amazon S3, integrates to existing applications through industry-standard
file system protocols, and provides a cost-effective alternative to on-premises storage. It also provides 
low-latency access to data through transparent local caching. A file gateway manages data transfer to and from AWS,
buffers applications from network congestion, optimizes and streams data in parallel, and manages bandwidth consumption.

**Volume Gateway:** A volume gateway provides cloud-backed storage volumes that you can mount as Internet Small Computer 
System Interface (iSCSI) devices from your on-premises application servers. The volume gateway is deployed into your 
on-premises environment as a VM running on VMware ESXi, KVM, or Microsoft Hyper-V hypervisor. The gateway supports the 
following volume configurations:
* Cached Volumes: Store data in S3 and retain a copy of frequently accessed data subsets locally.
* Stored Volumes: If you need low-latency access to your entire dataset, first configure your on-premises gateway
 to store all your data locally. Then asynchronously back up point-in-time snapshots of this data to Amazon S3.
 
**Tape Gateway:** A tape gateway provides cloud-backed virtual tape storage. The tape gateway is deployed into your 
on-premises environment as a VM running on VMware ESXi, KVM, or Microsoft Hyper-V hypervisor. 

With a tape gateway, you can cost-effectively and durably archive backup data in GLACIER or DEEP_ARCHIVE. A tape gateway provides a virtual tape 
infrastructure that scales seamlessly with your business needs and eliminates the operational burden of provisioning, 
scaling, and maintaining a physical tape infrastructure.

You can run AWS Storage Gateway either on-premises as a VM appliance, as a hardware appliance, or in AWS as an Amazon EC2 
instance. You deploy your gateway on an EC2 instance to provision iSCSI storage volumes in AWS. You can use gateways hosted 
on EC2 instances for disaster recovery, data mirroring, and providing storage for applications hosted on Amazon EC2.

# AWS Cloud Adoption Framework

#### Business Perspective: Value Realization
* IT-finance: A common budgeting change involves moving from capital asset expenditures
and maintenance to consumption-based pricing. Can easily track consumption with details which makes it easier to associate costs with results. Easier to implement Charge Back models
* IT Strategy: IT teams will need new skills and processes to be successful in the cloud
* Benefits Realization: TCO & ROI are easier to quantify in the cloud
* Business Risk Management: Moving to the cloud reduces risk and allows for more financial and technical agility

#### People Perspective: Roles and Readiness
* Resource Management: Cloud adoption requires that the staffing teams in your organization acquire
new skills and processes to ensure that they can forecast and staff based on your
organization’s needs.
* Incentive Management: Worker compensation/incentives should be reviewed as cloud roles are more competitive
* Career Management: Employees should have clear career paths in the cloud
* Training Management: Provide training to current employees on the cloud
* Organizational Change Management: Have a centralized process for informing the company of changes 

#### Governance Perspective: Prioritization and Control
* Portfolio Management: Organizations need to be able to prioritize which projects are eligible for cloud migration
* Program and Project Management: Orgs need to be able to manage multiple projects and be more agile (waterfall methods usually don't work)
* Business Performance Management: With the ability to optimize and automate more tasks KPIs should be re-calculated
* License Management: Need new skills to manage licenses in the cloud

#### Platform Perspective: Applications and Infrastructure
New skills are needed because the administration of infrastructure in the cloud 
is much different than in person

### Security Perspective: Risk and Compliance
* Identity and Access Management: AWS comes with multiple access control mechanisms
* Detective Control: AWS provides native logging to provide realtime insights into your environment
* Infrastructure Security: The cloud allows security controls to become more agile and automated
* Data Protection: Maintain visibility and control of your data
* Incident Response: AWS & independent vendors provide an array of solutions when responding to incidents

#### Operations Perspective: Manage and Scale
* Service Monitoring: Address and detect issues with automation for greater uptime
* Application Performance Monitoring: Teams will need new skills to properly monitor and manage applications in the cloud
* Resource Inventory Management: Licensing and hardware management becomes simpler in the cloud
* Release/Change Management: The cloud makes it easy to deploy and rollback changes
* Reporting and Analytics: The cloud allows for more detailed analytics and reporting

# Application Service Discovery
Helps plan cloud migrations by collecting usage and config data about on-prem servers. Application Auto Discovery is built in 
and integrated with AWS Migration Hub to simplify tracking the migration status of assets.

#### Application Discovery Service
* **Agentless discovery:** AWS Agentless Discovery Connector (OVA file) is deployed through your VMware vCenter. once configured it can 
discover VMs and hosts associated with vCenter. From there it can discover servers names, IPs, and metrics around CPU, RAM, & disk. (Only works for VMware vCenter)
* **Agent-based discovery:** Deploy the AWS Application Discovery Agent on each VM and physical server. The agent collects config data
& performance metrics.

# Cloud Migration Strategies
* **Rehosting:** Also known as a "lift-and-shift" is what many early cloud projects gravitate towards. Most rehosting can be automated with tools,
although some customers will choose to do it manually to better understand their applications. This is also a good choice because it is easier
to re-architect solutions once they're already in the cloud.
* **Replatforming:** Also known as a "lift-tinker-and-shift", this involves making some slight optimizations for the cloud but otherwise not changing
the core architecture of the application. Examples could be moving a DB to RDS or moving the application to a fully managed service like Elastic Beanstalk.
* **Repurchasing:**: Moving to a different product, such as moving a CRM system over to salesforce.com
* **Refactoring/Re-architecting:** Re-architect the application to use cloud native features. Typically this is drive by a strong business need to 
new features, scale, or performance that couldn't be achived in the current environment. Examples could be moving a monolith to serverless 
microservices.
* **Retire:**: Get rid of the application, if you no longer need it.
* **Retain:** Do nothing for now and revisit in the future

# RDS

#### Microsoft SQL Server
* Multi-AZ: To create a multi-az SQL server choose **Yes** for the **Mirroring/Always On** option

# Ops Works
AWS OpsWorks is a configuration management service that helps you configure and operate applications in the cloud using Puppet or Chef.

#### OpsWorks for Puppet Enterprise
* Lets you create AWS-managed Puppet master servers
* Master servers manage nodes in your infrastructure and stores facts about those nodes
* Allows you to automate how nodes are configured, deployed, and managed in EC2 or on prem

#### OpsWorks for Chef Automate
* Lets you create AWS-managed Chef servers that include Chef Automate premium features and use Chef to manage them
* Can run cookbooks across nodes

#### OpsWorks Stacks
* Provides a simple and flexible way to manage stacks and applications. For example a web application (stack) with app servers, db servers, load balancers, and other resources.
* OpsWorks Stacks doesn't require Chef servers; OpsWorks Stacks performs some of the work for you by monitoring instance health, provisioning new instances when necessary, by using Auto Healing and Auto Scaling.
* OpsWorks Stacks layers will help provision AWS Elastic Load Balancers, EC2 instances, RDS instances, ECS clusters, and custom resources
* OpsWorks Stacks are made up of layers 
* OpsWorks Stacks also allows autoscaling to be setup based on CPU or Memory usage

# Elastic Load Balancing

#### Availability Zones and Load Balancer Nodes
When enabling and availability zone for a load balancer, the load balancer creates a node in that availability zone. If you
register targets in an availability zone but do not enable the availability zone, these targets do not receive traffic.

#### Cross Zone Load Balancing
The nodes for the load balancer distribute requests from clients to registered targets. When cross zone load balancing is enabled
each load balancer node distributes traffic across the registered targets in all enabled AZs. When it is disables, each load balancer 
node distributes traffic only across the registered targets in its AZ.

#### Security
* Load balancers offer private VPC endpoints

# EFS
Fully managed and distributed NFS file system for use in AWS and on-prem resources. Can scale to petabytes and grows and shrinks automatically.
Supports NFS version 4 (NFSv4.1 & NFSv4.0) protocol.
* Can mount EFS into on-premise data centers using AWS Direct Connect or VPN

#### Security & Networking
* EFS allows you to control access using Portable Operating System Interface (POSIX) permissions
* EFS mount targets associated with the file system live in security groups. NFS communicates on port 2049!!!

#### Encryption
* EFS supports authentication, authorization, and encryption capabilities. Two forms of encryption are supported, encryption in transit and encryption at rest.
* When encryption at rest is enabled all data & metadata is encrypted
* Data encryption in transit can be enabled when the file system is mounted
* NFS client access to EFS is controlled by both IAM and network security policies

#### Provisioned Modes
* **General Purpose:** This mode is ideal for latency-sensitive use cases, like web serves, content management systems, home directories, and general file serving.
* **Max I/O Mode:** Can scale to higher levels of aggregate throughput and operations per second with the trade of of slightly higher latencies for file metadata operations
* **Default Bursting Throughput Mode:** Scales as the file system grows
* **Provisioned Throughput Mode:** Specify the throughput of the file system independent of the amount of data stored

#### Quotas & Limits
* EFS with Windows is not supported

# Elasticsearch
Also known as (ES) is a managed service that makes it easy to deploy, operate, and scale Elasticsearch clusters in AWS. ES will
automatically detect and replace failing nodes.

#### Features
* Up to 3PB of attached storage
* Cognito, Basic or SAML (for Kibana) authentication
* Audit logs
* Node allocation across two or three AZs
* Dedicated master node 
* Automated snapshots
* Integration with BI applications
* Integration with S3 Kinesis, DynamoDB for streaming data into ES

#### Security
* Manual snapshots are not automatically encrypted at rest, the S3 bucket that they are stored in must also be encrypted for them to be encrypted.
* Each ES domain resides in its own VPC, this prevents potential attackers from intercepting traffic between ES nodes and keeps the cluster secure.

# Route53

#### Choosing a Routing Policy
* Latency Based Routing: If your application is hosted in multiple regions, you can improve performance for your users by serving their requests from the region that provides the lowest latency
* Multivalue Answer Routing: Allows you to configure Route53 to return multiple values such as Ip addresses to web servers. With this you can also check the health of each resource, so Route53 only returns healthy resource values.
* Weighted Routing: Allows you to associate multiple resources with a single domain and choose how much traffic is routed to each resource. Allows you to send x% to one resource and y% to another.
* Geoproximity Routing: Routes users to the nearest location when the user's browser supports it.  

#### Health Checks and DNS Failover
* In a basic setup Route53 will be configured with multiple weighted records and then configure health checks for each of the corresponding resources.
* In a more complex config you might create a tree of records and route based on multiple criteria. For example if latency is important you might:
    1. Use latency alias records to route traffic to the region with the best latency
    1. Then the region records might have weighted records in each region as the target
    1. After that the weighted records may route traffic to EC2 instances based on instance type or health

# Service Catalog
Enables organizations to create and manage catalogs of IT services that are approved for AWS. These can include VMs, servers, software, databases, and 
more complete multi-tier architectures. 

#### Benefits
* Standardization: Only approved assets can be launched within the entire organization
* Self-service discovery and launch: Users are able to brows a listing of products that they have access to and are able to provision
* Fine-grain access control: Administer and assemble portfolios of products from their catalog, add constraints onf tags, and grant access to the portfolio via IAM
* Extensibility and version control: Can produce any number of portfolios and restrict it w/o creating another copy. Updating products to a new version propagates the update to all products in the portfolio.  

#### Management
* Add template constraints to limit instance sizes
* Grant templates IAM roles for the template to assume when deploying. i.e. end users don't need permissions to run CloudFormation or start an EC2 instance to 
 launch a template that creates an EC2 instance.
* Constrain what tags are required on the created resource

# SQS
* Messages are not automatically deleted after they've been received, that needs to be done via a separate API call
* Purging a queue deletes all messages from it
* Visibility timeout: How long it takes for a message to re-appear in the queue if it's been retrieved but hasn't been deleted.
    * e.g. if your application requires 10 seconds to process a message but you set the visibility timeout to only 2 seconds, a duplicate message is received by another consumer while the original consumer is still working on the message
* Batch message actions to reduce costs
* Long polling allows you to consume messages from SQS as soon as they become available
    * Reduces costs because there are less empty recieves
    * Preferred over short polling in most cases
* Short polling returns responses immediately, even if the polled SQS queue is empty 
* FIFO queues can have duplicate data, use the message id to de-dupe
  
# WAF, Shield, and Firewall Manager

#### WAF
Web application firewall that lets you monitor HTTP and HTTPS requests in front of CloudFront, API Gateway, Load Balancers, and AWS App Sync. It allows the following behaviors:
* Allow all requests except for x
* Block all requests except for x
* Only allow requests that match x

#### Shield
You can use WAF web ACLs to minimize the effects of DDoS attacks. For additional DDoS protection AWS Shield & Shield Advanced can protect EC2 ELBs, CloudFront, Route53, and Global Accelerator accelerators.

#### AWS Firewall Manager
 AWS Firewall Manager simplifies your administration and maintenance tasks across multiple accounts and resources for AWS WAF rules, AWS Shield Advanced protections, and Amazon VPC security groups. 
 The Firewall Manager service automatically applies your rules and other security protections across your accounts and resources, even as you add new accounts and resources.

# EBS

#### Initializing Volumes
While initializing Provisioned IOPS SSD volumes that were created from snapshots, the performance of the volume may drop below 50 percent of its expected level, 
which causes the volume to display a warning state in the I/O Performance status check. This is expected, and you can ignore the warning state on Provisioned IOPS 
SSD volumes while you are initializing them.

# DMS

#### Parameters
* MaxFullLoadSubTasks (defaults to 8): Determines the number of tables that can be transferred in parallel during a full load
* ParallelLoadThreads (2-32 threads per table during full load): Determines the number of threads that can be allocated for a given table for the parallel transfer of data. 

# AWS Single Sign-On
AWS Single Sign-On is a cloud-based single sign-on (SSO) service that makes it easy to centrally manage SSO access to all of 
your AWS accounts and cloud applications. Specifically, it helps you manage SSO access and user permissions across all your AWS accounts in AWS Organizations.

#### Features
* Integrates with AWS organizations
* SSO access to AWS accounts and cloud applications
* Create ana manage users and groups

# AWS Organizations
AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization 
that you create and centrally manage. AWS Organizations includes account management and consolidated billing capabilities that 
enable you to better meet the budgetary, security, and compliance needs of your business. As an administrator of an organization, 
you can create accounts in your organization and invite existing accounts to join the organization.

#### Features
* **Centralized and management all AWS accounts:** Combine existing accounts into an organization and create accounts that are 
automatically part of the organization.
* **Consolidated billing for all member accounts:** Use the management account to consolidate billing across all accounts and take advantage of bulk discounts
* **Hierarchical grouping of your accounts to meet your budgetary, security, or compliance needs:** You can group accounts into organizational units (OUs) and
attach different access policies to each OU. For example you could group HIPAA accounts into one OU and then attach a policy that blocks usage of non HIPAA 
compliant resources.
* **Policies to centralize control over the AWS services and API actions that each account can access:** As an admin of the management account for the organizations,
you can user service control policies (SCPs) to specify the maximum permissions for member accounts in the organization. In SCPs you can restrict which AWS services,
resources, and API actions can be taken. These restrictions even override the admins of the member accounts in the organizations. 
* **Policies to standardize tags across the resources in your organization's accounts:** You can use tag policies to maintain consistent tags, including preferred case treatment
of tag keys and values.
* **Policies that configure automatic backups for the resources in your organization's accounts:** Can configure policies to apply AWS backup plans across all accounts
* **Integration and support for AWS Identity and Access Management (IAM):** Use IAM to provide granular control over users and roles in individual accounts. This allows 
you to set policies that will restrict access to only resources and actions that are allowed by the AWS Organization policies and IAM policies.
* **Integration with other AWS services:** Master organization accounts are able to create service linked roles in all organization member accounts to preform tasks across accounts.

#### Allow vs. Deny List
* Allow list strategy: You explicitly specify the access that is allowed. All other access is implicitly blocked. By default, AWS Organizations attaches an AWS managed policy called FullAWSAccess to all roots, OUs, and accounts.
* Deny list strategy: You explicitly specify the access that is not allowed. All other access is allowed. In this scenario, all permissions are allowed unless explicitly blocked. This is the default behavior of AWS Organizations. By default, AWS Organizations attaches an AWS managed policy called FullAWSAccess to all roots, OUs, and accounts. This allows any account to access any service or operation with no AWS Organizations–imposed restrictions.
* SCPs merely provide guardrails for what is and isn't allowed to happen in an account. To grant actual permissions IAM roles or users must be created in the member account.

# Cost and Usage Report
The AWS Cost and Usage Reports (AWS CUR) contain the most comprehensive set of cost and usage data available. After setting 
up a Cost and Usage Report, the current month’s billing data will be delivered to an Amazon S3 bucket that you designate during 
set-up. You can receive hourly, daily or monthly reports that break out your costs by product or resource and by tags that 
you define yourself. AWS updates the report in your bucket at least once per day. After setting up a Cost and Usage Report,
you will receive the current month’s billing data and daily updates in the same Amazon S3 bucket.

Reports can either be downloaded, queried using Athena, or imported into redshift or Quicksight.

# Well Architected Framework

#### Operational Excellence Pillar
The operational excellence pillar focuses on running and monitoring systems to deliver business value, and continually improving processes and procedures. Key topics include automating changes, responding to events, and defining standards to manage daily operations.

Principals:
* Perform operations as code
* Make frequent, small, reversible changes
* Refine operations procedures frequently
* Anticipate failure
* Learn from all operational failures

#### Security Pillar
The security pillar focuses on protecting information and systems. Key topics include confidentiality and integrity of data, identifying and managing who can do what with privilege management, protecting systems, and establishing controls to detect security events.

Principals:
* Implement a strong identity foundation
* Enable traceability
* Apply security at all layers
* Automate security best practices
* Protect data in transit and at rest
* Keep people away from data
* Prepare for security events

#### Reliability Pillar
The reliability pillar focuses on ensuring a workload performs its intended function correctly and consistently when it’s expected to. A resilient workload quickly recovers from failures to meet business and customer demand. Key topics include distributed system design, recovery planning, and how to handle change.

Principals:
* Automatically recover from failure
* Test recovery procedures
* Scale horizontally to increase aggregate workload availability
* Stop guessing capacity
* Manage change in automation

#### Performance Efficiency Pillar
The performance efficiency pillar focuses on using IT and computing resources efficiently. Key topics include selecting the right resource types and sizes based on workload requirements, monitoring performance, and making informed decisions to maintain efficiency as business needs evolve.

Principals:
* Democratize advanced technologies: Make advanced technology implementation easier for your team 
* Go global in minutes
* Use serverless architectures
* Experiment more often
* Consider mechanical sympathy

#### Cost Optimization Pillar
The cost optimization pillar focuses on avoiding unnecessary costs. Key topics include understanding and controlling where money is being spent, selecting the most appropriate and right number of resource types, analyzing spend over time, and scaling to meet business needs without overspending.

Principals:
* Implement cloud financial management
* Adopt a consumption model
* Measure overall efficiency
* Stop spending money on undifferentiated heavy lifting:
* Analyze and attribute expenditure

# Transit Gateway
AWS Transit Gateway connects VPCs and on-premises networks through a central hub. This simplifies your network and puts an end to complex peering relationships. It acts as a cloud router – each new connection is only made once.

As you expand globally, inter-Region peering connects AWS Transit Gateways together using the AWS global network. Your data is automatically encrypted, and never travels over the public internet. And, because of its central position, AWS Transit Gateway Network Manager has a unique view over your entire network, even connecting to Software-Defined Wide Area Network (SD-WAN) devices.

# EC2

#### Reserved Instances
Reserved Instances provide you with significant savings on your Amazon EC2 costs compared to On-Demand Instance pricing. Reserved Instances are not physical instances, but rather a billing discount applied to the use of On-Demand Instances in your account. These On-Demand Instances must match certain attributes, such as instance type and Region, in order to benefit from the billing discount.

Savings Plans also offer significant savings on your Amazon EC2 costs compared to On-Demand Instance pricing. With Savings Plans, you make a commitment to a consistent usage amount, measured in USD per hour. This provides you with the flexibility to use the instance configurations that best meet your needs and continue to save money, instead of making a commitment to a specific instance configuration. For more information, see the AWS Savings Plans User Guide.

**Instance Attributes**
* Instance type
* Region
* Tenancy
* Platform

**Term Commitment**
* One year 
* Three year

**Payment Options**
* All Upfront: full payment is made for the entire term
* Partial Upfront: A portion of the term is paid upfront and the remaining hours are billed at a discounted hourly rate
* No Upfront: Billed an hourly rate for every hour within the term

**Offering Class**
* Standard: provide the most significant discount but can only be modified. Standard Reserved Instances can't be exchanged.
* Convertible: Provide a lower discount rate than standard, ut can be exchanged for another convertible instance with different attributes.

Note: You cannot purchase schedule reserved instances!

#### Dedicated Hosts
An Amazon EC2 Dedicated Host is a physical server with EC2 instance capacity fully dedicated to your use.

#### Dedicated Instances
Dedicated Instances are Amazon EC2 instances that run in a virtual private cloud (VPC) on hardware that's dedicated to a single customer. Dedicated Instances that belong to different AWS accounts are physically isolated at a hardware level, even if those accounts are linked to a single payer account. 

#### On Demand Capacity Reservations
On-Demand Capacity Reservations enable you to reserve capacity for your Amazon EC2 instances in a specific Availability Zone for any duration. This gives you the ability to create and manage Capacity Reservations independently from the billing discounts offered by Savings Plans or regional Reserved Instances. By creating Capacity Reservations, you ensure that you always have access to EC2 capacity when you need it, for as long as you need it. 

When you create a Capacity Reservation, you specify:
* The Availability Zone in which to reserve the capacity
* The number of instances for which to reserve capacity
* The instance attributes, including the instance type, tenancy, and platform/OS

Capacity Reservations can only be used by instances that match their attributes. By default, they are automatically used by running instances that match the attributes. If you don't have any running instances that match the attributes of the Capacity Reservation, it remains unused until you launch an instance with matching attributes.

In addition, you can use Savings Plans and regional Reserved Instances with your Capacity Reservations to benefit from billing discounts. AWS automatically applies your discount when the attributes of a Capacity Reservation match the attributes of a Savings Plan or regional Reserved Instance. For more information, see Billing discounts.

# Billing and Cost Management
AWS Billing and Cost Management is the service that you use to pay your AWS bill, monitor your usage, and analyze and control your costs.

AWS automatically charges the credit card that you provided when you signed up for a new account with AWS. Charges appear on your monthly credit card bill. You can view or update your credit card information, including designating a different credit card for AWS to charge, on the Payment Methods page in the Billing and Cost Management console. AWS Billing and Cost Management provides useful tools to help you gather information related to your cost and usage, analyze your cost drivers and usage trends, and take action to budget your spending.

#### Features
* **Analyzing Costs with Cost Explorer:** Cost explorer tool to view AWS cost data as a graph. Allows graphs to be filtered by service, AZ, API, tag, instance type, purchase option, usage type, and more.
* **AWS Budgets:** You can use AWS Budgets to track your AWS usage and costs. Budgets use the cost visualization provided by Cost Explorer to show you the status of your budgets. This provides forecasts of your estimated costs and tracks your AWS usage, including your free tier usage. You can also use budgets to create Amazon Simple Notification Service (Amazon SNS) notifications that tell you when you go over your budgeted amounts, or when your estimated costs exceed your budgets.


# Random Architectures

#### Serverless Data Integrity Checks
Compute the objects checksum and attach it as metadata when uploading it to S3. Once the object is uploaded to S3 
trigger a Lambda to compute the checksum and compare it against the checksum in the S3 objects metadata.


