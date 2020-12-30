# Networking
## VPC Overview

#### What is a VPC?
Think of a VPC as a virtual data centre in the cloud

#### VPC - AWS Definition
Amazon virtual private cloud (Amazon VPC) lets you provision a logically isolated
section of AWS Cloud where you can launch resources in a virtual network that you
define. You have complete control over your virtual network environment, including
selection of your own IP address rance, creation of subnets, and configuration
of route tables and network gateways

Additionally you can create VPN connections between your corporate datacenter and
your VPC and leverage the AWS cloud as an extension of your corporate datacenter.

VPC Prefixes:
* 10.0.0.0 - 10.255.255.255 (10/8 prefix) - Most addresses
* 172.16.0.0 - 172.32.255.255 (173.16/ prefix)
* 192.168.0.0 - 192.168.255.255 (192.168/16 prefix) - Least addresses

#### What can you do with a VPC?
* Launch instances into a subnet of your choosing
* Assign custom IP address ranges in each subnet
* Create route travels between subnets
* Create internet gateway and attach it to our VPC
* Much better security control over AWS resources
* Instance security groups
* Subnet network access control lists

#### Default VPC vs Custom VPC
* Default VPC is user friendly, allowing you to immediately deploy instances
* All subnets in default VPC have route out to the internet
* Each EC2 instance has both a public and private IP address

#### VPC Peering
* Allows you to connect one VPC with another via a direct network route using 
private IP address
* Instances behave as if they were on the same private network
* You can peer VPC's with other AWS accounts as well as with other VPCs in the same
account
* Peering ins ina star configuration: ie 1 central VPC peers with 4 others. NO 
TRANSITIVE PEERING!!
  - Meaning a VPC can only communicate with one another if they're peered. If
  VPC A is peered with VPC B and VPC B is peered with VPC C, VPC A can't communicate
  with VPC C unless they're peered as well.
  
#### Exam Tips
* Think of a VPC as a logical datacenter in AWS
* Consists of IGWs, Route tables, Network Access Control Lists, Subnets, and 
Security Groups
* 1 subnet = 1 AZ
* Security Groups are stateful; Network Access Control Lists are Stateless
* No transitive peering

## VPC Lab

#### Notes
The 1st 4 and last IP address in each subnet are not available for you to use, and
cannot be assigned to an instance.
* 10.0.0.0: network address
* 10.0.0.1: reserved by AWS for the VPC router
* 10.0.0.2: reserved by AWS, the IP address of the DNS server is always the base of 
the VPC network range plus 2
* 10.0.0.3: reserved for future use
* 10.0.0.255: network broadcast address, this is reserved since AWS doesn't support
broadcast in a VPC

## NAT Instances & NAT Gateway

#### Exam Tips
Nat Instances
* When creating a NAT instance, Disable Source/Destination Check on the instance
* NAT instances must be in a public subnet
* There must be a route out of the private subnet to the NAT instance, in order for
this to work
* The amount of traffic that NAT instances can support depends on the instance size.
If you are bottlenecking, increase the instance size.
* You can create high availability using Autoscaling Groups, multiple subnets in
different AZs, and a script to automate failover.
* Behind a security group

Nat Gateway
* Preferred by the enterprise
* Scale automatically up to 10 Gbps
* No need to patch
* Not associated with security groups
* Automatically assigned to a public ip address
* Remember to update your route tables
* No need to disable Source/Destination Checks
* More secure than a NAT instance

## Network Access Control Lists & Security Groups

#### Notes
* By default when you create a NACL, all traffic is blocked
* All NACL rules start at 100 and go up in increments of 100
* Ephemeral ports:
  - Many linux kernels use ports 32768-61000
  - Requests originating from an ELB use ports 1024-65535
  - Windows uses ports: 49152-65535
  - NAT Gateways use ports: 1024-65535
* NACL rules are evaluated in numerical order, so if you have rule 100 and 101,
rule 100 is evaluated before 101

#### Exam Tips - Network ACLs
* Your VPC automatically comes with a default network ACL, and by default it allows
all outbound and inbound traffic
* You can create custom network ACLs. By default, each custom network ACL denies all
inbound and outbound traffic until you add rules.
* Each subnet in your VPC must be associates with a network ACL. If you don't 
explicitly associate a subnet with a network ACL, the subnet is automatically 
associated with the default network ACL.
* You can associate a network ACL with multiple subnets; however, a subnet can be 
associated with only one network ACL at a time. When you associate a network ACL
with a subnet, the previous association is removed.
* Network ACLs contain a numbered list of rules that is evaluated in order, 
starting with the lowest numbered rule.
* Network ACLs have separate inbound and outbound rules, and each rule can either
allow or deny traffic.
* Network ACLs are stateless; responses to allowed inbound traffic are subject to
the rules for outbound traffic (and vice versa)
* Block IP Addresses using network ACLs not security groups

## VPC Endpoints

#### Notes
A VPC endpoint enables you to privately connect your VPC to supported AWS services
and VPC endpoint services powered by PrivateLink without requiring an internet gateway,
NAT device, VPN connection, or AWS Direct Connect connection. Instances in your
VPC do not require public IP addresses to communicate with resources in the service.
Traffic between your VPC and the other service doesn't leave the Amazon network.

There are 2 types of VPC endpoints:
* Interface endpoints: an elastic network interface with a private IP address that
serves as an entry point for traffic destined to a supported service.
* Gateway endpoint: is a gateway that is a target for a specified route in your 
route table, used for traffic destined to a supported AWS service.

## VPC Flow Logs

#### What are VPC Flow Logs?
They are a feature that enables you to capture information about the IP traffic
going to and from network interfaces in your VPC. Flow log data is stored using
CloudWatch. After you've created a flow log, you can view and retrieve it's data
in CloudWatch.

They can be created at 3 different levels:
* VPC
* Subnet
* Network Interface Level

Can be used to debug a number of issues:
* Why specific traffic isn't reaching an instance
* Diagnose overly restrictive security groups

#### Exam Tips
* You can't enable flow logs for VPCs that are peered with your VPC unless the peer
VPC is in your account
* You can't tag a flow log
* After creating a flow log, you can't change it's config; for example, you can't
associate a different IAM role with the flow log.

Not all IP traffic is monitored:
* Traffic generated by instances whn they contact the Amazon DNS server. If you 
use your own DNS server, then all traffic to that DNS server is logged.
* Traffic generated by a Windows instance for Amazon Windows license activation
* Traffic to and from 169.254.169.254 for instance metadata
* DHCP traffic
* Traffic to the reserved IP address for the default VPC router

## CIDR Calculations

#### Calculating CIDR Blocks
Need to know how many IP addresses are available
* /24 = 256
* /25 = 128
* /26 = 64
* /27 = 32
* /28 = 16 (Lowest you can go in AWS)
* /29 = 8
* /30 = 4
* /31 = 2
* /32 = 1

Note that there will always be 5 less than the number displayed

#### Exam Tips
Remember thr following:
* Max size of subnet for VPC is /16
* Min size of subnet for VPC is /29
* Amazon reserves 4 addresses + broadcast address = 5

## Direct Connect Gateways

#### Exam Tips
If you have a VPC in us-east-1 and it has a direct connect connection to a 
customer network, and you want to add us-west-1, don't add another direct connect,
instead add a direct connect gateway.

## DNS 101

#### What is DNS?
If you've used the internet, you've used DNS. DNS is used to convert human friendly
domain names into IP addresses. Think about it as a phone book.

#### IPv4 VS IPv6
The IPv4 space has a 32 bit field and has over 4 billion addresses

IPv6 was created to solve the depletion issue and has an address space of 128 bits,
which in theory is 340 undecillion addresses

#### Top level Domains
If we lok at common domain names such as google.com, acloud.guru, etc. you will notice
a string of chars separated by dots. The last word in the domain nae represents
the "top level domain". The second word in a domain name is know as the second level
domain name (this is optional though and depends on the domain name)

These top level domain names are controlled by the Internet Assigned Numbers 
Authority (IANA) is a root zone database which is essentially a database of all
available top levl domains.

#### Domain Registrars
Because all of the dames in a given domain name have to be unique there needs to 
be a way to organize this all so that domain names aren't duplicated. This is 
where domain registrars come in. A registrar is an authority that can assign
domain names directly under on or more top level domains. These domains are 
registers with InterNIC a service of ICANN, which enforces uniqueness of domain
names across the internet. Each domain name becomes registered in a central DB 
known as the WhoIS database. 

Because DNS operates on port 53 that's why Amazon named Rote 53.

#### Start Of Authority Record (SOA)
The SOA record stores information about:
* The name of the server that supplied the data for the zone
* The administrator of the zone
* The current version of the data file
* The default number of seconds for the time-to-alive file on resource records

#### NS Records
NS stands for Name Server records. They are used by tip level domain servers to
direct traffic to the content DNS server which contains the authoritative DNS
records.

#### A Record
The A record is the fundamental type of DNS record. The A in the A record stands 
for address. The A record is used by computer to translate the name of the domain 
to the IP address.

#### TTL
The length that a DNS record is cached on either the Resolving Server of the users
own local PC is equal to the Time to Live in seconds. The lower the time to live,
the faster changes to DNS records take to propogate throughout the internet.

#### CNAMES
A CName can be used to resolve one domain name to another. For example, you may
have a mobile website with the domain name http://m.website.com that is used for
when users browse to your domain name on their mobile devices. You may also 
want the name http://mobile.website.com to resolve to the same address.

#### Exam Tips
* ELBs do not have a pre-defined IPv4 addresses; you resolve to them using a 
DNS name
* Understand the difference between an Alias record and a CNAME
* Given the choice, always choose an Alias record over a CNAME
* SOA record info
* Alias record info

## Weighted Routing Policy

#### Weighted Routing
* Allows you to specify 20% goes to one AZ and 80% goes to another

## Latency Based Routing
* Create an ELB or EC2 instance in each region that you want, then create a 
latency based record set for each instance. Then Route53 will choose to route
users to the region with the lowest latency.

## Geolocation
* Will route users to AZ depending on their Geolocation

## Multivalue Answer
You can list multiple ip addresses and have the traffic routed randomly to the 
servers

## Exam Tips

#### Notes
Remember all of the different routing policies and what they do