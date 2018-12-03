# Elasticity & Scalability

## Elasticity & Scalability 101

#### What is elasticity?
* Think about it as a rubber band. Elasticity allows you to stretch out and 
retract your infrastructure, based on your demand.
* Under this model you only pay for what you need
* Elasticity is used during a short time period such as hours or days

#### What is scalability?
* Scalability is used to talk about building out the infrastructure to meet your
demands long term.
* Scalability is used over longer time periods such as weeks, days, months, years

#### AWS Services
EC2
* Scalability: Increase instances sizes as required using reserved instances
* Elasticity: Increase the number osf EC2 instances, based on autoscaling

DynamoDB
* Scalability: Unlimited amount of storage
* Elasticity: Increase additional IOPS for additional traffic spikes.

RDS
* Scalability: Increase the size of DB
* Elasticity: not very elastic, can't scale RDS based on demand

Aurora
* Scalability: Modify the instance type
* Elasticity: Aurora serverless

#### Exam Tips
* Elasticity: short term, scale with demand
* Scalability: long term, scale out infrastructure

## RDS Multi-AZ Failover

#### RDS Multi-AZ 101
Multi -AZ keeps a copy of your production db in a separate AZ in case of a failure
or disaster. AWS manage the failure from one AZ to another automatically.

Used only for disaster recovery, not for improved performance.

AWS handles the replication for your, so when your db is written to this write is
automatically synced to the standby db. In the event of a planned DB maintenance,
db instance failure, or an AZ failure, RDS will automatically failover to the 
standby DB do that database operations can resume quickly.

Outage only takes a minute.

For MySQL, Oracle, and PostgreSQL engines utilize synchronous physical replication 
to keep data on the standby up to date with the primary.

For SQL Server engine use synchronous logical replication to achieve the same result,
employing SQL Server-native Mirroring technology.

Both approaches safeguard your data in the event of a DB instance failure or loss
of an AZ.

#### RDS Multi-AZ Failover Advantages
* High availability
* Backups are taken from secondary which avoids I/O suspension to the primary
* Restores are taken fro secondary which avoids I/O suspension to the primary
* You can force a failover from one AZ to the other by rebooting the db instance

#### Exam Tips
* Failover isn't a scaling solution
* Amazon handles failover
* Backups and restore are taken from secondary
* Read replicas are used to scale
* Can for failover by rebooting db

## RDS Read Replicas

#### What are Read Replicas?
Make it easier to take advantage of supported engines' built in replication 
functionality to elastically scale out beyond the capacity constraints of a 
single DB instance for read heavy workloads.

You can create a read replica with a few clicks in the console or by using the 
API. Once the read replica is created, DB updates on the source DB instance will be
replicated using ta supported engine's native async replication. You can create 
multiple read replicas for a given source DB instance and distribute the traffic
among them.

#### When to Use Read Replicas
Scaling beyond the compute or I/O capacity of a single DB instance for read
heavy DB workloads. This excess read traffic can be directed to one or more Read
replicas.

Serving read traffic while the source DB is unavailable. You can direct traffic to
read replica if source DB is doing a backup or something similar.

#### When Would You Use Read Replicas?
* Business reporting or data warehousing scenarios; you may want business reporting
queries to run against read replicas, rather than your primary, prod DB instance.

#### Supported Versions
* MySQL
* PostgreSQL
* MariaDB
* Aurora

#### Creating Read Replicas
When creating a new Read Replica, AWS will take a snapshot of your DB

If multi-az is not enabled:
* This snapshot will be of your primary database and can cause brief I/O
suspension for around 1 min

If multi-az is enabled:
* This snapshot will be of your secondary and you will not experience any 
performance hits

#### Connecting to Read Replica
When a new read replica is created you will be able to connect to it using a 
DNS endpoint

#### Read Replicas Can Be Promoted
You can promote read replicas to be their own stand alone DBs

#### Exam Tips
* You can have up to 5 read replicas
* Replicas can be in multiple regions
* Replication is async
* Read replicas can be built off multi-az databases
* Read replicas can be multi-az
* You can have read replicas of read replicas (beware of latency)
* DB snapshots and backups cannot be taken of read replicas
* Ket metric to look for is REPLICA LAG
* Know the difference between read replicas and multi-az

## Elasticache

#### What is Elasticache
 A web service that makes it easy to deploy, operate, and scale an in memory
cache in the cloud. The service improves the performance of web applications
by allowing you to retrieve information from fast, managed, in memory caches,
instead of relying entirely on slower disk based databases.

Can be used to improve latency & throughput for many read-heavy workloads, or
compute heavy workloads

Caching improves application speed by storing critical pieces of data in memory
for low latency access. Cached infor may include the results of I/O intensive db
queries or results of computationally intensive calculations.

#### Types of Elasticache
* Memcached:
  - A widely adopted memory object caching system. ElastiCache is protocol compliant
  with Memcached, so popular tools that you use today with existing Memcached
  environments will work seamlessly with the service.  
* Redis:
  - A popular open source in memory KV that supports data structures such as 
  stored sets and lists. ElastiCache supports Master / Slave replication and
  multi-az which can be used to achieve cross AZ redundancy.

#### Exam Tips
If given a scenario where db is under heavy read load, when asked how to 
alleviate this, Elasticache is a good choice. Redshift is a good answer if the 
db is feeling stress because of management running OLAP transactions.

## Aurora 101

#### What is Aurora?
It's a relational db that is MySQL and PostgreSQL compatible. Combines speed and 
availability of highend commercial dbs with the simplicity and cost effectiveness
of open source dbs. Provides up to 5x better read performance for MySQL and 3X for
PostgreSQL.

#### Aurora Scaling
* Starting wirh 10GB, scales in 10GB increments and up to 64 TB
* Compute can scale up to 64vCPUs and 488GiB of memory
* Two copies of your data are in each AZ in a minimum of 3 AZs with a min of 6 copies
* Designed to handle the loss of up to 2 copies of your data with out affecting
db write availability and up to 3 copies w/o affecting read availability
* Storage is self healing. Data block and disks are continuously scanned for errors
and fixed automatically.

#### Aurora Replicas
Two types are available
* Aurora replicas (up to 15)
* MySQL read replicas (up to 15)

#### Aurora 100% CPU Utilization
* Is it writes causing the issue? If so you need to scale up and increase the 
instance size
* If it is reads causing the issue? If you need to add more read replicas

#### Aurora Serverless
Is an on demand, auto-scaling configurations for Aurora where the db will 
automatically start up, shut down, and scale up or down capacity depending on the
application's needs.

You pay on a per second basis for the db capacity you use when the db is active,
and you can migrate between standard and serverless configurations.

#### Exam Tips
* Two types: serverless and non
* Redundancy 2 copies in each az and 3 az's
* Self healing storage
* Aurora 100% CPU handling
* Encryption at rest is turned on by default. Once encryption is turned on, all
read replicas will be encrypted.
* Failover is defined by tiers. The lower the tier, the higher the priority with
tier 0 being the highest priority.
* Cross region replicas create a new aurora cluster in the target region. If the
replication is disrupted, you will need to start over. It's recommended that you
select multi-az deployment to ensure high availability for the target cluster

## Troubleshooting Autoscaling

#### Instances not launching unto Autoscaling groups
Below is a list of things to look for if your instances are not launching to an 
autoscaling group:
* associated key pair doesnt exist
* Security group doesnt exist
* Autoscaling config is not working correctly
* Autoscaling group isn't found
* Instance type specified isn't supported in the AZ
* AZ is no longer available
* Invalid EBS device mapping
* Autoscaling servce os not enabled on your account
* Attempting to attach and EBS block device to an instance-store AMI 
