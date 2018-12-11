# Security & Compliance

## Compliance on AWS

#### Compliance Frameworks
* PCI
* ISO
* HIPPA

More notes at: https://aws/amazon.com/compliance

#### ISO 27001:2005/10/13
Specifies the requirements for establishing, implementing, operating, monitoringm
reviewing, maintaining and improving a document Information Security Management 
System within the context of the organization's overall business risks

#### FedRAMP
The Federal Risk and Authorization Management Program, or FedRAMP, is a govt wide
program that provides a standard approach to security assessment, authorization, and
continuous monitoring for cloud products and services.

#### HIPPA 
Is the federal health insurance portability and accountability of 1996. The primary
goal of the law is to make it easier for people to keep health insurance, protect
the confidentiality of information and help the healthcare industry control 
administrative costs.

#### PCI
The payments card industry data security standard (PCI DSS) is a widely accepted set
of policies and procedures intended to optimize the security of credit, debit and 
cash card transactions and protect card holders against misuse of their personal
information.

#### PCI DSS v3.2
Build and maintain a secure network and systems
* requirement 1: install and maintain a firewall configuration to protect cardholder
data
* requirement 2: do not use vendor supplied defaults for system passwords and other
security params
* requirement 3: protect and store cardholder data
* requirement 4: encrypt transition of cardholder data across public networks
* requirement 5: protect all systems against malware and regularly update
anti-virus software
* requirement 6: develop and maintain secure systems and applications
* requirement 7: restrict access to cardholder data by business need to know
* requirement 8: identify and authenticate access to system components
* requirement 9: restrict physical access to cardholder data
* requirement 10: track and monitor all access to network resources and cardholder
data
* requirement 11: regularly test security systems and processes
* requirement 12: maintain a policy that addresses information security for all 
personnel

## DDos

#### AWS DDOS White Paper
https://d1.awsstatic.com/whitepapers/Security/DDoS_White_Paper.pdf

#### Amplification / Reflection Attacks
These can include things such as NTP, SSDP, DNS, Chargen, SNMP attacks, etc. and is
where an attacker may send a third party (such as an NTP server) a request using 
a spoofed IP address. jThat server will then usually respond to that request with
a greater payload than the initial request (usually within the region of 28 x 54 
times larger than the request) to the spoofed IP address.

This means that if the attacker sends a packet with a spoofed IP address of 64
bytes, the NTP server would respond with up to 3456 bytes of traffic. Attackers
can co-ordinate this using multiple NTP servers and a second to send legit NTP
traffic to the target.

#### Application Attacks (L7)
* Flooding the webserver with GET requests

Slowloris Attack
* Attacker sends connection requests that stay open for as long as possible
* Causing gateway to stay open and fills max concurrent connection pool

#### How to mitigate against DDoS
* Minimize attack surface area
* Be ready to scale and absorb attack
* Safeguard exposed resources
* Learn the normal behavior
* Create a plan for attacks

#### AWS Shield
* Free service that protects all AWS customers on ELB, Amazon Cloudfront, and 
Route53
* Protects against SYN/UDP floods, Reflection attacks, and other layer 3/4 attacks
* Advanced provides enhanced protections for your apps running on ELB, 
CloudFront, and Route 53 against larger and more sophisticated attacks. ($3000 per
month)

Advanced:
* Provides near real time notifications of an attack
* DDoS response team will help mitigate and manage application layer attacks
* Protects your bill from higher fees during the attack
* $3000 per month

## AWS Marketplace - Security Products

#### Security Products
* Can purchase stuff from 3rd party vendors
* Firewalls, Hardened OS, WAF's, Antivirus, Security Monitoring
* Free, Hourly, Monthly, Annual
* CIS OS Hardening

## STS

#### STS
Grants users limited and temp access to AWS resources. Users can come from 3
sources:
* Federation (Typically Active Directory)
  - Uses security assertion markup language (SAML)
  - Grants temp access based off users AD credentials. Doesn't need to be a user
  in IAM.
  - Single sign on allows users to login to AWS console without assigning IAM
  credentials
* Federation with mobile apps
  - Use facebook/amazon/google or other OpenID providers to login
* Cross Account Access
  - Lets users from one account access resources in another

#### Understanding Key Terms
* Federation: combining or joining a list of users in one domain, such as IAM with
a list of users in another domain (such as AD, Facebook, etc.)
* Identity Broker: a service that allows you to take an identity from point A and
joint it (federate it) to point B
* Identity Store: services like AD, Facebook, Google, etc
* Identities: a user of a service like Facebook etc.

#### Scenario
You are hosting a company website on some EC2 web servers in your VPC. Users of the
website must login yo the site which then authenticates against the companies AD
servers which are based on site at the companies head quarters. Your VPC is connected
to your company HQ via a secure IPSEC VPN. Once logged in the user can only have
access to their own S3 bucket. How would you set this up?

1. Employee enters username and password
2. App calls identity broker
3. Identity broker uses the organizations LDAP directory to validate the employee's 
identity
4. IB calls the new GetFederationToken function using the IAM credentials. The 
call must include an IAM policy and a duration, along with a policy that
specifies the permissions to be granted to the temporary security credentials.
5. The STS service confirms that the policy of the IAM user making the call to 
GetFederatedToken gives permission to create new tokens and then returns 4 values 
to the application: an access key, a secret access key, a token, and a duration
6. The IB returns the temp security credentials to the reporting application
7. The data storage app uses the temp security credentials to make requests to S3
8. S3 uses IAM to verify that the credentials allow the requested operation on the
given S3 bucket and key
9. IAM provides S3 with the approval to perform the requested operation

## Logging

#### Services
* CloudTrail
* Config
* CloudWatch
* VPC Flow Logs

#### Control Access to Log Files
Prevent unauthorized access:
* IAM users, groups, roles and policies
* S3 bucket policies
* Muli factor auth

Ensure role based access:
* IAM users, groups, roles and policies
* S3 bucket policies

#### Obtain Alerts on Log File Creation and Misconfiguration
Alerts when logs are created or fail:
* Cloudtrail notifications
* AWS config rules

Alerts are specific, but don't divulge detail:
* Cloudtrail SNS notifications ony point to log file location

#### Manage Changes to AWS Resources and Log Files
Log changes to system components:
* AWS Config rules
* Cloudtrail

Controls exist to prevent modifications to logs
* IAM and S3 controls
* Cloudtrail log file validation
* Cloudtrail log file encryption

## AWS Hypervisors, Isolation of AWS Resources and AWS Firewalls

#### The AWS Hypervisor
A hypervisor or virtual machine monitor (VMM) is a software, firmware or 
hardware that creates and runs virtual machines. A computer on which a 
hypervisor runs one or more VMs is called a host machine, and each VM is a
guest machine.

EC2 runs on the Xen Hypervisor.

#### Exam Tips
* Choose HVM ove PV when possible
* PV is isolated by layers, Guest OS sits on Layer 1, Application on Layer 3
* Only AWS admins have access to hypevisors
* AWS staff do hot have access to EC2
* All storage memory and RAM memory is scrubbed before it's delivered to you.

## EC2 Dedicated Instances VS Dedicated Hosts?

#### What are EC2 dedicated instances?
These are physically isolated instances at the hardware level. Dedicated instances
from the same account may share hardware with other instances within the same 
AWS account that are not dedicated instances.

#### What are EC2 dedicated hosts?
These are instances that allow you to deploy your instances to the same physical
host every time. This is good for stuff like Oracle and other bad tools.

#### Exam Tips
* Both instance types have dedicated hardware
* Dedicated instance are charged by the instance, dedicated hosts are charged by
the host
* If you have specific regulatory requirements or licensing conditions, choose 
dedicated hosts.
* Dedicated instances may share the same hardware with other AWS instances from
the same account that are not dedicated
* Dedicated hosts give you much better visibility in to thinks like sockets, 
cores and host id

## AWS Systems Manager EC2 Run Command

#### Exam Tips
* Commands can be applied to a group of systems based on AWS instance tags
* SSM agent needs to be installed on all of your managed instances
* The commands and params are defined in systems manager document
* Commands can be issued using the console, cli, tools for powershell, systems 
manager API or Amazon SDKs.
* You can use this service with on premise systems as well

## Systems Manager Parameter Store

#### AWS Systems Manager Parameter Store
 
* You can use this with EC2, CloudFormation, Lambda, or EC2 Run Command

## Inspector VS Trusted Advisor

#### What is Inspector?
It is a automanted security assessment service that helps improve the security
and compliance of applications deployed on AWS. It also automatically assesses
applications for vulnerabilities or deviations from best practices. After 
performing an assessment, it will produce a detailed list of security findings
prioritized by level of severity. These findings can be reviewed directly or as
part of a detailed assessment reports which are available via the console or API.

#### How does it work?
* Create "Assessment target"
* Install agents on EC2 instances
* Create "Assessment template"
* Perform "Assessment run"
* Review "Finding" against "Rules"

#### What is Trusted Advisor?
An online resource to help reduce costs, increase performance, and improve
security by optimizing your AWS environment. Advisor will advise you on Cost
Optimization, Performance, Security, Fault Tolerance.
* Core checks and recommendations
* Full trusted advisor: business and enterprise companies only

#### Exam Tips
Inspector:
* Rules packages
  - Common vulnerabilities and exposures
  - CIS operating system security configuration benchmarks
  - Security best practices
  - Runtime behavior analysis
* Severity levels for inspector
  - High
  - Medium
  - Low
  - Informational
* What will inspector do?
  - Monitor network, file systems, and process activity within the specified targets
  - Compare what it sees to security rules
  - Report on security issues observed within target during run
  - Report findings and advise remediation
* It will not:
  - Relieve you of your responsibility under the shared responsibility model
  - Perform miracles
Trusted Advisor:
* Cost optimization
* Availability
* Performance
* Does security as well

## Shared Responsibility Model

#### What is the Shared Responsibility Model?
While AWS manages security of the cloud, security in the cloud is the responsibility
of the customer. Customers retain control of what security they choose to implement
to protect their own content, platform, applications, systems and networks, no 
differently than they would in an on-site data center.

AWS Security Responsibilities:
* Global infrastructure
* Hardware, software, network, and facilities
* "managed services"

Customer Security Responsibilities:
* Infrastructure as a Service (IaaS)
* Include updates and security patches
* Configuration of the AWS provided firewalls

The model changes for the different service types:
* Infrastructure Services: This category includes compute services such as EC2, EBS,
Auto Scaling, and VPC. With these services, you can architect and build a cloud 
infrastructure using tech similar and largely compatible with on-premises solutions.
You control the OS, you configure and operate any identity management system that
provides access to the user layer of the virtualization stack.
* Container Services: Services in this category typically run on separate EC2 or 
other infrastructure instances, but sometimes you don't manage the OS or the 
platform layer. AWS provides a manages service for these application "containers".
You are responsible for setting up and managing network controls, such as firewall
rules, and for managing platform-level identity and access management separately 
from IAM. Examples of container services include RDS, EMR, & Elastic Beanstalk.
* Abstracted Services: This category includes high-level storage, database, and 
messaging services, such as S3, Glacier, DynamoDB, SQS, SES. These services 
abstract the platform or management layer on which you can build and operate cloud
applications. You access the endpoints of these services using AWS APIs, and AWS 
manages the underlying service components or OS on which they reside.

## Other Security Aspects

#### Security Groups
* They are stateful, this means that if you open up a port for inbound traffic,
it automatically opens it up to leave as well.
* Need to be able to read subnet rules

#### Who Keeps Provisioning Stuff?
How do you know who is provisioning EC2 instances in a certain account?
* You have cloudtrail turned on, but have 1000's of developers using the account
* You can use Athena to query logs stored in S3

#### AWS Artifact
Provides on demand downloads of AWS security compliance documents, such as AWS ISO
certifications, PCI, and SOC reports. You can submit the security and compliance 
docs to your auditors or regulators to demonstrate the security and compliance of 
the AWS infrastructure and services that you use.

#### CloudHSM vs KMS
Need to know the differences!!!!

#### Instant Encryption
Instant Encryption
* S3

Encryption with Migration
* RDS
* DynamoDB
* EBS
* EFS
