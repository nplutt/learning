# Storage & Data Management

## S3 101

#### What is S3?
S3 provides developers and IT teams with secure, durable, HA, object storage. S3
is easy to use and files can be retrieved from any where on the web.

Safe place to store your files. 

Data is spread across multiple devices and facilities.

#### S3 the basics
* S3 is object based
* Files can be 0 bytes to 5 TB
* There is unlimited storage
* Files are stored in buckets
* S3 has a universal name space i.e. names must be unique globally.
* When you upload a file, you'll receive a 200 status code
* Built for 99.99% availability

#### Data Consistency Model For S3
* Read after write consistency for PUTS of new objects
* Eventual consistency for overwrite PUTS and DELETES (can take some time to 
propagate)


#### S3 Is A Simple KV Store
* S3 is object based. Objects consist of the following:
  - Key
  - Value
  - Version ID
  - Metadata
  - Subresources - bucket specific configuration
    * Bucket policies, Access Control Lists
    * Cross Origin Resource Sharing (CORS)
    * Transfer Acceleration
    
#### S3 the basics
* Amazon guarantees 99.9% availability
* Amazon guarantees 99.99999999999% durability for S3 information. (Remember 11 x 9's)
  - Keep multiple versions 
  - Replicate data
  - Permissioning around deleting objects
* Tiered storage
* Lifecycle Management
* Versioning
* Encryption
* Secure your data - ACLs

#### S3 - Storage Tiers/Classes
* S3: 99.99% availability, 99.999999999999% durability, stored redundancy across
multiple facilities, and is designed to sustain the loss of 2 facilities concurrently.
* S3 - IA (Infrequently Accessed): For data that is accessed less frequently, but
requires rapid access when needed. Lower fee than S3, but you're charged a retrieval
fee.
* S3 - One Zone IA: Same as IA however data is stored in a singe AZ only, still 
99.99999999999% durability, but only 99.5% availability. Cost is 20% less than 
regular S3 - IA.
* Reduced Redundancy Storage: Designed to provide 99.99% durability and 99% 
availability of objects over a given year. Used for data that can ve recreated,
e.g. thumbnails.
* Glacier: Very cheap, but used for archival only. Optimised for data that is 
infrequently accessed and it can take 3-5 hours to restore from Glacier.

#### S3 Charges
Charged for:
* Storage per GB
* Requests (Get, Put, Copy, etc.)
* Storage management pricing
  - Inventory, Analytics, and object tags
* Data management pricing
  - Data transfer out of S3
* Transfer Acceleration
  - Use of CloudFront to optimize transfers

#### Exam Tips
* S3 is object based
* Files can be 0 to 5 TB
* Unlimited storage
* Files are stored in buckets
* Universal name space
* Read and write consistency PUTS of new objects
* Eventual consistency for overwrite PUTS and DELETES
* S3 storage classes/tiers
* Core fundamentals of an S3 object
* Successful uploads will generate 200 status code
* Read S3 FAQ

## S3 Lifecycle Policies

#### Lifecycle Policies
* You can use these to manage your objects so that they are stored using the most
cost effective S3 option throughout their lifecycle
* You can configure lifecycle rules to tell S3 to transition objects to less
expensive storage classes, archive them or delete them.
* Best for objects which have a well defined lifecycle e.g.g log files, which may
not be useful once they reach a certain age.

#### Example S3 Lifecycle Policies
* Transition objects to an IA storage class 90 days after you created them - e.g.
transaction log files
* Archive objects to Glacier 1 year after creating them
* Configure objects to expire 1 year after creating them - S3 will auto delete
expired objects on your behalf
* e.g. buckets with server access logging can accumulate many log files over time

#### Exam Tips
* S3 policies are used to ensure your using the most cost effective S3 option
* Rules are based on creation date
* Can transition your objects to infrequently accessed storage or Glacier
* Can have objects delete after certain date

## MFA Delete

#### MFA Delete & S3 Versioning
* S3 versioning allows you to revert to older versions of S3 objects
* Multiple versions of an object are stored in the same bucket
* Versioning protects against accidental / malicious deletes
* With versioning enabled, a DELETE actions doesn't actually delete the object 
version, but applies a delete marker instead
* To permanently delete, provide the object version ID
* MFA delete provides an addition layer of protection to S3 Versioning
* Once enabled, MFA Delete will enforce 2 things:
  - You will need to provide a valid code when deleting an object version
  - MFA is needed to suspend/reactivate MFA
  
## S3 Encryption

#### Encryption
* In transit:
  - SSL/TLS
* At rest:
  - Server side encryption:
    * S3 managed keys - SSE-S3
    * AWS Key Management Service, Managed Keys, SSE-KMS
    * Server Side Encryption with Customer Provided Keys - SSE-C
* Client side encryption

#### Enforcing Encryption on S3 Buckets
* Every time a file is uploaded to S3 a PUT request is initiated
* If the file is to be encrypted at upload time, the x-amz-server-side-encryption
parameter will be included in the request
  - The 2 values for this parameter are:
    * AES256 (S3 managed keys)
    * ams:kms ( SSE-KMS - KMS managed keys)
* When this param is included in the header of the PUT request, it tells S3 to 
encrypt the object at the time of upload, using the specified encryption method
* You cna enforce the use of Server Side encryption by using a Bucket Policy which
denies any S3 PUT request which doesn't include the required header.

## EC2 Types - EBS vs Instance Store

#### History
When EC2 was 1st launched, all AMI's were backed by Amazon's Instance Store.
Instance store is known as ephemeral storage, which simply means non-persistence
or temporary storage.

Later when AWS launched EBS which allows users to have data persistence and to
save their data permanently.

#### Confusion
There is a lot of confusion between the instance store volumes and EBS volumes.
It's important to know the difference between the two. To start there are 2
types of volumes:
* Root volume (This is where OS is installed)
* Additional volumes (This can be D:\ E:\ F:\ or /dev/sdb, /dev/sdc, /dev/sdd etc)

#### Root Volume Sizes
* Root device volumes can either be EBS volumes or Instance Store volumes
* An Instance store root device volume's max device size is 10 Gb
* EBS root device volume can be up to 1 or 2 Tb depending on the OS

#### Terminating an Instance
EBS
* EBS root device volumes are terminated by default when the EC2 instance is 
terminated. You can stop this by unselecting the "Delete on termination" option
when creating the instance, or by setting the deleteontermination flag to false
in the command line.
* Other EBS volumes attached to the instance are preserved however, if you delete
the instance

Instance Store
* Instance store device root volumes are terminated by default when the EC2 instance
is terminated. You can't stop this.
* Other instance store volumes will de deleted on termination automatically
* Other EBS volumes attached to the EC2 instance will persist automatically

#### Stopping and Instance
* EBS backed instances can be stopped
* Instance Store backed instances cannot be stopped. Only rebooted or terminated.

#### Instance Data Store
The data in an instance store persists only during the lifetime of its associated
instance. If an instance reboots (intentionally or unintentionally), data in the 
instance store volumes is lost under the following circumstances:
* Failure of an underlying drive
* Stopping and EBS backed instance
* Terminating and instance

Therefore, do not rely on instance store volumes for valuable, long term data.
Instead keep your data save by using replication strategy across multiple 
instances, storing data in S3, or by using EBS volumes.

#### Exam Tips
* Delete on Termination is the default for all EBS root device volumes. You can
set this to false however but only at instance creation time.
* Additional volumes will persist automatically. You need to delete this manualy
when you delete an instance.
* Instance Store is known as ephemeral storage, meaning that data will not
persist after the instance is deleted. You can't set this to false, data will 
always be deleted when that instance disappears.

## EBS Volumes Lab

#### Notes
* Your EBS volume and EC2 instance must be in the same AZ
* Can modify root volume once provisioned with no down time. There will be a 
IOPS hit while this is being done though.
* To move and EBS volume from one AZ to another, you must 1st take a snapshot, 
then copy it to the new region.

#### Volumes & Snapshots
* Volumes exist on EBS:
  - Virtual hard disk
* Snapshots exist on S3
* Snapshots are point in time copies of volumes
* Snapshots are incremental - this means that only the blocks that have changed
since your last snapshot are moved to S3.
* If it's the 1st snapshot it can take a while

#### Snapshots of Root Devices
* To create a snapshot for EBS volumes that serve as root devices, you should stop
the instance before taking the snapshot.
* However you can take a snap while the instance is running
* You can create AMI's from both images and snapshots
* You can change EBS volumes sizes on the fly, including changing the size and 
storage type.
* Volumes will always be in the same AZ as the EC2 instance
* To move an EC2 volume from one AZ/Region to another, take a snap or an image of
it, then copy it to the new AZ/Region.

#### Volumes vs Snapshots - Security
* Snapshots of encrypted volumes are encrypted automatically
* Volumes restored from encrypted snapshots are encrypted automatically
* You can share snapshots, but only if they are unencrypted
  - These snapshots can be shared with other AWS accounts or made public
* Look at the lab one more time before the exam!!!

## Encryption and Downtime

#### Enabling Encryption and Downtime
* For most AWS resources, encryption can only be enabled at creation.
* EFS: if you want to encrpyrt an EFS filesystem that already exists, you will
need to create a new encrypted EFS and migrate your data.
* RDS: if you want to encrypt and existing RDS, you will need to create a new 
encrypted db and migrate your data
* EBS Volumes: encryption must be selected at creation time
  - You can't encrypt an unencrypted volume or unencrypt an encrypted volume
  - You can migrate data between encrypted and unencrypted volumes
  - If you want to encrypt an existing volume, you can create a snapshot, copy 
  the snapshot and apply encryption at the same time yo give you and encrypted 
  snapshot. Then restore the encrypted snapshot to new encrypt volume.
* S3 is much more flexible
  - S3 Buckets: you can enable encryption at any time
  - S3 Objects: you can enable encryption at any time

## KMS vs CloudHSM

#### What are KMS and CloudHSM
* Both allow you to generate, store and manage cryptographic keys used to protect
yout data in AWS
* HSMs (Hardware Security Modules) are used to protect the confidentiality of your
keys
* Both offer a high level of security

#### KMS vs CloudHSM
KMS
* KMS - Shared hardware, multi-tenant managed service
* Allows you to generate, store, and manage your encryption keys
* Suitable for applications for which multi-tenancy is not an issue
* Free tier eligible
* Encrypt your data stored in AWS, including EBS volumes, S3, RDS, DynamoDB, etc.

CloudHSM
* CloudHSM - Dedicated HSM instance, hardware is not shared with other tenants no
Free tier
* Allows you to generate, store and manage your encryption keys
* HSM is under your exclusive control within your VPC
* FIPS 140-2 Level 3 compliance (US Government for HSMs) - includes tamper-evident 
physical security mechanisms
* Suitable for applications which have a contractural or regulatory requirement 
for dedicated hardware managing cryptographic keys
* Use cases include: database encryption, digital rights management (DRM),
Public Key Infrastructure (PKI), authentication and authorization, document
signing, and transaction processing
  
## AMIs

#### AMIs
An AMI provides all the info needed to launch an EC2 instance
* Template for the root volume, e.g. OS, Applications
* Launch permissions - defining which AWS accounts can use the AMI to launch 
instances
* Block device mapping to specify EBS volumes to attach to the instance at launch
time
* AWS provides a selection of default AMIs
* You can also create your own custom AMIs
  - Launch an instance from and existing AMI
  - Create a custom AMI image from your instance
  - Your AMI mist be registered before it can be used to launch an instance

#### AMIs are Regional
* AMIs are registered on a per region basis
* If you have registered your AMI in us-east-1 and you want to use it to launch
instances in eu-west-1, you need to copy it ot eu-west-1 to use it.
* If you can't find an AMI in a region it might need to be copied there

## Sharing AMIs

#### Sharing AMIs
* After creating an AMI, you can either keep it private, share it with a 
specified list of AWS accounts, make it publicly available or even sell it on
the market place
* Sharing account still controls the AMI, as well as still pays for storage
of AMI

#### Copying AMIs
* The owner of the source AMI must grant you read permissions for the storage 
that backs the AMI
* If you cpy an AMI that was shared with you, you are then the owner of that 
copy and will be charged for the storage of the target AMI in the destination 
region

Limitations:
* Cannot directly copy and encrypted AMI shared by another account
  - Copy the snapshot and re-encrypt using your own key
  - The sharing account must also share with you the underlying snapshot and 
  encryption key used to create the AMI
  - You'll own the copied snapshot and can register it as a new AMI
* You cannot directly copy and AMI with an associated billingProducts code (
applies to Windows, RedHeat abd AMIs from AWS Marketplace)
* BillingProducts code is used to bill for the use of an AMI
* Launch an EC2 instance using the shared AMI and create an AMI from the shared
instance

#### Exam Tips
* AMIs can be shared & copied between user accounts
* Remember 2 restrictions:
  - Encrypted AMIs
  - Copy the underlying snapshot, re-encrypt using your own key and create a new
  AMI
  - AMIs with an associated billingProducts code
  - Launch an EC2 instance using the shared AMI and create an AMI from the 
  instance
  
## Snowball & Snowball Edge

#### What is snowball
* Snowball is a physical device used for transporting many terabytes or petabytes
of data into and out of AWS
* Makes large scale data transfers, fast easy and secure
* Tamper resistant enclosure
* 256 bit encryption
* Region specific transfers (not for moving data from 1 region to another)

How does it work?
* Connect to local network
* Snowball client auto encrypts and copies the data from network to location
* Notified when it's back at amazon

#### When to Use Snowball
* Have many TB or PB of data
* You don't want to make upgrades to your network for a 1 time thing
* If you frequently experience backlogs of data
* You're in an isolated location
* Use if it takes more than one week to upload your device

#### What is snowball edge
* Each one had 100TB device, which also features onboard compute power which can
be clustered together to act as a single storage & compute pool
* Designed to undertake local processing / edge computing as well as data transfer
* S3 compatible endpoint, supports NFS, and can also run AWS lambda functions 
as data is copied to the device
* S3 buckets and lambda functions come pre-configured on device

## Storage Gateway

#### What is storage gateway?
Consists of an on-premise software appliance which connects with AWS cloud-based
storage to give you a seamless and secure integration between your on-premises IT
environments and AWS.
* Storage gateway virtual appliance is installed in your data center
* Supports VMware ESXi ot Microsfot Hyper-V
* On-premises systems seamlessly integrate with AWS storage - e.g. S3

#### Types of Storage Gateway
* File Gateway - NFS / SMB
* Volume Gateway (iSCSI)
  - Stored volumes
  - Cached volumes
* Tape Gateway

#### File Gateway
* Files stored as objects in S3 buckets
* Accessing using NFS or SMB mount point
* To your on premises systems this appears like a file system mount backed by S3
* All the benefits of S3: bucket policies, S3 versioning, lifecycle management,
replication, etc
* Low cost alternative to on premises storage


#### Volume Gateway
* Provides cloud backed storage using the iSCSI protocol
* 2 different gateway types:
  - Gateway Stored Volumes: store all your data locally and only backup to AWS
  * Gateway Cached Volumes: Use S3 as your primary storage and cache frequently
  accessed data in your storage gateway
* Stored Volumes: Stores all data locally, so your applications get low latency
access to the entire data set
* You need your own storage infrastructure as all data is stored locally in your
data center
* Provides durable off site async backups in the form of EBS backups that are 
stored in S3

#### Cached Volumes
* Cached volumes: the gateway stores all your data in S3 and cached only frequently
accessed storage
* You need only enough local storage capacity to store the frequently accessed
data
* Applications still get low latency access to frequently used data without a 
large investment in on-premises storage

#### Tape Gateway
* Is a virtual tape library which provides cost effective data archiving in the 
cloud using Glacier
* You don't need to invest in your own tape backup infrastructure
* Integrates with existing tape backup infrastructure 
* Data is stored on virtual tapes which are stored in Glacier and accessed using
VTL

#### Exam Tips
* File gateway: flat files stored on S3, accessed using NFS or SMB
* Volume gateway - 2 types:
  - Stored volumes: entire dataset stored on site, backed up to S3 as EBS snapshots
  - Cached volumes: entire dataset stored in S3, only frequently access data
  cached on site
* Tape Gateway - VTL
  - Used for archiving your backups to Glacier
  * Can be used with or without your own backup application

## Athena

#### What is Athena
* An interactive query service that enables you to analyse and query data located
in S3 using standard SQL
* Serverless, nothing to provision, pay per query / per TB scanned
* No need to setup complex ETL processes
* Works directly with data stored in S3

#### Use cases
* Query log files stored in S3
* Generate business reports
* Analyse AWS cost and usage reports
* Run queries on click stream data

#### Exam Tips
* Remember what it is and what it allows you to do

