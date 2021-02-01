# Cost Management

## Concepts
* Capital Expenses (CapEx): Money spent on long-term assets like property, buildings and equipment.
* Operational Expenses (OpEx): Money spent for on-going costs for running the business. Usually considered variable expenses.

* Total Cost of Ownership (TCO): A comprehensive look at the entire cost model of a given decision or option, often including both hard costs and soft costs.
* Return on Investment (ROI): The amount an entity can expect to receive back within a certain amount of time given an investment
 
#### TCO and ROI
* Many times, organizations don't have a good handle on their full on-prem data center sosts (power, cooling, fire suppression, etc.)
* Soft costs are rarely tracked or even understood as tangible expense.
* Learning curve will be very different from person to person.
* Business plans usually include many assumptions which in turn require support organizations to create derivative assumptions - sometimes layers deep.


## Cost Optimization Strategies

#### Appropriate Provisioning
* Provision the resources you need and nothing more
* Consolidate where possible for greater density and lower complexity (multi-database RDS, containers)
* CloudWatch can help monitor utilization

#### Right Sizing
* Using lowest cost resource that still meets the technical specifications
* Architecting for most consistent use of resources is best versus spikes and valleys
* Loosely coupled architectures using SNS, SQS, Lambda and DynamoDB can smooth demand and create more predictability and consistency

#### Purchase Options
* For permanent applications or needs, Reserved Instances provide the best cost advantage.
* Sport instances are best for temporary horizontal scaling.
* EC2 fleet lets you define target mix of On-Demand, Reserved and Spot instances.

| Instance | On Demand | Reserved 1 Year All Upfront | Spot Instance |
| -------- | --------- | --------------------------- | ------------- |
| m5.2xlarge | $0.384 | $0.229 (40% less) | $0.0798 (79% less) |

#### Geographic Selection
* AWS pricing can vary from region to region
* Consider potential savings by locating resources in a remote region if local access is not required
* Route53 and CloudFront can be used to reduce potential latency of a remote region

| Region | S3 Standard Storage First 50GB |
| ------ | ------------------------------ |
| us-west-2 | $0.023 per GB |
| us-west-1 | $0.026 per GB |
| ap-northeast-1 | $0.025 per GB |
| sa-east-1 | $0.0405 per GB |

#### Managed Services 
* Leverage managed services such as MySQL RDS over self-managed options such as MySQL on EC2
* Cost savings gained through lower complexity and manual intervention
* RDS, RedShift, Fargate, and EMR are great examples of full-managed services that replace traditionally complex and difficult installations with push-button ease.

#### Optimize Data Transfer
* Data going out and between AWS regions can become a significant cost component
* Direct Connect can be more cost-effective option given data volume and speed


## Tagging and Resource Groups

#### AWS Tagging
* The number one best thing you can do to help manage your AWS assets
* Tags are just arbitrary name/value pairs that you can assign to virtually all AWS assets to serve as metadata
* Tagging strategies can be used for Cost Allocation, Security, Automation, and many other uses.
    - For example, we can use a tag in an IAM policy to implement access controls to certain resources
* Enforcing standardized tagging can be done via AWS Config Rules or custom scripts
    - For example, EC2 instances not properly tagged are stopped or terminated nightly
* Most resources can have up to 50 tags
    
#### AWS Resource Groups
* Resource Groups are groupings of AWS assets defined by tags
* Create custom consoles to consolidate metrics, alarms and config details around given tags

Common Resource Groupings:
* Environments (Dev, QA, Prod)
* Project resources
* Collection of resources supporting key business processes
* Resources allocated to various departments or cost centers


## Spot and Reserved Instances

#### Reserved Instances
* Purchase (or agree to purchase) usage of EC2 instances in advance for a significant discount over On-Demand pricing
* Provides capacity reservation when used in a specific AZ
* AWS Billing automatically applies discounted rates when you launch an instance that matches your purchased RI
* EC2 has three RI types: Standard, Convertible, and Scheduled
* Can be shared across multiple accounts within Consolidated Billing
* If you find you don't need RI's you can tru to sell them on the Reserved Instance Marketplace

| What | Standard | Convertible |
| ---- | -------- | ----------- |
| Terms | 1 year, 3 year | 1 year, 3 year |
| Average Discount off On-Demand | 40% - 60% | 31% - 54% |
| Change AZ, Instance Size, Networking Type | Yes via API or console | Yes via API or console |
| Change instance family, OS, Tenancy, Payment Options | No | Yes | 
| Benefit from Price Reductions | No | Yes |
| Sellable on Reserved Instances Marketplace | Yes (Sales proceeds must be deposited in US bank account | Coming soon |

#### RI Attributes
* Instance Type - designates CPU, memory, networking capability
* Platform - Linux, SUSE Linux, RHEL, Windows, Microsoft SQL Server
* Tenancy - Default (shared) tenancy or Dedicated tenancy
* Availability Zone (optional) - if AZ is selected, RI is reserved and discount applies to that AZ (Zonal RI). If no AZ is specified, no reservation is created but the discount is applied to any instance in the family in any AZ in the region (Regional RI).
 
#### Spot Instances
* Excess EC2 capacity that AWS tries to sell on an market exchange basis
* Customer creates a Spot Request and specifies AMI, desired instance types, and other key information.
* Customer defines highest price willing to pay for instance. If capacity constrained and others are willing to pay more, your instance might get terminated or stopped.
* Spot request can be a "fill and kill", "maintain", "duration-based".
* For "One-Time Request", instance is terminated and ephemeral data lost.
* For "Request and Maintain", instance can be configured to Terminate, Stop or Hibernate until price point can be met again.

#### Dedicated Instances and Hosts
Dedicated Instance:
* Virtualized instances on hardware just for you
* May share hardware with other non-dedicated instances in the same account
* Available as On-Demand, Reserved Instances, and Spot instances
* Cost additional $2 per hour per region

Dedicated Host:
* Physical servers dedicated to just your use
* You then have control over which instances are deployed on that host
* Available as On-Demand or with Dedicated Host Reservation
* Useful if you have server-bound software licences that use metrics like per-core, per-socket or per-VM 
* Each dedicated host can only run one EC2 instance size and type

## Cost Management Tools

#### AWS Budgets
* Allow you to set pre-defined limits and notifications if nearing a budget or exceeding the budget
* Can be based on Cost, Usage, Reserved Instance Utilization or Reserved Instance Coverage
* Useful as a method to distribute cost and usage awareness and responsibility to platform users

#### Consolidated Billing
* Enable a single payer account that's locked down to only those who need access
* Economies of scale by bringing together resource consumption across accounts

| Example | Account A | Account B | Account C | Billed Individually | Consolidated Billing |
| ------- | --------- | --------- | --------- | ------------------- | -------------------- |
| S3 Storage | 50 TB | 50 TB | 50 TB | $3,450 | $3,350 |

#### Trusted Advisor 
* Runs a series of checks on your resources and proposes suggested improvements
* Can help recommend cost optimization adjustments like reserved instances or scaling adjustments
* Core checks are available to all customers
* Full Trusted Advisor benefits require Business or Enterprise support plan


## Exam Tips
Costing in General:
* Understand the difference between CapEX and OpEx models
* Understand TCO, ROI, and the challenges faced in these activities 

Cost Optimization Strategies:
* Know conceptually the variety of ways customers can approach cost optimization on AWS
* Fully understand the Cost Optimization Pillar white paper

Tagging and Resource Groups:
* Understand the various common uses for tagging and ways you can implement/enforce a tagging strategy
* Know when and how to create Resource Groups, and don't be tricked into thinking they are anything more than a logical grouping
  
Sport and Reserved Instances:
* Know the differences and limitations for different types of Reserved Instances, including Zonal and Regional
* Understand how Spot instances work and when they are best used
* Understand Dedicated Instances and Dedicated Hosts

Cost Management Tools:
* Know how and when you would use AWS budgets
* Understand the benefits of consolidated billing
* Know how Trusted Advisor can help customers optimize and improve their AWS landscapes

White Papers:
* [Cost Optimization Pillar: Well Architected Framework](https://d1.awsstatic.com/whitepapers/architecture/AWS-Cost-Optimization-Pillar.pdf)
* [Maximizing Value with AWS](https://d1.awsstatic.com/whitepapers/total-cost-of-operation-benefits-using-aws.pdf)
* [Introduction to AWS Economics: Reducing Cost and Complexity](https://d1.awsstatic.com/whitepapers/introduction-to-aws-cloud-economics-final.pdf)
* [ReInvent: Building a Solid Business Case for Cloud Migration](https://www.youtube.com/watch?v=CcspJkc7zqg&ab_channel=AmazonWebServices)
* [ReInvent: Running Lean Architectures: How to Optimize for Cost Efficiency](https://www.youtube.com/watch?v=XQFweGjK_-o&ab_channel=AmazonWebServices)
* [Re:Invent How Hess Has Continued to Optimize the AWS Cloud After Migrating](https://www.youtube.com/watch?v=1Z4BfRj2FiU&ab_channel=AmazonWebServices)


## Pro Tips
* Be extra careful around the TCO and ROI minefield
* The real benefit of a Cloud Migration is in Agility and Flexibility. Cost alone is typically not the strongest business case.
* Think of cost optimization as a long term effort - don't spend too much time on trying to micro manage it up front
* Implement a tagging strategy out of the gate
* Be aggressive in formulating a pilot projec: large-scale benefits make for dramatic business cases, where small scale wins can easily be ignored
 

 ## Challenges
 * Question 1:
    - My Answer: C, D, E, F, G
    - Correct Answer: D, E
    
* Question 2:
    - My Answer: E, F
    - Correct Answer: A, E 