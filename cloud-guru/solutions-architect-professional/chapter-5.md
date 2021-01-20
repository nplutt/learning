# Migrations

## Migration Strategies
| Migration Strategy | Description | Example |
| ------------------ | ----------- | ------- |
| Re-Host | "Lift and Shift"; simply move assets with no change | Move in-prem MySQL database to EC2 instance |
| Re-Platform | "Lift and Reshape"; move assets but change the underlying platform | Migrate on-prem MySQL database to RDS MySQL |
| Re-Purchase | "Drop and Shop"; Abandon existing and purchase new | Migrate legacy on-prem CRM system to salesforce.com |
| Rearchitect | Redesign application in a cloud native manner | Create a serverless version of legacy application |
| Retire | Get rid of application which are not needed | End of life the label printing app because no-one uses it anymore |
| Retain | "Do nothing option"; Decide to reevaluate at a future date | Good news servers, you'll live to see another day |


## Cloud Adoption Framework

#### TOGAF
* The Open Group Architectural Framework
* Approach for redesigning, planning, implementing and governing enterprise IT architectures
* Started development in 1995
* De facto standard in EA practice
* Favored enterprise architecture framework for most fortune 500 companies
* Enterprise Architecture is not TOGAF
* But TOGAF often fills a vacuum
* Often misunderstood and victim of unreasonable expectations
* Not all practitioners are great practitioners
* TOGAF is not a cookbook
* People take it too literally
* "Architects gonna architect"

#### What is a Framework?
* Is some information to help you egt your mind around a problem
* Is open for localization and interpretation
* Is something you should adapt to your organizational culture
* Is not a perfect step by step recipe to success
* Is not something to hide behind with big words

#### Cloud Adoption Framework
* There's more to cloud adoption than technology
* To fully unlock the potential benefits of a cloud migration a holistic approach must be considerd

Business:
* Creation of a strong business case for cloud adoption
* Business goals are congruent with cloud objectives
* Ability to measure benefits (TCO, ROI)

People:
* Evaluate organizational roles and structures, new skills and process needs and identify gaps
* Incentives and Career Management aligned with evolving roles
* Training options appropriate for learning styles

Governance
* Portfolio Management geared for determining cloud eligibility and priority
* Program and Project management more agile projects
* Align KPI's with newly enabled business capabilities

Platform:
* Resource provisioning can happen with standardization
* Architecture patterns adjusted to leverage cloud-native
* New application development skills and processes enable more agility

Security:
* Identity and access management modes change
* Logging and audit capabilities will evolve
* Shared responsibility model removes some and adds some

Operations:
* Service monitoring has potential to be highly automated
* Performance management can scale as needed
* Business continuity and disaster recovery takes on new methods in the cloud


## Hybrid Architecture
* Hybrid architectures make use of cloud resources along with on-premises resources
* Very common first step as a pilot for cloud migrations
* Infrastructure can augment or simply be extensions of on-prem platforms - VMWare for example
* Ideally, integrations are loosely coupled - meaning each end can exist without extensive knowledge of the other side

Storage Gateway:
* Storage Gateway creates a bridge between on-prem and AWS
* Seamless to end users
* Common first step into the cloud due to low risk and appealing economics

On-Prem ERP System:
* Middleware often a great way to leverage cloud services
* Loosely coupled canonical based


## Migration Tools

#### Server Migration Service
* Automates migration of on-premises VMware vSphere or Microsoft Hyper-V/SCVMM virtual machines to AWS
* Replicates VMs to AWS, syncing volumes and creating periodic AMIs
* Minimizes cutover downtime by syncing VMs incementally
* Supports Windows and Linux Vms only
* The Server Migration Connector is downloaded as a virtual appliance into your on-prem vSphere or Hyper-V setup

#### Database Migration Service
* Data Migration Service (DMS) along with Schema Conversion Tool (SCT) helps customers migrate databases to AWS RDS or EC2-based databases
* Schema Conversion Tool can copy database schemas for homogenous migrations (same database) and convert schemas for heterogeneous migrations (different database)
* DMS is used for smalled, simpler conversions and also supports MongoDB and DynamoDB
* SCT used for larger, more complex datasets like data warehourses
* DMS has replication function for on-prem to AWS or to Snowball or S3

#### Application Discovery Center
* Gathers information about on-premises data centers to help in cloud migration planning
* Often customers don't know the full inventory or status of all their data center assets, so this tool helps with that inventory
* Collects config, usage and behavior data for your servers to help in estimating TCO of running on AWS 
* Can run as agent-less or agent-based
* Only supports OSs that AWS supports


## Network Migrations and Cutovers

#### CIDR Reservations
* Ensure your IP addresses will not overlap between VPC and on-prem
* VPCs support IPv4 netmasks range from /16 to /28
    - /16 = 255.255.0.0 = 65,536 addresses
    - /28 = 255.255.255.240 = 16 addresses
* Remember 5 IPs are reserved in every VPC subnet that will take up addresses
    - /28 = 255.255.255.240 -> = 16 addresses -> 14 usable addresses minus 3 reserved in VPC = 11 in VPC

##### Connections
* Most organizations start with a VPN connection to AWS
* As usage grows, they might choose Direct Connect but keep the VPN as a backup
* Transition from VPN to Direct Connect can be relatively seamless using BGP
* Once Direct connect is set-up, configure both VPN and Direct Connect withing the same BGP prefix
* From the AWS side, the Direct Connect path is always preferred...
* ... but you need to be sure the Direct Connect path is the preferref rout from your network to AWS and not VPN (through BGP weighting or static routes)


## Snow Family
* Evolution of AWS Import/Export process
* Move massive amounts of data to and from AWS
* Data transfer as fast or as slow as you're willing to pay a common carrier
* Encrypted at rest

| Option | Info |
| ------ | ---- |
| AWS Import/Export | Ship an external hard drive to AWS. Someone at AWS plugs it in and copies your data to S3. |
| AWS Snowball | Ruggedized NAS in a box AWS ships to you. You copy over up to 80TB of your data and ship it back to AWS. They copy the data over to S3. |
| AWS Snowball Edge | Same as Snowball, but with onboard Lambda and clustering |
| AWS SNowmobile | A literal shipping container full of storage (up to 100PB) and a truck to transport it | 


## Exam Tips
Migration Strategies:
* Understand the different strategies that companies might undertake when deciding if the cloud is right for them
* Understand the typical trade-offs and relative benefits for each strategy

Cloud Adoption Framework:
* Know what a "framework" is and the realistic expectations that should accompany it
* Understand the high level components of the Cloud Adoption Framework
* Most importantly, know that cloud adoption is only partially a technology effort

Hybrid Architectures:
* Be able to speak to some typical hybrid architectures that leverage both on-prem and cloud assets
* Know that VMware has some nifty tools for abstracting workloads across on-prem and cloud, such as the Import plug-in

Migrations:
* Understand the different services and tools available for migrating servers, storage, and databases
* Tool usage specifics won't likely be on the exam, except maybe Storage Gateway

Networking Migration and Cutover:
* Know various hybrid networking architectures 
* Understand that smooth transitions from and to VPN and Direct Connect can be done using BGP routing; abrupt route changes risk downtime.

White Papers:
* [AWS Migration Whitepaper](https://d1.awsstatic.com/whitepapers/Migration/aws-migration-whitepaper.pdf)
* [An Overview of the AWS CLoud Adoption Framework](https://d1.awsstatic.com/whitepapers/aws_cloud_adoption_framework.pdf)
* [Migrating Applications to AWS: Guide and Best Practices](https://d1.awsstatic.com/whitepapers/Migration/migrating-applications-to-aws.pdf)
* [AWS Cloud Transformation Maturity Model](https://d1.awsstatic.com/whitepapers/AWS-Cloud-Transformation-Maturity-Model.pdf)
* [Re:Invent How to Assess Your Organization's Readiness to Migrate at Scale](https://www.youtube.com/watch?v=id-PY0GBHXA&ab_channel=AmazonWebServices)
* [Re:Invent Migrating Databases and Data Warehouses to the Cloud](https://www.youtube.com/watch?v=Y33TviLMBFY&ab_channel=AmazonWebServices)
* [Re:Invent Using Hybrid Storage with AWS Storage Gateway](https://www.youtube.com/watch?v=9wgaV70FeaM)


## Pro Tips
* Technology is often a minor part of a cloud migration project
* Project management discipline is a must - don't underestimate this
* Adapt the Cloud Adoption Framework for your own organizations culture
* Leverage the CAF to get buy in by acknowledging the enterprise nature of cloud migrations
* Be a boundary spanner!


## Challenges
* Question 1:
    - My Answer: A, C, D, E
    - Correct Answer: A, C, D, E

* Question 2:
    - My Answer: C
    - Correct Answer: D
