# Deployment & Provisioning

## EC2 Launch Issues

#### Common Issues
* InstanceLimitExceeded Error
  - You have reached the limit on the number of instances you can launch in 
  a region
  - Default limit is 20
  - Can request an increase on a per region basis
* InsufficientInstanceCapacity Error
  - AWS doesn't currently have enough available on demand capacity to service 
  your request
  - You could wait a couple minutes and then it might work
  - You could request fewer instances
  - You could select a different instance type
  - Try purchasing reserved instance
  - Submit a new request with no AZ specified
  
#### Exam Types
* Remember the 2 reasons why an instance might not launch

## EBS Volumes & IOPS

#### EBS Volumes
* Allows you to create storage volumes and attach them to your EC2 instance

#### EBS SSD IOPS
* 2 different variants of SSD:
  - GP2: boot volumes
  - io1: provisioned IOPS
* IOPS used to benchmark performance for SSD volumes
* IOPS capacity is dependent on your volume

#### Hitting the IOPS limit of your Volume
What can you do about it?
* If GP2, you can increase your drive size
  - If at 10,000 IOPS limit, then you'll need to change to io1
  
#### Exam Tips
* IOPS (Input/Output Operations per second) used to benchmark performance for
SSD volumes
* IOPS is dependent on the size of volume
* Increase the volume size if under 10,000 IOPS and move to io1 if greater than

## What is a Bastion Host?

#### Bastion Hosts
* A bastion host is a host located in your public subnet
* Allows you to connect to your EC2 instances using SSH ot RDP
* You can login to the Bastion host over the internet from your desktop
* You then use the bastion host to initiate SSH/RDP session over the private
subnet to your EC2 instances in the Private subnet.
* Allows you to safely administer your EC2 instances without exposing them to the
internet
* Also called a jump server
 
## Elastic Load Balancers 101

#### Types Of Load Balancers
* Application Load Balancer
  - Works at layer 7 of the OSI model
  - Ability to inspect packets and make routing decisions 
* Network Load Balancer
  - Works at layer 4 of the OSI model
* Classic Load Balancer
  - Works at layer 7 and 4
  - Legacy load balancer (not recommended any more)
  
#### Application Load Balancer
ALB's are best suited for load balancing of HTTP & HTTPS traffic. They operate at 
layer 7 and are application aware. They are intelligent, and you can create
advanced request routing, send specific requests to specific web servers.

#### Network Load Balancer
NLB's are best suited for load balancing of TCP traffic where extreme performance
is required. Operating at connection level (Layer 4), NLB are capable of handling
millions of requests per second.
* Most expensive option

#### Classic Load Balancer
CLB's are legacy. You can balance HTTP/HTTPS applications and use layer 7 specific
features such as X-Forwarded and sticky sessions. You can also use strict Layer 4 
load balancing for applications that rely purely on the TCP protocol.

#### Pre-Warming Your Load Balancers
Imagine you're running a busy website, and you learn that your website will receive
a huge spike in traffic in 2 days. How would you handle this?

There is a chance that a sudden increase in traffic could cause the ELB to be
overloaded and unable to handle all of the requests. In order to avoid this,
you can contact AWS and request them Pre-Warm your ELB.

Pre-Warming will configure the ELB to the appropriate level of capacity, based
on the traffic you expect.

AWS will need to know:
1. Start and end dates
2. Expected request rates
3. Total size of a typical request

#### Load Balancers & Static IP Addresses
* ALBs scale automatically to adapt to your workload
* However this has the effect of changing the IP address which your clients
connect to as new ALBs are brought into service
* NLBs solve this by creating a static IP address in each subnet you enable, 
so that keeps firewall rules really simple - clients only need to enable access
to a single IP address per subnet.
* You don't have to choose one ot the other, you can get the benefit of both, by
putting an ALB behind a NLB.

#### Exam Tips
* Remember the 3 types
* Can pre-warm load balancers if needed
* Static IP's can be provided by NLB and there will be 1 per subnet

## ELB Error Messages

#### Load Balancer Errors 4XX and 5XXX
* Classic & ALB's by default the successful response code is 200
* Unsuccessful request will generate 4XX or 5XX
* 4XX indicates something has gone wrong on the client side
* 5XX message relate to server side errors

## ELB CloudWatch Metrics

#### Metrics
* ELBs publish metrics to CloudWatch for the load balancer itself and for the 
backend instances
* Helps you verify that your system is performing as expected
* Can create CloudWatch alarm to perform a specific action
* Metrics gathered at 60 second intervals

#### Overall Health
* BackendConnectionErrors: number of unsuccessful connections to backend instances
* HealthyHostCount: number of healthy instances registered
* UnHealthyHostCount: number of unhealthy instances
* HTTPCode_Backend_2XX,3XX,4XX,5XX

#### Performance Metrics
* Latency: number of seconds for registered instances to respond / connect
* RequestCount: number of requests completed / connections made during specified
interval of 1 or 5 min 
* SurgeQueueLength: number of pending requests, max queue size is 1024, additional
requests will be rejected (Classic only)
* SpilloverCount: number of requests rejected because surge queue is full (Classic only)

#### Exam Tips
* Metrics are published to CloudWatch
* Can create alarms
* Remember the different metric types

## Systems Manager 101

#### What is Systems Manager
* SSM is a management tool which gives you visibility & control over your AWS
infrastructure.
* Integrates with CloudWatch allowing you to view your dashboards, view operational
data & detect problems
* Includes Run Command which automates operational tasks across resources. e.g.
security patching, package installs
* Organize your inventory, group resources together by application and environment,
including on premise systems

#### Run Command
* Allows you to run pre-defined commands on one or more EC2 instances
* Stop, restart, terminate and resize instances
* Attach / detach EBS volumes
* Create snapshots, backup DynamoDB tables
* Apply patches and updates
* Run Ansible playbooks
* Run shell scripts

#### Systems Manager Lab
1. Need to create IAM role with the EC2 role with SSM permissions
2. Launch an instance with the role we just created
3. Go to Systems Manager and find all EC2 instances with a certain tag
4. Can then create a resource group for all EC2 instances with the tag
5. Can also access Config, CloudTrail, Personal Health Dashboard, and Trusted
Advisor from the Systems Manager dashboard
6. Can view Dashboards, Inventory of AWS resources, and Compliance
7. Can run automated tasks
8. Can run commands across EC2 instances
9. Can configure patches to run
10. Can schedule tasks to run at set times
11. You can manage on premise systems as well
12. Can access parameter store

#### Exam Tips
* Used to give visibilty and control over infrastructure
* Integrates with cloudwatch dashboards
* Allows you to organize inventory & logically group resources together
* Run Command enables you to perform common operational tasks on groups of 
instances simultaneously  

