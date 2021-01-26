# Business Continuity

## Concepts

#### Terms
* Business Continuity (BC): Seeks to minimize business activity disruption when something unexpected happens
* Disaster Recovery (DR): Act of responding to an event that threatens business continuity
* High Availability (HA): Designing for redundancies to reduce the chance of impacting service levels
* Fault Tolerance: Designing in the ability to absorb problems without impacting service levels.
* Service Level Agreement (SLA): An agreed goal or target for a given service on its performance or availability.
* Recovery Time Objective (RTO): Time that it takes after a disruption to restore business process to their service levels.
* Recovery Point Objective (RPO): Acceptable amount of data loss measured in time.

#### Disaster Categories
| Category | Example |
| -------- | ------- |
| Hardware Failure | Network switch power supply fails and brings down LAN |
| Deployment Failure | Deploying a patch that breaks an ERP business process |
| Load Induced | Distributed denial of service attack on your website |
| Data Induced | Ariane 5 rocket explosion on June4, 1996 |
| Credential Expiration | An SSL/TLS certificate expires on your site |
| Dependency | S3 subsystem failure cause numerous other AWS service failures |
| Infrastructure | A construction crew accidentally cuts a fiber optic data line |
| Identifier Exhaustion | We currently do not have sufficient capacity in the AZ you requested |


## AWS Continuum of HA

#### Backup & Restore
Pros:
* Very common entry point into AWS
* Minimal effort to configure

Cons:
* Least flexible
* Analogous to off-sire backup storage

#### Pilot Light
Pros:
* Cost effective way to maintain a "hot site" concept 
* Suitable for a variety of landscapes and applications

Cons:
* Usually requires manual intervention for failover
* Spinning up cloud environments will take minutes or hours
* Must keep AMIs update to date with on-prem counterparts

#### Warm Standby
Pros:
* All services are up and ready to accept a failover faster within minutes or seconds
* Can be use as a "shadow environment" for testing or production staging

Cons:
* Resources would need to be scaled to accept production load 
* Still requires some environment adjustments but could be scripted

#### Multi-Site
Pros:
* Ready all the time to take full production load - effectively a mirrored data center
* Fails over in seconds or less
* No or little intervention required to fail over

Cons:
* Most expensive DR option
* Can be perceived as wasteful as you have resources just standing around waiting for the primary to fail


## Storage HA Options

#### EBS Volumes
* Annual failure rate less than 0.2% compared to commodity hard drive at 4% so give 1000 EBS volumes, expect 2 to fail per year
* Availability rate of 99.999%
* Replicated automatically within a single AZ
* Vulnerable to AZ failure. Plan accordingly.
* Easy to snapshot, which is stored on S3 and multi-AZ durable
* You can copy snapshots to other regions as well
* Supports RAID configurations

#### RAID Configurations
| What | RAID0 | RAID1 | RAID5 | RAID6 |
| ---- | ----- | ----- | ----- | ----- |
| Redundancy | None | 1 drive can fail | 1 drive can fail | 2 drives can fail |
| Reads | 4/5 | 3/5 | 4/5 | 4/5 |
| Writes | 4/5 | 3/5 | 2/5 | 1/5 |
| Capacity | 100% | 50% | (n-1)/n | (n-2)/n |
 
 RAID 5 & 6 are not recommended in AWS
 
 #### RAID IOPS and Throughput
 | RAID | Volume Size | Provisioned IOPS | Total Volume IOPS | Usable Space | Throughput |
 | ---- | ----------- | ---------------- | ----------------- | ------------ | ---------- |
 | No RAID | (1) 1000 GB | 4000 | 4000 | 1000 GB | 500 MB/s |
 | RAID0 | (2) 500 GB | 4000 | 8000 | 1000 GB | 1000 MB/s | 
 | RAID1 | (2) 500 GB | 4000 | 4000 | 500 GB | 500 MB/s |
 
 #### S3 Storage 
 * Standard Storage Class (99.99% availability = 52.6 minutes / year)
 * Standard Infrequent Access (99.9% availability = 8.76 hours / year)
 * One-zone Infrequent Access (99.5% availability = 1.83 days / year)
 * Eleven 9s of durability (99.999999999%)
 * Standard & Standard-AZ have multi-AZ durability; One-zone only has single AZ durability
 * Backing service for EBS snapshots and many other AWS services

#### Amazon EFS
* Implementation of the NFS file system
* True file system as opposed to block storage (EBS) or object storage (S3)
* File locking, strong consistency, concurrently accessible
* Each file object and metadata is stored across multiple AZs
* Can be accessed from all AZs concurrently
* Mount targets are highly available


## Compute HA Options

#### HA Approaches for Compute
* Up to date AMIs are critical for rapid fail-over
* AMIs can be copied to other regions for safety or DR staging
* Horizontally scalable architectures are preferred because risk can be spread across multiple smaller machines versus one large machine
* Reserved instances is the only way to guarantee that resources will be available when needed
* Auto Scaling and Elastic Load Balancing work together to provide automated recovery by maintaining minumum instances

## Database HA Options

#### HA Approaches for Databases
* If possible, choose DynamoDB over RDS because of inherent fault tolerance 
* If DynamoDB can't be used, choose Aurora because redundancy and automatic recovery features
* If Aurora isn't available, choose multi-AZ RDS
* Frequent RDS snapshots can protect against data corruption or failure and they won't impact performance of multi-AZ deployment
* Regional replication is also an option, but will not be strongly consistent
* If database is on EC2, you're on your own

#### HA Notes for Redshift
* Currently Redshift doesn't support multi-AZ deployments
* Best HA option is to use a multi-node cluster which support data replication and node recovery
* A single node Redshift cluster does not support data replication and you'll have to restore from a snapshot on S3 if a drive fails

#### HA Notes for ElastiCache
Memcached
* Because Memcached doesn't support replication a node failure will result in data loss
* Use multiple nodes in each shard to minimize data loss on doe failure
* Launch multiple nodes across available AZs to minimize data loss on AZ failure

Redis
* Use multiple nodes in each shard and distribute the nodes across multiple AZs
* Enable multi-AZ on the replication group to permit automatic failover if the primary node fails
* Schedule regular backups of your Redis cluster


## Network HA Options
*  By creating subnets in the available SZs, you can create multi-AZ presence for your VPC
* Best practice is to create at least two VPN tunnels in your Virtual Private Gateway
* Direct Connect is not HA by default, so you need to establish a secondary connection via another Direct Connect (ideally with another provider) or use a VPN
* Route 53's health checks provide a basic level of redirecting DNS resolutions.
* Elastic IPs allow you flexibility to change out backing assets without impacting name resolution.
* For multi-AZ redundancy of NAT gateways, create NAT gateways in each AZ with routes for private subnets to use the local Gateway


## Exam Tips
General Concepts
* Know the difference between Business Continuity, Disaster Recovery, and Service Levels
* Know the difference between High Availability and Fault Tolerance
* Understand the inter-relationships and how AWS uses the terms
* Know the difference between RTO and RPO
* Know the four general types of DR architectures and trade-offs of each

Storage Options
* Understand the HA capabilities and limitations of AWS storage options
* Know when to use each storage option to achieve the required level of recovery capability
* Understand RAID and the potential benefits and limitations

Compute Options
* Understand why horizontal scaling is preferred from an HA perspective
* Know that compute resources are finite in an AZ and know how to guarantee their availability
* Understand how Auto Scaling and ELB can contribute to HA

Database Options
* Know the HA attributes of the various database services
* Understand the different HA approaches and risks for Memcached and Redis
* Know which RDS options require manual failover and which are automatic

Network Options
* Know which networking components are not redundant across AZs and how to architect for then to be redundant
* Understand the capabilities of Route 52 and Elastic IP in context of HA

White Papers
* [Backup and Recovery Approaches Using AWS](https://d1.awsstatic.com/whitepapers/Storage/Backup_and_Recovery_Approaches_Using_AWS.pdf)
* [Getting Started with Amazon Aurora](https://d1.awsstatic.com/whitepapers/getting-started-with-amazon-aurora.pdf)
* [AWS Reliability Pillar: AWS Well Architected Framework](https://d1.awsstatic.com/whitepapers/architecture/AWS-Reliability-Pillar.pdf)
* [Re:Invent Models of Availability](https://www.youtube.com/watch?v=xc_PZ5OPXcc&ab_channel=AmazonWebServices)
* [Re:Invent How to Design a Multi-Region Active Active Architecture](https://www.youtube.com/watch?v=RMrfzR4zyM4&ab_channel=AmazonWebServices)
* [Re:Invent Disaster Recovery with AWS: Tiered Approaches to Balance Cost with Recovery Objectives](https://www.youtube.com/watch?v=a7EMou07hRc&ab_channel=AmazonWebServices)


## Pro Tips

#### Failure Mode and Effects Analysis
Failure Mode and Effects Analysis (FMEA): A systematic process to examine
1. What could go wrong
2. What impact it might have
3. What is the likelihood of it occurring
4. What is our ability to detect and react

Severity * Probability * Detection = Risk Priority Number

#### Step 1 - Round up Possible Failures
| What | Failure Mode | Cause | Current Controls |
| ---- | ------------ | ----- | ---------------- | 
| Invoicing | Pricing Unavailable | Retail price incorrect in ERP system | Master data maintenance audit report |
| Invoicing | Pricing Incorrect | Retail price not assigned in ERP system | None |
| Invoicing | Slow to build invoice | Invoicing system is slow | None |
| Invoicing | Unable to build invoice | Invoicing system is offline | Uptime monitor |

#### Step 2 - Assign Scores
| What | Failure Mode | Customer Impact | Likelihood | Detect and React | Risk Number Priority |
| ---- | ------------ | --------------- | ---------- | ---------------- | -------------------- |
| Invoicing | Pricing Unavailable | 7 | 3 | 2 | 42 |
| Invoicing | Pricing Incorrect | 8 | 3 | 9 | 216 |
| Invoicing | Slow to build Invoice | 5 | 2  | 9 | 90 |
| Invoicing | Unable to build Invoice | 8 | 3 | 2 | 48 |
 
 
 ## Challenges
 * Question 1:
    - My Answer: A
    - Correct Answer: A 
    
* Question 2:
    - My Answer: A, C, G
    - Correct Answer: A, D, E, G