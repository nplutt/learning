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



