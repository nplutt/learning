# Security

## Security Concepts
Principle of least privilege: Give users or services nothing more than those privileges required to perform their intended function.

#### Security Facets
| Facet | Description | AWS Example |
| ----- | ----------- | ----------- | 
| Identity | Who are you? | Root account user, IAM user, temporary security credentials |
| Authentication | Prove that you're who you say. | Multi-factor authentication, client side SSL certificate |
| Authorization | Are you allowed to do this? | IAM policies |
| Trust | Do other entities that I trust say they trust you? | Cross account access, SAML based federation, web identity federation |

#### SAML vs. OAuth vs. OpenID
SAML 2.0
* Can handle both authorization and authentication
* XML based protocol
* Can contain user, group membership and other useful information
* Assertions in the XML for authentication, attributes or authorization
* Best suited for Single Sign-on for enterprise users

OAuth 2.0
* Allow sharing of protected assets without having to send login credentials
* Handles authorization only, not authentication 
* Issues token to client
* Application validates token with Authorization Server
* Delegate access, allowing the client applications to access information on behalf of user
* Best suited for API authorization between apps

OpenID Connect
* Identity layer built on top of OAuth 2.0 adding authentication
* Uses REST/JSON message flows
* Supports web clients, mobile clients, javascript clients
* Extensible
* Best suited for Single Sign-on customer

#### Compliance 
AWS has implemented certain processes, practices, and standards as prescribed by many national and international standards bodies. These can be found in **AWS Artifact**.


## Multi-Account Management
* Most large organizations will have multiple AWS accounts
* Segregation of duties, cost allocation, increased agility
* Need methods to properly manage and maintain them

#### When should you use multiple accounts?
* Do you require administrative isolation between workloads?
* Do you require limited visibility and discoverability of workloads?
* Do you require strong isolation to minimize "blast radius"?
* Do you require string isolation of recovery and/or auditing data?

#### AWS Tools for Account Management
* AWS organizations
* Service control policies
* Tagging
* Resource groups
* Consolidated billing

#### Identity Account Structure
* Manage all user accounts in one location
* Users trust relationship from IAM roles in sub-accounts to Identity Account to grant temporary access
* Variations include by Business Unit, Deployment Environment, Geography

#### Logging Account Structure
* Centralized logging repository
* Can be secured so as to be immutable
* Can use Service Control Policies (SCP) to prevent sub accounts from changing logging settings

#### Publishing Account Structure
* Common repository for AMI's, Containers, Code
* Permits sub-accounts to use pre-approved standardized services as assets

##### Information Security Structure
* Hybrid of consolidated security and logging
* Allows one point of control and audit
* Logs cannot be tampered with by sub-account users

#### Central IT Account Structure
* IT can manage IAM users and groups while assigning to sub-account roles
* IT can provide shared services and standardized assets (AMI's databases, EBS, etc.) that adhere to corporate policy


## Network Controls & Security Groups

#### Security Groups
* Virtual firewalls for individual assets (EC2, RDS, AWS Workspaces, etc)
* Controls inbound and outbound traffic for TCP, UDP, ICMP, or custom protocols
* Port to port ranges
* Inbound rules are by Source IP, Subnet, or other Security Group
* Outbound rules are by Destination IP, Subnet, or other Security Group

#### Network Access Control List
* Additional layer of security for VPC that acts as a firewall
* Apply to entire subnets rather than individual assets
* Default NACL allows all inbound and outbound traffic
* NACLs are stateless - meaning outbound traffic simply obeys outbound rules - no connection is maintained
* Can duplicate or further restrict access along with security groups
* Remember ephemeral ports for outbound if you need them

 ##### Why use SG's and NACL's
 * NACLs provide a backup method of security if you accidentally change your SG to be too permissive
 * Covers the entire subnet wo users to create new instances and fail to assign a proper SG are still protected
 * Part of a multi-layer Least Privilege concept to explicitly allow or deny
 
 
 ## AWS Directory Services
 
 #### Types of Directory Services Offered
 | Directory Service Option | Description | Best for... |
 | ------------------------ | ----------- | ----------- |
 | AWS Cloud Directory | Cloud-native directory to share and control access to hierarchical data between applications | Cloud applications that need hierarchical data with complex relationships |
 | Amazon Cognito | Sign up and sign in functionality that scales to millions of users and federated to public social media services | Develop consumer apps or SaaS |
 | AWS Directory Service for Microsoft Active Directory | AW managed full Microsoft AS running on Windows Server 2012 R2 | Enterprises that want hosted Microsoft AS or tou need LDAP for Linux apps |
 | AD Connector | Allows on-premises users to log into AWS services with their existing AD credentials. Also allows EC2 instances to join AD domanin. | Single sign-on for on-prem employees and for adding EC2 instances to the domain |
 | Simple AD | Low scale, low cost AD implementation based on Samba | Simple user directory, or you need LDAP compatibility |
 
#### AD Connector vs. Simple AD
AD Connector:
* Must have existing AD
* Existing AS users can access AWS assets via IAM roles
* Supports MFa via existing RADIUS-based MFA infrastructure

Simple AD:
* Stand-alone AD based on Samba
* Supports user accounts, groups, group policies, and domains
* Kerberos-based SSO
* MFA not supported
* No trust relationships


## Credentials and Access Management
* Know what IAM is and components
* Users, Groups, Roles, Policies
* Resource based Policies vs Identity based Policies
* Know how to read and write policies in JSON
* Service -> Actions -> Resources

#### Token vending Machine Concept
* Common way to issue temporary credentials for mobile app development
* Anonymous TVM - Used as a way to provide access to AWS services only, doesn't store user identity
* Identity TVM - used for registration and login, and authorizations
* AWS now recommends that mobile developers use Cognito and related SDK

#### AWS Secrets Manager
* Store passwords, encryption keys, API keys, SSH keys, PGP keys, etc.
* Alternative to storing passwords or keys in a "vault"
* Can access secrets via API with fineg grained access control provided by IAM
* Automatically rotate RDS database credentials for MySQL, PostgreSQL, and Aurora
* Better than hard coding credentials in scripts or application


## Encryption

#### Key Management Service (KMS)
* Key storage, management and auditing
* Tightly integrated into many AWS services
* You can import your own keys or have KMS generate them
* control who manages and accesses keys via IAM users and roles
8 Audit use of keys via CloudTrail
* Differs from Secrets Manager as its purpose built for encryption key management
* Validated by many compliance schemes (PCI DSS Level 1, FIPS, 140-2 Level 2)

#### CloudHSM
* Dedicated hardware device, Single Tenanted
* Must be within a VPC and can access via VPC peering
* Does not natively integrate with many AWS services like KMS< but rather requires custome application scripting
* Offload SSL from web servers , act as an issuing CA, enable TDE for Oracle databases

| About | "Classing" CloudHSM | Current Cloud HSM |
| ----- | ------------------- | ----------------- |
| Device | safeNet Luna SA | Proprietary | 
| Pricing | Upfront cost required ($5000) | No upfront cost, pay per hour |
| High Availability | Have to buy second device | Clustered |
| Fip 140-2 | Level 2 | Level 3 |

#### CloudHSM vs KMS
| About | CloudHSM | AWS KMS |
| ----- | -------- | ------- |
| Tenancy | Single tenant HSM | Multi-tenant AWS service |
| Availability | Customer managed durability and available | Highly available and durable key storage and management |
| Root of Trust | Customer managed root of trust | AWS managed root of trust |
| FIPS 140-2 | Level 3 | Level 2 / Level 3 in some areas |
| 3rd Party Support | Broad 3rd party support | Broad AWS service support |

#### AWS Certificate Manager
* Managed service that lets you provision, manage, and deploy public or private SSL/TLS certificates
* Directly integrated into many AWS services like CloudFront, ELB, and API Gateway
* Free public certificates to use with AWS services; no need to register via a 3rd party certificate authority
* You can import 3rd party certificates for use in AWS
* Supports wildcard domains to cover all subdomains
* Managed certificate renewal 
* Can create a managed Private Certificate Authority as well for internal or proprietary apps, services or devices


## Distributed Denial of Service Attacks
* Amplification/Reflection Attacks
* Application Attacks (Layer 7)

#### Mitigating DDoS
| Best Practice | AWS Service |
| ------------- | ----------- |
| Minimize attack surface | NACLs, SGs, VPC design |
| Scale to absorb the attack | Auto-Scaling groups, AWS Cloudfront, Static web content via S3 |
| Safeguard exposed resources | Route53, AWS WAF, AWS Shield |
| Learn normal behavior | AWS GuardDuty, Cloudwatch |
| Have a plan | All you! |


## IDS and IPS

#### Intrusion Prevention and Detection
* Intrusion Detection System: watches the network and systems for suspicious activity that might indicate someone trying to compromise a system
* Intrusion Prevention System: tries to prevent exploits by sitting behind firewalls and scanning and analyzing suspicious content for threats.
* Normally compromised of a Collection / Monitoring system and monitoring agents on each system
* Logs collected or analyzed in CloudWatch, S3 or third-party tools (Splunk, SumoLogic, etc.) sometimes called a Security Information and Event Management (SIEM) system

 #### CloudWatch vs CloudTrail
 | CloudWatch | CloudTrail |
 | ---------- | ---------- |
 | Log events across AWS services; Think operations | Log API activity across AWS services; Think activities |
 | Higher-level comprehensive monitoring and venting | More low-level granular |
 | Log from multiple accounts | Log from multiple accounts |
 | Logs stored indefinitely | Logs stored to S3 or CloudWatch indefinitely |
 | Alarms history for 14 days | No native alarming; Can use CloudWatch alarms |
 
 
 ## Service Catalog
 
 #### AWS Service Catalog
 * Framework allowing administrators to create pre-defined products and landscapes for their users
 * Granular control over which users have access to which offerings
 * Make user of adopted IAm roles so users don't need underlying service access
 * Allows end users to be self-sufficient while upholding enterprise standards for deployments
 * Based on CloudFormation templates
 * Administrators can version and remove products. Existing running product versions will not be shutdown.
 
 #### AWS Service Catalog Constraints 
 | Type | What | Why |
 | ---- | ---- | --- |
 | Launch Constraint | IAM role that Service Catalog assumes when an end-user launches a product. | Without a launch constraint, the end-user mist have all permissions needed withing their own IAM credentials. |
 | Notification Constraint | Specifies the Amazon SNS topic to receive notifications about stack events. | Can get notifications when products are launched or have problems. |
 | Template Constraint | One or more rules that narrow allowable values an end-user can select. | Adjust product attributes based on choices a user makes. (Ex: Only allow certain instance types for dev environment) |

#### Multi-Account Scenarios
* Can create constraints to share across multiple accounts


## Exam Tips
Multi-Account Management: 
* Know the different models and best practices for cross-account management of security.
* Know how roles and trusts are used to create cross-account relationships and authorizations.

Network Controls and Security Groups:
* Know the differences and capabilities of NACLs and SGs
* NACLs are stateless
* Get some hands-on with NACLs and SGs to reinforce your knowledge
* Remember the ephemerals

AWS Directory Services:
* Understand the types of Directory Services offer by AWS - especially AD Connector and Simple AD
* Understand use-cases for each type of Directory Service
* Be familiar with how on-prem Active Directory implementation might connect to AWS and what functions that might enable

Credential and Access Management:
* Know IAM and its components
* Know how to read and write IAM policies in JSON
* Understand Identity Brokers, Federation, and SSO
* Know options and steps for temporary authorization

Encryption:
* Know differences between AWS KMS and CloudHSM and use cases
* Test will likely be restricted to the "classic" CloudHSM
* Understand AWS Certificate Manager and how it integrates with other AWS services

DDoS Attacks:
* Understand what they are and some best practices to limit your exposure
* Know some options to mitigate them using AWS services

IDS/IPS:
* Understand the difference between IDS and IPS
* Know what AWS services can help with each
* Understand the differences between CloudWatch and CloudTrail

Service Catalog:
* Know that it allows users to deploy assets through inheriting rights
* Understand how Service Catalog can work in a multi-account scenario

White Papers: 
* [AWS Best Security Practices](https://d1.awsstatic.com/whitepapers/aws-security-best-practices.pdf)
* [AWS Multi-Account Security Strategy](https://d1.awsstatic.com/aws-answers/AWS_Multi_Account_Security_Strategy.pdf)
* [AWS Best Practices for DDoS Resiliency](https://d1.awsstatic.com/whitepapers/Security/DDoS_White_Paper.pdf)
* [AWS Well Architected Framework - Security Pillar](https://d1.awsstatic.com/whitepapers/architecture/AWS-Security-Pillar.pdf?ref=wellarchitected)
* [Re:Invent Best Practices for Managing Security Operations](https://www.youtube.com/watch?v=gjrcoK8T3To&ab_channel=AmazonWebServices)
* [Re:Invent Become an IAM Policy Master](https://www.youtube.com/watch?v=YQsK4MtsELU&ab_channel=AmazonWebServices)
* [Re:Invent Security Anti-Patterns](https://www.youtube.com/watch?v=tzJmE_Jlas0&ab_channel=AmazonWebServices)
* [Re:Invent Architecting Security and Governance Across a Multi-Account](https://www.youtube.com/watch?v=71fD8Oenwxc&ab_channel=AmazonWebServices)
* [Re:Invent Managing Multi-Account AWS Environments Using AWS Organizations](https://www.youtube.com/watch?v=fxo67UeeN1A&ab_channel=AmazonWebServices)


## Pro Tips
* Know that security will be front-of-mind for every client evaluating the cloud ... but rarely are there sound processes in place
* Acknowledge concerns and be ready with a process (Cloud Adoption Framework is a good start)
* Leverage assessments and checklists as illustrators of care and best practice
* Migrating to the cloud is often more secure than on-prem due to increased transparency and visibilty
* Speak in terms of risk as a continuum rathe than an absolute
* Consider AWS Certified Security - Specialty or other security minded certification like CISSP


## Challenges
* Question 1:
    - My Answer: C, F, H
    - Correct Answer: A, C, F
    
* Question 2:
    - My Answer: B, F
    - Correct Answer: B, F
