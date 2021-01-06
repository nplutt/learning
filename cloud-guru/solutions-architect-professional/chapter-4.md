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



