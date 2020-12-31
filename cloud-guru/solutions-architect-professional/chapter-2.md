# Data Stores

## Concepts

#### Data store types:
* Persistent data store: Data is durable and sticks around after 
reboots, restarts, or power cycles. e.g. Glacier, S3, RDS
* Transient data store: Data is just temporarily stored and passed
along to another process or persistent store. e.g. SQS, SNS
* Ephemeral data store: Data is lost when stopped. e.g. EC2, Memcached

#### IOPS vs. Throughput
Input/Output operations per second (IOPS): Measure of how fast we can 
read and write to a device
Throughput: Measure of hwo much data can be moved at a time

#### Consistency Models - ACID & BASE
ACID:
* Atomic - Transactions are "all or nothing"
* Consistent - Transactions must be valid
* Isolated - Transactions can't mess with one another
* Durable - Completed transaction must stick around

BASE:
* Basic Availability - values availability even if stale
* Soft-state - might not be instantly consistent across stores
* Eventual Consistency - will achieve consistency at some point


## S3

#### About:
* One of the first AWS services
* S3 is an object store
* Used in other AWS services - directly and behind the scenes
* Maximum object size is 5TB; largest object in a single PUT is 5GB
* Recommended to use multi-part uploads if larger than 100MB
* A key != file path

#### S3 Consistency:
* S3 provides read-after-write consistency for PUTs of new objects:
Cool, I;ve never seen this object, and no-one has asked about it before.
Welcome aboard new object - and you can read it immediately.
* HEAD or GET requests of the key before and object exists will result
in eventual consistency: Wait a secomd someone already asked about 
this keu, and I told them, "never saw it". I remember that, and need 
to honor that response until I completely write this new object and fully
replicate it. So I'll let you read it eventually.
* S3 offers eventual consistency for overwrite PUTs and DELETEs:
Ok, so you want to update or delete an object. Let's make sure we get that
update or delete completed locally, then we can replicate it to other places. 
Until then I have to serve up the current file. I'll serve up the update/delete
 once its fully replicated - eventually.
* Updates to a single key are atomic: Whoa, there. Only one person can update 
this object at a time. If I get two requests I'll have to process them in order
 of their timestamp and you'll see the updates as soon as I replicate elsewhere.
 
 #### S3 Security
 * Resource based (Object ACL, Bucket policy)
 * User based (IAM policies)
 * Optional MFA before delete
 
 #### S3 Data Protection
 Versioning:
 * New version with each write
 * Enables roll-back and un-delete capabilities
 * Old versions counted as billable size until they're permanently deleted
 * Integrated with lifecycle management
 
 MFA:
 * Safeguard against accidental deletion of an object
 * Change the versioning state of your bucket
 
 Cross region replication:
 * Security 
 * Compliance
 * Latency
 
 #### S3 Lifecycle Management
 * Optimize storage costs
 * Adhere to data retention policies
 * Keep S3 volumes well maintained
 
 #### S3 Analytics
 * IoT Streaming Data Repository: Kinesis Firehose directly into an S3 bucket
 * Machine Learning & AI Storage: Rekognition, Lex, MXNet can reference S3 data
 * Storage Class Analysis: S3 management analytics (help analyze storage class optimization)
 
 #### S3 Encryption at Rest
 * SSE-S3: Use S3's existing encryption key for AES-256
 * SSE-C Upload your own AES-256 encryption key which S3 will use when it writes the object.
 * SSE-KMS: Use a key generated and managed by AWS Key Management Service
 * Client-Side: encrypt objects using your own local encryption process before uploading to 
 S3 (i.e. PGP, GPG, etc.)
 
 #### More Nifty S3 Tricks
 * Transfer Acceleration: Speed up data uploads using Cloudfront in reverse
 * Requester Pays: The requester rather than the bucket owner pays for requests and data transfer.
 * Tags: Assign tags to objects for use in costing, billing, security, etc.
 * Events: Trigger notification to SNS, SQS, or Lambda when certain events happen in your bucket
 * Static Web Hosting: Simple and massively scalable static web hosting
 * BitTorrent: Use BitTorrent protocol to retrieve any publicly available object by automatically
 generating a .torrent file.
 
 
 ## Glacier
 
 #### Overview
 * Cheap, slow to respond and seldom accessed
 * Used by AWS Storage Gateway Virtual Tape Library
 * Integrated with AWS S3 via lifecycle management
 * Faster retrieval speed options available if you pay more
 * Glacier is immutable meaning that in order to update something it must be deleted and re-uploaded
 
 #### Glacier Vault
 Glacier vault locks:
 * Must be confirmed within 24 hours if not confirmed then vault is deleted
 * Once applied it cannot be changed
 
 ## Elastic Block Storage
 
 #### Overview
 * Think "virtual hard drives"
 * Can only be used w/EC2
 * Tied to a single AZ
 * Variety of Optimized choices for IOPS, Throughput & cost
 * Snapshots are great!
 
 #### EBS vs Instance Stores
 * EBS: Able to attach and detach from EC2 instances and move amongst instances
 * Instance: Temporary, ideal for caches, buffers & work ares. Data goes away once 
 EC2 instance is terminated or stopped.
 
 #### Snapshots
 * Cost effective and easy backup strategy
 * Share data sets with other users or accounts
 * Migrate a system from a new AZ or region
 * Convert unencrypted volume to an encrypted volume
 
 #### Amazon Data Lyfecycle Manager
 * Schedule snapshots for volumes or instances every X hours
 * Retention rules to remove stale snapshots
 

## Amazon Elastic File System

#### Overview
* Implementation of NFS file share
* Elastic storage capacity and pay for only what you use (in contrast to EBS)
* Multi-AZ metadata and data storage
* Configure mount-points in one, or many, AZs.
* Can be mounted from on-premises systems. (Caution: Worry about latency and NFS is not a secure protocol so if done it should be over a VPN connection)
* Alternatively, use Amazon DataSync with on-prem
* 3x more expensive than EBS & 20x more expensive than S3

Example use would be to serve up a PHP web app across a fleet of servers.

## Amazon Storage Gateway
* Virtual machine that you run on-premises with VMWare or HyperV or via specifically configured Dell hardware appliance
* Provides local storage resources backed by AWS S3 and Glacier
* Often used in disaster recovery preparedness to sync to AWS
* Useful in cloud migrations

Multiple modes:
* File Gateway: Exposes volumes as NFS or SMB and allows on-prem EC2 instances to store objects in S3 via NFS or SMB mount point
* Volume Gateway Stored Mode / Gateway-stored Volumes: Exposes volumes via iSCSI interface and allows for asycn replication of on-prem data to S3
* Volume Gateway Cached Mode / Gateway-cached Volumes: Exposes volumes via iSCSI interface and allows for primary data stored in S3 with frequently accessed data to be cached locally on prem.
* Tape Gateway / Gateway-virtual Tape Library: Exposes volumes via iSCSI interface and allows for virtual media changer and tape library for use with existing backup software


## EC2 Databases
* Run any database with full control and ultimate flexibility
* Must manage everything like backups, redundancy, patching, scale
* Good option if you require a database not yet supported by RDS such as IBM DB2 or SAP HANA
* Good option if it is not feasible to migrate to AWS-managed database


## RDS
* Managed database option for MySQL, Maria, PostgreSQL, Microsoft SQL Server, Oracle, and MySQL compatible Aurora
* Best for structured, relational data store needs
* Aims to be a drop in replacement for existing on-prem instances of same databases
* Automated backups and patching in customer defined maintenance windows
* Push button scaling, replication and redundancy

#### Anti-Patterns
| If you need... | Don't use RDS, instead use... |
| -------------- | ----------------------------- |
| Lots of large binary objects (BLOBS) | S3 |
| Automated scalability | DynamoDB |
| Name/Value data structure | DynamoDB |
| Data is not well structured or unpredictable | DynamoDB |
| Other database platforms like IBM DBS or SAP HANA | EC2 |
| Complete control over the database | EC2 |


## DynamoDB
* Managed multi-az NoSQL data store with cross region replication option
* Defaults to eventual consistency reads but can request strongly consistent read via SDK parameter
* Priced on throughput, rather than compute
* Provisioned read and write capacity in anticipation of need
* Autoscale capacity adjusts per configured min/max levels
* On-Demand Capacity for flexible capacity at a small premium cost
* Achieve ACID compliance with DynamoDB Transactions

#### Relations vs NoSQL
Relational databases are best when the data is in a "relational structure". 
A NoSQL db excels at Name Value pairs with a self contained record.

Name Value pair -> Attribute
Item -> Whole collection of name and values
Many Items -> come together to form a table

#### Partition Key
* Must be unique
* Creates a hash from this value which is used to determine what partition the item is stored in
* Can use a composite primary key known as a partition key and sort key. We can have occurences of the same partition key 
so long as the sort key is different. Useful when pulling back data based on a sort key, eg. by date.

#### Secondary Indexes
| Index Type | Description | How to Remember |
| ---------- | ----------- | --------------- |
| Global Secondary Index | Partition key and sort key can be different from those on the table | I'm not restricted to just the partitioning set forth by the partition key. I'm global baby. |
| Local Secondary Index | Same partition key as the table but different sort key | I have to stay local and respect the table's partition key, but I can choose whatever sort key I want.

* There is a limit to the number of indexes and attributes per index
* Indexes take up storage space

| Index Type | When to Use | Example |
| ---------- | ----------- | ------- |
| Global Secondary Index | When you want a fast query of attributes outside the primary key = without having to do a table scan | "I'd like to query sales orders by customer number rather than sales order number" |
| Local Secondary Index | When you already know the partition key and want to quickly query on some other attribute | "I have the sales order number, but I'd like to retrieve only those records with a certain material number" |

| If you need to ... | Consider... | Cost | Benefit |
| ------------------ | ----------- | ---- | ------- |
| access just a few attributes the fastest way possible | project just those few attributes in a global secondary index | mimimal | lowest possible latency access for non-key items |
| frequently access some non-key attributes | projecting those attributes in a global secondary index | moderate; aim to offset cost of table scans | lowest possible latency access for non-key items |
| frequently access most non-key attributes | projecting those attributes or even the entire table in a global secondary index | up to double | maximum flexibility |
| rarely query but write or update frequently | projecting keys only for the global secondary index | minimal | very fast write or updates for non-partition-key items |

## Redshift
* Fully managed, cluster petabytes scale data warehouse
* Extremely cost effective  as compared to some other on-premises data warehouse platforms
* PostgreSQL compatible with JDBC and ODBC drivers available; compatible with most BI tools out of the box
* Features parallel processing and columnar data stores which are optimized for complex queries
* Option to query directly from data files on S3 vi Redshift Spectrum

#### Datalake
* Query raw data without extensive pre-processing
* Lessen time from data collection to data value
* Identify correlations between disparate data sets
* Can use S3 to dump lost of data into and then use Redshift Spectrum to query that data with other tools

## Neptune
* Fully managed graph database
* Supports open graph APIs for both Gremlin and SPARQL
* Best for inter relationship data

## Elasticache
* Fully managed implementations of two popular in memory data stores - Redis & Memcached
* Push button scalability for memory writes and reads
* In Memory key/value store - not persistent in the traditional sense...
* Billed by node size and hours of usage

#### Use Cases
| Use | Benefit |
| --- | ------- |
| Web session store | In cases with load balanced web serves, store web session information in Redis so if a server is lost, the session info is not lost and another web server can pick-up |
| Database caching | Use Memcache in front of AWS RDS to cache popular queries to offload work from RDS and return results faster to users |
| Leaderboards | Use Redis to provide a live leaderboard for millions of users of your mobile app |
| Streaming data dashboards | Provide a landing spot for streaming sensor data on the factory flow, providing real-time dashboard displays |

#### Data Store Types
Memcached:
* Simple, no-frills, straight forward
* You need to scale out and in as demand changes
* You need to run multiple CPU cores and threads
* You need to cache objects (i.e. like database queries)

Redis:
* You need encryption
* You need HIPPA compliance
* Support for clustering
* You need complex data types
* You need high-availability (replication)
* Pub/Sub capability
* Geospacial indexing
* Backup and restore
 

## Other Database Options

#### Amazon Athena
* SQL engine overlaid on S3 based on Presto
* Query raw data objects as they sit in an S3 bucket
* Use or convert your data to Parquet format if possible for a big performace jump
* Similar in concept to Redshift spectrum

Use Athena: Data lives mostly in S3 without the need to perform joins with other data sources
Redshift Spectrum: Want to join S3 data with existing RedShift tables or create union products

#### Amazon Quantum Ledger Database
* Based on blockchain concepts
* Provides an immutable and transparent journal as a service without having to setup and maintain an entire blockchain framework
* Centralized design (as opposed to decentralized consensus-based design for common blockchain frameworks) allows for higher performance and scalability
* Append only concept where each record contributes to the integrity of the chain

#### Amazon Managed Blockchain
* Fully managed blockchain framework supporting open source frameworks of Hyperledger Framework and Ethereum
* Distributed consensus-based concept consisting of a network, members (other AWS accounts), nodes (instances), and potentially applications.
* Uses the Amazon QLDB ordering service to maintain complete history of all transactions

#### Amazon Timestream Database
* Fully managed database service specifically built for storing and analyzing time-series data
* Alternative to DynamoDB or RedShift and includes some built-in analytics and like interpolation and smoothing

Example usese: Industrial machinery, sensor networks, equipment telemetry

#### Amazon DocumentDB
* Compatible with MongoDB
* Fully managed, multi AZ, HA, scalable
* Integrated with KMS & backups to S3

#### Amazon ElasticSearch
* Also referred to as ES
* Mostly a search engine but also a document store 
* Amazon ElasticSearch Service components are sometimes referred to as an ELK stack
 
 
 ## Amazon Database Options
 Database on EC2:
 * Unlimited control over database
 * Preferred DB not available under RDS
 
 Amazon RDS:
 * Need traditional relational database for OLTP
 * Your data is well-formed and structured
 
 Amazon DynamoDB:
 * Name/value pari data or unpredictable data structure
 * In-memory performance with persistence
 
 Amazon RedShift:
 * Massive amounts of data
 * Primarily OLAP workloads
 
 Amazon Neptune:
 * Relationships between objects a major portion of data value
 
 Amazon Elasticache:
 * Fast temporary storage for small amounts of data
 * Highly volatile data
 
 
 ## Exam Tips
 
 White Papers:
 * [AWS Storage Services Overview White Paper](https://d1.awsstatic.com/whitepapers/Storage/AWS%20Storage%20Services%20Whitepaper-v9.pdf)
 * [SASS Storage Strategies](https://d1.awsstatic.com/whitepapers/Multi_Tenant_SaaS_Storage_Strategies.pdf)
 * [Performance at Scale with Amazon ElastiCache](https://d0.awsstatic.com/whitepapers/performance-at-scale-with-amazon-elasticache.pdf)
 
 re:Invent Videos:
 * [S3 Deep Dive](https://www.youtube.com/watch?v=SUWqDOnXeDw&ab_channel=AmazonWebServices)
 * [RDS Deep Dive](https://www.youtube.com/watch?v=TJxC-B9Q9tQ&ab_channel=AmazonWebServices)
 * [ElastiCache Deep Dive](https://www.youtube.com/watch?v=_YYBdsuUq2M&ab_channel=AmazonWebServices)
 * [Hybrid Storage](https://www.youtube.com/watch?v=9wgaV70FeaM&ab_channel=AmazonWebServices)
 
 
 ## Pro Tips
 Storage:
 * Archiving and backup often a great "pilot" to build AWS business case
 * Make use of the S3 endpoints with your VPC
 * Learn how to properly secure your S3 bucket
 * Encrypt, Encrypt, Encrypt
 
 Database:
 * Consider Aurora for MySQL or PostgreSQL needs
 * Consider NoSQL if you don't need relational database features
 * Databases on EC2 cost less on the surface than RDS, but remember to factor in management
 * there can be a performance hit when RDS backups run if you have only a singe AZ instance
 
 
 ## Challenges
 1. 
 * Mine: B, A, D, C
 * Correct: D, A, C, B
 
 2. 
 * Mine: C
 * Correct: C
 
 ## Lab - Air Quality Analysis
 
 