# Configuration Management & Infrastructure as Code

## AWS CloudFormation
* Building blocks: It's a language that gives you building blocks to describe the infrastructure you want to provision in AWS
* Text files: Containing that description. Formatted in JSON and YAML. You can version it and track changes just like any other piece of code.
* Free: You can build your entire infrastructure with CloudFormation.
 
 #### CloudFormation Terms
 * Stack: A collection of AWS resources that you manage as a single unit. The stack is created when you give the CloudFormation service your template.
 * Template: The document that describes how to act and what to create. Literally the text that you write that CloudFormation uses to provision infrastructure. A template can be used to both create and update a stack.
 * Stack Policy: IAM style policy statement which governs what can be changed and who can change it.
 
 #### Template Anatomy
 * Parameters: Allow the passing of variables into the template via the UI, CLI or API
 * Mapping: Allow processing of hashes (arrays of key/value pairs) by the template
 * Resources: Where your actual resources are declared
 * Outputs: results from the template
 
 #### When and where?
 * To deploy infrastructure rather than doing it manually
 * To create a repeatable patterned environment
 * To run automated testing for CI/CD environments. Create a dedicated environment, inject your code, run testing, produce results, then delete the test environment; all with no human input
 * To define an environment all at once, and have it deployed to any region in the AWS Cloud without reconfiguration
 * To manage infrastructure configuration using software development style versioning and code repositories
 * Key Learning: A template should be designed fo it's equally suitable for 1, 100, or 100 applications in one or more regions
 
 
## AWS CloudFormation Intrinsic Functions
AWS CloudFormation provides function to assist in assigning values to template properties that are not available until runtime.

#### FindInMap YAML Example:
```yaml
Mappings:
  RegionMap:
    us-east-1:
      HMV64: "ami-foo-east"
      HMVG2: "ami-bar-east"
    us-west-1:
      HMV64: "ami-foo-west"
      HMVG2: "ami-bar-west"


Resources:
  myEC2Instance:
    Type: "AWS::EC2::Instance"
    Properties:
      ImageId: !FindInMap
        - RegionMap
        - !Ref 'AWS::Region'
        - HMV64
      InstanceType: m1.small
```
 
#### Functions
**Fn:Base64**
* Returns the Base64 representation of the input string
* Used to pass encoded data to the UserDate in EC2
* JSON: `{"Fn::Base64": valueToEncode}`
* YAML: `Fn:Base64: valueToEncode` or `!Base64 valueToEncode`

**Fn:Cidr**
* Returns an array of CIDR address blocks
* The number of blocks returned is dependent on the count value from 1 to 256
* JSON: `"Fn::Cidr": [ipBlock, count, cidrBits]}`
* YAML:
    ```yaml
    Fn::Cidr:
      - ipBlock
      - count
      - cidrBots
    or
    !Cidr [ ipBlock, count, cidrBits ]
    ```

**FnGetAtt**
* Returns the value of an attribute from a resource in the template
* JSON: `{"Fn::GetAtt": ["logicalNameOfResource", "attributeName"]`
* YAML: `Fn:GetAtt: [ logicalNameOfResource, attributeName ]` or `!GetAtt logicalNameOfResource.attributeName`

**Fn:GetAZs**
* Returns an array that lists Availability Zones for a specified region
* JSON: `{"Fn::GetAZs": "region"}`
* YAML: `Fn::GetAZs: region` or `!GetAZs region`

**Fn:ImportValue**
* Returns the value of an output exported by another stack
* Typically to create cross-stack references
* JSON: `{"Fn::ImportValue": SharedValueToImport}`
* YAML: `Fn::ImportValue: sharedValueToImport` or `!ImportValue sharedValueToImport`

**Fn:Join**
* Appends a set of values into a single value, separated by the specified delimiter
* JSON: `{"Fn::Join": ["delimiter", [comma-delimited list of values]]}`
* YAML: `Fn::Join: [ delimiter, [comma-delimited list of values]]` or `!Join [ delimiter, [comma-delimited list of values]]`

**Fn:Select**
* Returns a single object from a list of objects by index
* JSON: `{"Fn::Select": [index, listOfObjects]}`
* YAML: `Fn::Select: [index, listOfObjects]` or `!Select [index, listOfObjects]`

**Fn:Split**
* Splits a string into a list of string values so that you can select an element from the resulting string list
* JSON: `{"Fn::Split": ["delimiter", "source string"]}`
* YAML: `Fn::Split: [delimter, source string]` or `!Split [delimiter, source string]`

**Fn:Sub**
* Substitutes variables in an input string with values that you specify
* JSON: `{"Fn::Sub": [String, {Var1Name: Var1Value, Var2Name: Var2Value}]}`
* YAML:
    ```yaml
    Fn::Sub:
      - String
      - {Var1Name: Var1Value, Var2Name: Var2Value}
    or 
    !Sub
      - String
      - {Var1Name: Var1Value, Var2Name: Var2Value}
    ```
 
 **Fn:Transform**
 * Specidies a macro to perform custom processing on part of a stack template
 

## AWS CloudFormation Wait Conditions

#### DependsOn
* Used for controlling resource creation order within CloudFormation
```yaml
Resources:
  MyEC2Instance:
    Type: "AWS::EC2::Instance"
    Properties:
      ImageId: "ami-foo"
    DependsOn: GatewayToInternet
  
  GatewayToInternet:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId:
        Ref: VPC
      InternetGatewayId:
        Ref: InternetGateway
```

#### Creation Policies
* Prevent a resource status from reaching create complete until AWS CloudFormation receives a specified number of success signals or the timeout period is exceeded
```yaml
CreationPolicy:
  ResourceSignal:
    Count: '3'
    Timeout: PT15M
``` 

#### Wait Conditions & Handlers
* Allows you to coordinate stack resource creation with other configuration actions that are external to the stack
* It also allows you to track the status of a configuration process
* Wait condition handles are a resource with no properties which generates a signed URL which can be used to communicate SUCCESS or FAILURE
* Wait conditions have 4 components:
  - They DependOn the resource(s) you are waiting on
  - A Handle property references the above handle
  - They have a response timeout
  - They have a `count`, if none is specifies the default is 1
  
#### Wait Conditions & Handlers vs Creation Policies
* Why are wait conditions and handlers different from creation policies?
* You can implement a complex order of conditions; the wait conditions can depend on many resources, and have many resources depending on it
* You can influence the order in which things are built by using DependsOn with WaitConditions
* Additional data can be passed back via the signed URL generated by the wait condition handler, which can then be accessed within the template

## AWS CloudFormation Nested Stacks
* A stack contains resources
* A resource can be an S3 bucket, EC2 instance or any other service
* With nesting, a whole other stack can be created
* Nested stacks can have nested stacks
* Why?
  - It allows a huge set of infrastructure to be split over multiple templates
  - There are limits to stacks, such as 200 resources, 60 outputs and 60 parameters
  - You can overcome these limits by using nested stacks
  - Allows more effective "infrastructure as code" reuse
  
 ## AWS CloudFormation Deletion Policies
 * A setting which is associated with each resource in a CloudFormation template
 * A way to control what happens to each resource when a stack is deleted
 * The policy value can be one of:
   - Delete - default
   - Retain
   - Snapshot
   
## AWS CloudFormation Stack Updates

#### Stack Updates
* What happens when we update a stack?
  - The stack policy is checked
  - Changes are orchestrated
* The absence of a stack policy allows all updates
* Once a stack policy is applied, it can't be deleted
* Once a policy is applied, by default ALL objects are protected and Update:* is denied

#### Resouce Impacts
* The change a resource undergoes during an update is dependent on the resource property
* An update can impact a resource in four ways
  - No interruption
  - Some interruption
  - Replacement
  - Delete
 
## AWS CloudFormation Change Sets
* Preview how your changes will impact your stack and resources
* See if changes will delete or replace critical resources
* Let you make changes only when you execute the change setf
* Available via console, AWS CLI, and CloudFormation API

## AWS CloudFormation Custom Resources
* Custom resources enable you to write custom provisioning logic in templates
* Extend CloudFormation beyond AWS
* Can invoke a lambda and reference it's output in the CloudFormation stack

## Elastic Beanstalk
* An orchestration service offered by AWS
* Used to deploy and scale web applications and services
* Supports Java, .NET, PHP NodeJS, Python, Ruby, Go, aand Docker
* You write the code and Beanstalk does the rest
* It takes care of deployment, capacity provisioning, load balancing, auto scaling, and application health monitoring
* Fastest and simplest way to deploy your applications to AWS
* You retain full control over the AWS resources
* There's no extra charge, you just pay for the other AWS services that are provisioned to run your application

#### AWS Elastic Beanstalk .ebextensions
* Allows advanced environment customizatio with configuration files
* YAML or JSON formatted documents
* Placed in a folder called .ebextensions
* Allows developers to configure the systems being deployed automatically
* Any automated customizable task on Beanstalk should most likely be done via an ebextension

## AWS Config

#### What is it?
Records change and such to all resources in your account and provides a nice dashboard and ways to alert if resources aren't compliant.
* Continuous monitoring
* Continuous assessment
* Troubleshooting
* Compliance monitoring
* Change management

## ECS

#### What is ECS?
* Elastic: scales automatically 
* Container: lightweight unit that packages code and all of it's dependencies into a Docker container
* Service: system supplying a need

## AWS Managed Services
AWS Managed Services (AMS) helps you operate your AWS infrastructure more efficiently and securely. Leveraging AWS services and a growing library of automations, configurations, and run books, AMS can augment and optimize your operational capabilities in both new and existing AWS environments.
AMS provides you operational flexibility, enhances security and compliance, and will help you optimize capacity and take action on identified cost savings. AMS provides a consistent operating model for your entire AWS fleet leveraging detective guardrails, monitoring, security, and incident management best practices for both traditional and modernized workloads.

