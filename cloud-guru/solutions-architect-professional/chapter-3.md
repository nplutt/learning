# Networking

## Concepts

#### Networking Refresher
You should already know:
* Physical layout of AZs and regions
* VPC concept and how to create
* Create private and public subnets
* What a NAR is and what "Disable Source/Destination Checks" means
* Routing table and routing terminology (default routes, local routes)
* IPv4 Addressing and subnet mask notation (/16, /24, etc.)
* Intermediate networking terminology (MAC address, port, gateway vs router)

#### OSI Model
| Layer | Name | Example | Mnemonic |
| ----- | ---- | ------- | -------- |
| 7 | Application | Web Browser | Away|
| 6 | Presentation | TLS/SSL, Compression | Pizza |
| 5 | Session | Setup, Negotiation, Teardown | Sausage |
| 4 | Transport | TCP | Throw |
| 3 | Network | IP, ARP | Not |
| 2 | Data Link | MAC | Do |
| 1 | Physical | Cat5, fiber optic cable, 5GHz carrier frequency | Please |

AWS is responsible for layers 1 & 2, customers are responsible for layers >= 3

#### Unicast vs. Multicast
Most cloud providers do not allow multicast

Unicast: Think of this as a direct conversation between two people over a telephone line. It doesn't interrupt anyone else.

Multicast: Think about this as someone shouting over a loud speaker to everyone, it is very disruptive. Multicast is when a 
network card starts sending messages to everyone on the network and because this is done at the MAC address level it's a 
layer 2 activity so if AWS allowed Multicast it could negatively affect other customer's network activity as well. Multicast 
doesn't fly officially on VPC.

#### VCP vs UDP vs ICMP
| Protocol | Characteristics | Plain Speak | Uses |
| -------- | --------------- | ----------- | ---- |
| TCP (layer 4) | Connection-based stateful, acknowledges receipt | After everything I say, I want you to confirm that you received it. | Web, Email, File Transfer |
| UDP (layer 4) | Connectionless, stateless, simple, no retransmission delays | I'm going to start talking and its ok af you miss some words | Streaming media, DNS |
| ICMP (layer 3, some people debate this though) | Used by network devices to exchange info | We routers can keep in touch about the health of the network using our own language | tracerouting, ping |

#### Ephemeral Ports
* Short lived transport protocol ports used in IP communications 
* Above the well-known IP ports (above 1024)
* "Dynamic Ports"
* Suggested range is 49152 to 65525 but...
    - Linux kernels generally use 32568 to 610000
    - Windows platforms default from 1025
* NACL and security group implications

#### Reserved IP Addresses
* AWS uses certain IP addresses in each VPC as reserved - you can't use them.
* 5 IPs are reserved in every VPC subnet (example: 10.0.0.0/24)
    - 10.0.0.0: Network address
    - 10.0.0.1: Reserved by AWS for the VPC router
    - 10.0.0.2: Reserved by AWS for Amazon DNS
    - 10.0.0.3: Reserved by AWS for future use
    - 10.0.0.255: VPCs don't support broadcast so AWS reserves this address
 * Example: 192.168.8.16/28
    - 192.168.8.16: Network address
    - 192.168.8.17: Reserved by AWS for the VPC router
    - 192.168.8.18: Reserved by AWS for Amazon DNS
    - 192.168.8.19: Reserved by AWS for future use
    - 192.168.8.20 to 192.168.8.30: Usable
    - 192.168.8.31: VPCs don't support broadcast so AWS reserves this address

#### AWS Availability Zones
* The physical to logical assignment of AZ's is done at the account level
* Assignments are set at account creation time

## Network to VPC Connectivity

#### Amazon Global network
Watch reinvent video on [Global Network](https://www.youtube.com/watch?v=uj7Ting6Ckk&ab_channel=AmazonWebServices)

#### AWS Managed VPN
* What: AWS managed Ipsec VPN connection over your existing internet 
* When: Quick and usually simple way to establish a secure tunneled connection to a VPC; Redundant link for Direct Connect or other VPC VPN 
* Pros: Supports static routes or BGP peering and routing 
* Cons: Dependent on your internet 
* How: 
    1. Designate an appliance to act as your customer gateway (usually your on-prem router)
    2. Create the VPN connection in AWS and download the configuration file for your customer gateway.
    3. Configure your customer gateway using the information from the configuration file.
    4. Generate traffic from your side of the VPN connection to bring up the VPN tunnel

#### AWS Direct Connect
* What: Dedicated network connection over private lines straight into AWS backbone
* When: Require a "big pipe" into AWS; lots of resources and services being provided on AWS to your corporate users
* Pros: More predictable network performance; potential bandwidth cost reduction; up to 10 Gbps provisioned connections; Supports BGP peering and routing
* Cons: May require additional telecom and hosting provider relationships and or new network circuits
* How: Work with your existing Data Networking Provider; Create Virtual Interfaces (VIF) to connect to VPCs (private VIF) or other AWS service like S3 or Glacier (public VIF)

#### AWS Direct Connect Plus VPN
* What: IPsec VPN connection over private lines
* When: Want added security of encrypted tunnel over direct connect
* Pros: More secure in theory than direct connect alone
* Cons: More complexity introduced by the VPN layer
* How: Work with your existing Data Networking Provider

#### AWS VPN Cloud Hub
* What: Connect locations in a hub and spoke manner using AWS's Virtual Private Gateway
* When: Link remote offices for backup or primary WAN access to AWS resources and each other
* Pros: Reuses existing Internet connection; Supports BGP routes to direct traffic (for example, use MPLS first then Cloudhub VPN as backup)
* Cons: Dependent on internet connection; No inherent redundancy
* How: Assign multiple Customer Gateways to a Virtual Private Gateway, each with their own BGP ASN and unique IP ranges

#### Software VPN
* What: You provide your own VPN endpoint and software
* When: You must manage both ends of the VPN connection for compliance reasons or you want to use a VPN option not supported by AWS
* Pros: Ultimate flexibility and manageability
* Cons: You must design for any needed redundancy across the whole chain
* How: Install VPN software via Marketplace appliance or on an EC2 instance

#### Transit VPC
* What: Common strategy for connecting geographically disperse VPCs and locations in order to create a global network transit center
* When: Locations and VPC-deployment assets across multiple regions that need to communicate with one another
* Pros: Ultimate flexibility and manageability but also AWS managed VPN hub and spoke between VPCs
* Cons: You must design for any needed redundancy across the whole chain
* How: Providers like Cisco, Juniper Networks and Riverbed have offerings which work with their equipment and AWS VPC


## VPC to VPC Connectivity

#### VPC Peering
* What: AWS-provided network connectivity between two VPCs
* When: Multiple VPCs need to communicate or access each others resources
* Pros: Uses AWS backbone without touching internet
* Cons: If A is connected to B and B is connected to C, A cannot talk to C via B. (transitive peering not supported)
* How: VPC Peering request is made; Accepter accepts request (either within account or across accounts)

#### AWS Private Link
* What: AWS-provided network connectivity between VPCs and or AWS services using interface endpoints
* When: Keep Private Subnets truely private by using the AWS backbone to reach other services rather than the public internet
* Redundant: uses AWS backbone
* How: Create Endpoitn for needed AWS or MArketplace service in all needed subnets; access via the provided DNS hostname

#### VPC Endpoints
| Question | Interface Endpoint | Gateway Endpoint |
| -------- | ------------------ | ---------------- |
| What | Elastic Network Interface with private IP | A gateway that is a target for a specific route |
| How | Uses DNS entries to redirect traffic | Uses prefix list in the rout table to redirect traffic |
| What Products | API Gateway, CloudFormation, Cloudwatch, etc. | S3, DynamoDB |
| Securing | Security Groups | VPC Endpoint Policies |


## Internet Gateways
* Horizontally scaled, redundant and highly available component that allows communication between your VPC and the internet
* No availability risk or bandwidth constraints
* If your subnet is associated with a route to the internet, then it is a public subnet
* Supports IPv4 and IPv6

Purpose:1: Provide route table target for internet bound traffic
Purpose 2: Perform NAT for instances with public IP addresses

Does not perform NAT for instances with only a private IP assigned

#### Egress-Only Internet Gateway
* IPv6 addresses are globally unique and are therefore public by default
* Provides outbound internet access for IPv6 addressed instances
* Prevents inbound access for those IPv6 instances
* Stateful - forwards traffic from instance to internet and then sends back the response
* Must create a custome toute for ::/0 to the Egress-Only internet gateway
* Use Egress-Only internet gateway instead of NAT for IPv6

#### NAT Instance
* EC2 instance from a special AWS provided AMI
* Translate traffic from many private IP instance to a single public IP and back
* Doesn't allow for public Internet initiated connections into private instances
* Not supported for IPv5 (use Egress-Only gateway)
* NAT instance must live on a public subnet with route to internet gateway
* Private instances in private subnet must have route to the NAT instance, usually the default route destination of 0.0.0.0/0

#### NAT Gateway
* Fully managed NAT service that replaces need for NAT instance on EC2
* Must be created in public subnet
* Uses Elastic IP for public IP for the life of the Gateway
* Private instances in private subnet mist have route to the NAT Gateway, usually the default route destination of 0.0.0.0/0
* Created in specified AZ with redundancy in that zone
* For multi-AZ redundancy, create NAT gateways in each AZ with routes for private subnets to use the local gateway
* Up to 5Gbps bandwidth that can scale up to 45 Gbps
* Can't use a NAT Gateway to access VPC peering, VPN or Direct Connect, so be sure to include specific routes to those in your route table

#### NAT Gateway vs NAT Instance
| Info | NAT Gateway | NAT Instance |
| ---- | ----------- | ------------ |
| Availability | Highly available within AZ | On your own |
| Bandwidth | Up to 45 Gbps | Depends on bandwidth of instance type |
| Maintenance | Managed by AWS | On your own |
| Performance | Optimized for NAT | Amazon Linux AMI configured to perform NAT |
| Public IP | Elastic IP that cannot be detached | Elastic IP that can be detatched |
| Security Groups | Cannot be associated with NAT gateway | CAn use Security Groups |
| Bastion Server | Not Supported | Can be used as bastion server |
 
 
 ## Routing 
 
 #### Routing Tables
* VPCs have an implicit router and main routing table
* You can modify the main routing table or create new tables
* Each route table contains a local route for the CIDR block
* Most specific route for an address wins

#### Border Gateway Protocol
* Popular routing protocol for the internet
* Propagates information about the network to allow for dynamic routing
* Required for direct connect and optional for VPN
* Alternative of not using BGP with AWS VPC is static routes
* AWS supports BGP community tagging as a way to control traffic scope and route preference
* Required TCP port 179 + ephemeral ports (remember these?)
* Autonomous System Number (ASN) = Unique endpoint identifier
* Wighting is local to the router and higher weight is preferred path for outbound traffic


## Enhanced Networking
* Generally used for high performance computing use cases
* Uses single root I/O virtualization (SR-IOV) to deliver higher performance than traditional virtualized network interfaces
* Might have to install driver if not using Amazon Linux HVM AMI
* Two types:
    - Intel 82599 VF Interface (10 Gbps)
    - Elastic Network Adapter (25 Gbps)

#### Placement Groups
| Question | Clustered | Spread | Partition |
| -------- | --------- | ------ | --------- |
| What | Instances are placed into a low-latency group within a single AZ | Instances spread across underlying hardware | Instances are grouped into partitions and spread across racks |
| When | Need low network latency and or high network throughput | Reduce risk of simultaneous failure if underlying hardware fails | Reduce risk of correlated hardware failure for multi-instance workloads |
| Pros | Get the most out of Enhanced Networking Instances | Can span multiple AZ's | Better for large distributed or replicated workloads than Spread |
| Cons | Finite capacity: recommend launching all you might need up front | Max of 7 instances running per group per AZ | Not supposed for Dedicated Hosts|


## Route 53
* Register domain names
* Check the health of your domain resources
* Route internet traffic for your domain

What you should already know:
* What is DNS?
* DNS record types (A, CNAME, MX, TXT, etc.)
* Route53 concepts (alias, hosted zone, etc.)
* Why is it called Route 53?

#### Route 53 Routing Policies
| Policy | Route 53 is thinking... |
| ------ | ----------------------- |
| Simple | Sinple. Here's the detination for that name. |
| Failover | Normally, I'd route you to <Primary>, but it appears down based on my health checks so I'll failover to <Backup> |
| Geolocation | Looks like you're in Europe, so I'm going to route you to a resources closer to you in that region. |
| Geoproximity | You're closer to the us-east-1 region than us-west-2 so I'll route you to us-east-2 |
| Latency | Let me see which resources has lower latency for you, the I'll direct you that way. |
| Multivalue Answer | I will return several IP addresses, as a sort of basic load balancer |
| Weighted | You can setup multiple resources and I'll route according to the percentage of weight you assigned each |

#### Weighted Routing
 Weighted traffic formula: Weight for a specified record / Sum of all weights for all records = percentage of traffic


## Cloudfront
* Distributed content delivery service for simpel statuc asset caching up to 4k live and on-demand video streaming
* You should already know how to create a CloudFront distribution and understand edge location concept
* Integrated with Amazon Certificate Manager and supports SNI (Server Name Indication)


## Elastic Load Balancers
* Distributes inbound connections to one or many backend endpoints
* Three different options:
    - Application Load Balancer (L7)
    - Network Load Balancer (L4)
    - Classic Load Balancer (L4 or L7)
* Can be used for public or private workloads
* Consume IP addresses within a VPC subnet

#### Elastic Load Balancer - Similarities
All load balancers support the following:
* Zonal Failover
* Health Checks
* Cross-Zone Load Balancing
* CloudWatch Metrics
* SSL Offloading
* Resource-based IAM Permissions

ALB & NLB are VPC only

Classic LB is EC2-Classic or VPC

#### Elastic Load Balancer
| What | Application LB | Network LB | Classic LB |
| ---- | -------------- | ---------- | ---------- |
| Protocols | HTTPS, HTTP | TCP, UDP, TLS | TCP, SSL, HTTP, HTTPS |
| Path or Host Based Routing | Yes | No | No |
| WebSockets | Yes | Yes | No |
| Server Name Indication (SNI) | Yes | Yes | No |
| Sticky Sessions | Yes | Yes | Yes |
| Static IP, Elastic IP | Only through AWS Global Accelerator | Yes | No |
| User Authentication | Yes | No | No |

#### Elastic Load Balancers - Routing
NLB:
* Port number
* RCP connections to backend are persisted for the duration of the connection 

ALB: 
* Host based routing 
* Path based routing 
* HTTP header based routing 
* HTTP method based routing 
* Query string parameter based routing
* Source IP address CIDR based routing


## Exam Tips
VPCs in General:
* Know the pros and cons of each On-prem to AWS connection mode
* Know the functions of the different VPC components (Customer Gateway, Virtual Private Gateway)
* Know that Direct Connect is not inherently redundant, so know how to architect a network that is (VPN, secondary direct connect)
* Multicast and Broadcast aren't supported in VPCs
* Know what is meant by "stateless", "stateful", "connectionless" and "connection-based" in terms of IP protocols
* Know what ephemeral ports are and why they might need to be in NACLs or SGs

Routing:
* Understand BGP and how to use weighting to shift network traffic
* Know how routes in a route table are prioritized (most specific first)
* What other routing protocols does AWS support (none... only BGP)

VPC Peering:
* CIDR ranges cannot overlap
* After VPC owner accepts a peering request, routes must be added to respective route tables
* Transitive peering is not supported, but mesh or hub-and-spoke architectures are ... with proper NACLs and routes
* A Transit VPC is supported

Internet Gateways:
* Difference between NAT instance and NAT Gateway
* Internet Gateway is horizontally scaled, redundant, with no bandwidth constraints
* NATs do have bandwidth constraints but...
* VPCs can have multiple NATs across AZs and subnets for scale - so long as routes are defined properly
* Use Egress-Only Gateway for IPv6

Route 53:
* Understand different types of routing policies and use cases
* Know the weighted routing formula
* Route 53 is a global service

CloudFront:
* Understand what must happen to use a custom domain with CloudFront
* Understand what SNI enables and the necessary alternatives

Elastic Load Balancer:
* Know the three different types of Load Balancers and which OSI Layer they work on
* Understand which major features each deliver (protocol, SNI, Sticky Sessions)
* Know what Sticky Sessions are and when they come into play

White Papers:
* [Amazon Virtual Private Cloud Connectivity Options](https://d0.awsstatic.com/whitepapers/aws-amazon-vpc-connectivity-options.pdf)
* [Integrating AWS with Mutiprotocol Label Switching](https://d1.awsstatic.com/whitepapers/Networking/integrating-aws-with-multiprotocol-label-switching.pdf)
* [Security in Amazon Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/security.html)
* [Re:Invent Networking Many VPCs: Transit and Shared Architectures](https://www.youtube.com/watch?v=KGKrVO9xlqI&ab_channel=AmazonWebServices)
* [Re:Invent Another Day, Another Billion Flows](https://www.youtube.com/watch?v=8gc2DgBqo9U&ab_channel=AmazonWebServices)
* [Re:Invent Deep Dive into the New Network Load Balancer](https://www.youtube.com/watch?v=z0FBGIT1Ub4&ab_channel=AmazonWebServices)


## Pro Tips:
* Direct Connect may be a more complex and costlier option to setup, but it could save big on bandwidth costs
* Explicitly deny as much traffic as you can with NACLs and SC-Principle of Least Privilege
* Think through your VPC layout (See Re:Invent video)
* You can use Route 53 for tour domain even if AWS isn't your registrar
* ELBs provide a useful layer of abstraction (as does Route 53 too!)


## Challenges
* Question 1:
    - My Answer: C, E, F
    - Correct Answer: C, F, H
    
    It's not E because there is not bandwidth limit for Internet Gateways
    
* Question 2:
    - My Answer: E
    - Correct Answer: E

