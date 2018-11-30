#Monitoring & Reporting

##CloudWatch Introduction
####Host Level Metrics
* CPU
* Network
* Disk
* Status Check

Exam Tip: RAM utilization is a custom metric. By default EC2 monitoring is 5 min
intervals, unless you enable detailed monitoring which will then make it 1 min
intervals.

####How Long are CloudWatch Metrics Stored?
You retrieve data using the GetMetricStatistics API or by using third party tools
offered by AWS partners

You can store your log data in CloudWatch for as long as you want. By default
CloudWatch logs are stored in each log group indefinitely. You can change the 
retention for each group at any time.

You can retrieve data from any terminated EC2 or ELB instance after it has been
terminated.

####Metric Granularity
It depends on the AWS service. Many default metrics for many services is 1 min,
but it can be 3 min or 5 min depending on the service.

For custom metrics the min granularity you can have is 1 min.

####CloudWatch Alarms
You can create alarms to monitor any metrics in your account. You can set 
thresholds and trigger alarms.

####Exam Tips
CloudWatch can be used on premise as well. You just need to download the SSM
agent and CloudWatch agent.

##Monitoring EC2 With Custom Metrics
We can create an EC2 instance, with the below script as the startup script. Once
the EC2 instance has been created, we can SSH into the system, and run the 
commented out commands to make the EC2 instance push metrics to CloudWatch
every minute.
* **note**: even though metrics are being sent to CloudWatch every minute, they
will only be available in 5 minute intervals unless detailed monitoring for EC2
is turned on.
Startup script:
```bash
#!/bin/bash
yum update -y
sudo yum install -y perl-Switch perl-DateTime perl-Sys-Syslog perl-LWP-Protocol-https perl-Digest-SHA.x86_64
cd /home/ec2-user/
curl https://aws-cloudwatch.s3.amazonaws.com/downloads/CloudWatchMonitoringScripts-1.2.2.zip -O
unzip CloudWatchMonitoringScripts-1.2.2.zip
rm -rf CloudWatchMonitoringScripts-1.2.2.zip

# Verifies that you can push metrics to cloudwatch
#   /home/ec2-user/aws-scripts-mon/mon-put-instance-data.pl --mem-util --verify --verbose

# Pushes metrics to cloudwatch
#   /home/ec2-user/aws-scripts-mon/mon-put-instance-data.pl --mem-util --mem-used --mem-avail

# Below command is for a cron job to run every min that pushed metrics to cloudwatch
#   */1 * * * * root /home/ec2-user/aws-scripts-mon/mon-put-instance-data.pl --mem-util --mem-used --mem-avail
```

##Monitoring EBS

#### EBS - Different Volume Types
4 Different Types of EBS Storage;
* General purpose (SSD) - gp2
* Provisioned IOPS (SSD) - io1
* Throughput optimization (HDD) -st1
* Cold (HDD) - sc1

#### Compare Volume Types
General purpose ssd:
* Recommended for most workloads
* System boot volumes
* Virtual desktops
* Low latency interactive apps
* Development and test environments

Provision IOPS SSD
* Critical business applications that require sustained IOPS performance or more
than 10,000 IOPS or 160 MiB/s of throughput per volume
* Large database workloads such as MonggoDB, Cassandra, or MicrosoftSQL

Throughput Optimized HDD
* Streaming workloads requiring consistent, fast throughput at a low price
* Big data, data warehouses, log processing
* Cannot be a boot volume

Cold HDD
* Through put oriented storage for large volumes of data that us infrequently
accessed
* Scenarios where the lowest storage cost is important
* Cannot be a boot volume

#### IOPS & Volumes
General purpose SSD volumes have a base of 3 IOPS per/GiB of volume size
* Maximum volume size of 16,384 GiB
* Maximum IOPS size 10,000 total (after that you need to move to provisioned
IOPS)

Say we have 1 Gib volume. We get 3 IOPS per Gb so we have 3x1 = 3 IOPS.
* We can burst performance on this volume up to 3000 IOPS if we want
* Using I/O credits
* The bust would be 2997 IOPS (ie 3000 - 3)

The bigger the volume the more performance you get. If you need a 6000 IOPS,
you'll need to make sure the volume size is large enough. In this case
the drive would need to be 3000 GiB in order to receive 6000 IOPS.

####I/O Credits
When your volume requires more than the baseline performance of I/O level, it
simply uses I/O credits in the credit balance to burst to the required performance
level, up to a maximum of 3,000 IOPS.
* Each volume receives an initial I/O credit balance of 5,400,000 I/O credits
* This is enough to sustain the maximum burst performance of 3,000 IOPS for 
30 minutes
* When you are not going over your provisioned IO level you will be earning 
credits

####Pre-Warming EBS Volumes
New EBS volumes receive their maximum performance the moment that they are
available and do not require initialization (formerly known as pre-warming).
However storage blocks on volumes that were restored from snapshots must be 
initialized (pulled down from S3 and written to the volume) before you can 
access the block. This preliminary action takes time and can cause a 
significant increase in the latency of an I/O operation the first time each block
is accessed. For most applications, amortizing this cost over the lifetime of the
volume is acceptable. Performance is restored after the data is accessed once.

You can avoid this performance hit in a production environment by reading from
all of the blocks on your volume before you use it; this process is called 
initialization. For a new volume created from a snapshot, you should read all
the blocks that have data before using the volume.

####EBS CloudWatch Metrics
* VolumeReadOps & VolumeWritOps: The total number of I/O operations in a 
specific period of time. **Note**: to calculate the average I/O per second
for the period, divide the total operations in the period by the number
of seconds in that period.
* VolumeQueueLength: The number of read & write operation requests waiting to be 
completed in a specific time period. **note**: you want this to be 0, if it's not
it means that you're maxing out your IOPS.

####Volume Status Checks
* ok: Normal
* Warning: Degraded (performance is below expected) or severely degraded 
(volume performance is well below expected)
* impaired: Stalled (volume performance is severely impacted) or not available
(unable to determine I/O performance because I/O is disabled)
* insufficient data: insufficient data

####Modifying EBS Volumes
If your EBS volume is attached to a current generation EC2, tou can increase it's
size, change the volume type, or ()for an io1 volume) adjust it's IOPS performance,
all without detaching it. 
* Issue the modification from the command line
* Monitor the progress
* If the size of the volume was modified, extend the volume's file system to 
take advantage of the increased storage capacity

####Exam Tips
* Remember EBS types
* Remember when to use each type
* General purpose SSD burst
* With metrics you should always track you read and write IOPS, along with
volume queue length
* Remember the volume status checks

##Monitoring ELB

####ELB - Load Balancer Types
* Application load balancer
* Network load balancer
* Classic load balancer

####ELB - Monitoring Types
* CloudWatch metrics
* Access logs
* Request tracing
* CloudTrail logs

####CloudWatch VS CloudTrail
* CloudWatch monitors performance
* CloudTrail monitors API calls in the AWS platform

####CloudWatch Metrics
Elastic Load Balancing publishes data points to CloudWatch for your load balancers
and your targets. CloudWatch enables you to retrieve statistics about those data
points as an ordered set of time-series data, known as metrics. Think of a metric
as a variable to monitor, and the data points as the values of that variable over
time. For example, you can monitor the total number of healthy targets for a 
load balancer over a specific time period. Each data point has an associated time
stamp and an optional unit of measurement.

####Access Logs
Elastic load balancing provides access logs that capture detailed information 
about requests sent to your load balancer. Each log contains information such as
the time the request was received, the client's IP address, latencies, request 
paths, and server responses. You can use these access logs to analyze traffic 
patterns and troubleshoot issues.

Access logging ia an optional feature, that is disabled by default. After you 
enable access logging for your load balancer, ELB captures the logs and stores
them in an S3 bucket that you specify as zip files. You can disable logging at
any time.

####Access Logs - SUPER IMPORTANT
Access logs can store data where the EC2 instance has been deleted. For example
say you have a fleet of EC2 instances behind an autoscaling group. For some 
reason your application has a load of 5XX errors which is only reported by your
end customers a couple of days after the event. If you aren't storing the web 
server logs anywhere persistent, it is still possible to trace these 5XX errors
using access logs which would be stored in S3.

####Request Tracing
You can use request tracing to track HTTP requests from clients to targets or 
other services. When the load balancer receives a request from a client, it 
adds or updates the `X-Amzn-Trace-Id` header before sending it on to the request
target. Any services between the load balancer and the target can update this 
value as well.

####CloudTrail
You can use it to capture detailed information made to your ELB API and store them
as log files in S3. You can track which calls are made, source IP, who made the
call, when the call was made, and so on.


##Monitoring Elasticache

####Elasticache
Two main engines
* Memcached
* Redis

####Monitoring
CPU Utilization:
* Memcached
  - Multi-threaded
  - Can handle leads of up to 90%. If it exceeds 90% add more nodes to the cluster.
* Redis
  - Not multi-threaded. To determine the point in which to scale, take 90 and 
  divide by the number of cores
  - For example if you're using a cache.m1.xlarge node, which has 4 cores. In
  this case, the threshold for CPU utilization would be (90/4), or 22.5%

Swap Usage:
* Swap usage is simply the amount of Swap file that is used. The Swap file is the 
amount of disk storage space reserved on disk if your computer runs out of ram. 
Typically the size of the swap file = the size of the RAM. So if you have 4Gb of
RAM, you will have a 4GB Swap file. 
* Memcached
  - Should be around 0 most of the time and should not exceed 50Mb
  - If this exceeds 50Mb you should increase the memcached_connections_overhead
  parameter
  - The memcached_connections_overhead defines the amount of memory to be 
  reserved for memchaced connections and other miscellaneous overhead
* Redis
  - No SwapUasage metric, instead use reserved-memory

Evictions:
* Think of evictions like tenants in an apartment building. There are a number of
empty apartments that slowly fill up with tenants. Eventually the apartment block
is full, however more tenants need to be added.
* An eviction occurs when a new item is added and an old item must be removed due
to lack of free space in the environment.
* Memcached
  - There is no recommended setting. Choose a threshold based off your app
  - Either scale up ot scale out
* Redis
  - There is no recommended setting. Choose a threshold based off your app
  - Only scale out (add read replicas)
  
Concurrent Connections:
* Memcached & Redis
  - There is no recommended setting. Choose a threshold based off your app
  - If there is a large and sustained spike in the number of concurrent connections
  this can either mean a large traffic spike of your application is not releasing
  connections as it should be.

####Exam Tips
* Remember the 2 different caching engines
* Remember the 4 important things to monitor

## CloudWatch Custom Dashboards

#### Exam Tips
* Dashboards are international
* Add widgets on a per region basis

## Creating A Billing Alarm

#### Exam Tips
* Create alarms under alarms and select billing in CloudWatch. This will allow
you to receive an email when your bill crosses a certain dollar threshold.

## AWS Organizations

#### What is AWS Organizations
