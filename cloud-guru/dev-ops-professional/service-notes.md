# CloudFormation

#### Limits
| Quotas | Description | Value | Tuning Strategy |
| ------ | ----------- | ----- | --------------- |
| cfn-signal wait condition data | Maximum amount of data that cfn-signal can pass | 4,096 bytes | To pass a larger amount, send the data to a S3 bucket and then use cfn-signal to pass the S3 URL to that bucket |
| Mappings | Maximum number of mappings that you can declare in your AWS CloudFormation template. | 200 mappings | To specify more mappings, separate your template into multiple templates by using, nested stacks |
| Mapping attributes | Maximum number of mapping attributes for each mapping that you can declare in your AWS CloudFormation template. | 200 attributes | To specify more mapping attributes, separate the attributes into multiple mappings. |
| Module versions | Maximum number of versions you can register in the CloudFormation registry for a given module. | 100 versions | To register new versions, first use DeregisterType to deregister versions you aren't using anymore. |
| Parameters | Maximum number of parameters that you can declare in your AWS CloudFormation template. | 200 parameters | To specify more parameters, you can use mappings or lists in order to assign multiple values to a single parameter. |
| Parameter value | Maximum size of a parameter value. | 4,096 bytes | To use a larger parameter value, create multiple parameters and then use Fn::Join to append the multiple values into a single value. | 
| Resources | Maximum number of resources that you can declare in your AWS CloudFormation template. | 500 resources | To specify more resources, separate your template into multiple templates by using, for example, nested stacks. | 
| Stacks |  Maximum number of AWS CloudFormation stacks that you can create. | 200 stacks | To create more stacks, delete stacks that you don't need or request an increase in the maximum number of stacks in your AWS account. For more information, see AWS service quotas in the AWS General Reference. |
|  

#### Template Anatomy
```json
{
  "AWSTemplateFormatVersion" : "version date",

  "Description" : "JSON string",

  "Metadata" : {
    template metadata
  },

  "Parameters" : {
    set of parameters
  },
  
  "Rules" : {
    set of rules
  },

  "Mappings" : {
    set of mappings
  },

  "Conditions" : {
    set of conditions
  },

  "Transform" : {
    set of transforms
  },

  "Resources" : {
    set of resources
  },
  
  "Outputs" : {
    set of outputs
  }
}
```

#### Stacks 
A stack is a collection of AWS resources that you can manage as a single unit. All the resources in a stack are defined by the stack's CloudFormation Template.

**Stack Update Methods**
* Direct update: immediately deploys changes submitted for the stack
* Change set: preview the changes CloudFormation will make to the stack and then decide whether or not to apply those changes

**Update Behaviors**
* Update with no interruption: updates the resource w/no operational disruption
* Updates with some interruption: updates the resource with some interruption
* Replacement: recreates the resource, changes references to point at the new resource, and deletes the old resource

**Prevent Updates to Stack Resources**
* To prevent stack resources from being updated, apply a stack policy. See the example below, which prevents updates to the ProductionDatabase resource.
```json
{
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : "Update:*",
      "Principal": "*",
      "Resource" : "*"
    },
    {
      "Effect" : "Deny",
      "Action" : "Update:*",
      "Principal": "*",
      "Resource" : "LogicalResourceId/ProductionDatabase"
    }
  ]
}
```

**Import and Move Resources**
* CloudFormation stack resources can be imported and moved between stacks using the `resource import` feature

**Nested Stacks**
* Nested stacks are stacks created as part of other stacks. You can create another stack by using the `AWS::CloudFormation::Stack` resource
* Allows you to you declare the same components in multiple templates
* Nested stacks can contain yet more nested stacks

#### Templates
To provision and configure stack resources you must understand CloudFormation templates which are formatted JSON or YAML files. These templates describe the resources
that you want to provision in your CLoudFormation stacks. 

**Template Sections**
* Format Version (optional): The AWS CloudFormation template version that the template conforms to. The template format version isn't the same as the API or WSDL version. The template format version can change independently of the API and WSDL versions.
* Description (optional): A text string that describes the template. This section must always follow the template format version section.
* Metadata (optional): Objects that provide additional information about the template.
* Parameters (optional): Values to pass to your template at runtime (when you create or update a stack). You can refer to parameters from the Resources and Outputs sections of the template.
* Rules (optional): Validates a parameter or a combination of parameters passed to a template during a stack creation or stack update.
* Mappings (optional): A mapping of keys and associated values that you can use to specify conditional parameter values, similar to a lookup table. You can match a key to a corresponding value by using the Fn::FindInMap intrinsic function in the Resources and Outputs sections.
* Conditions (optional): Conditions that control whether certain resources are created or whether certain resource properties are assigned a value during stack creation or update. For example, you could conditionally create a resource that depends on whether the stack is for a production or test environment.
* Transform (optional): For serverless applications (also referred to as Lambda-based applications), specifies the version of the AWS Serverless Application Model (AWS SAM) to use. When you specify a transform, you can use AWS SAM syntax to declare resources in your template. The model defines the syntax that you can use and how it is processed. You can also use AWS::Include transforms to work with template snippets that are stored separately from the main AWS CloudFormation template. You can store your snippet files in an Amazon S3 bucket and then reuse the functions across multiple templates.
* Resources (required): Specifies the stack resources and their properties, such as an Amazon Elastic Compute Cloud instance or an Amazon Simple Storage Service bucket. You can refer to resources in the Resources and Outputs sections of the template.
* Outputs (optional): Describes the values that are returned whenever you view your stack's properties. For example, you can declare an output for an S3 bucket name and then call the aws cloudformation describe-stacks AWS CLI command to view the name.

#### StackSets
AWS CloudFormation StackSets extends the functionality of stacks by enabling you to create, update, or delete stacks across multiple accounts and regions with a single operation. Using an administrator account, you define and manage an AWS CloudFormation template, and use the template as the basis for provisioning stacks into selected target accounts across specified AWS Regions.

After you've defined a stack set, you can create, update, or delete stacks in the target accounts and Regions you specify. When you create, update, or delete stacks, you can also specify operation preferences, such as the order of regions in which you want the operation to be performed, the failure tolerance beyond which stack operations stop, and the number of accounts in which operations are performed on stacks concurrently.

A stack set is a regional resource. If you create a stack set in one Region, you can't see it or change it in other Regions.

# AWS Step Functions
Step Functions is based on state machines and tasks. A state machine is a workflow. A task is a state in a workflow that represents a single unit of work that another AWS service performs. Each step in a workflow is a state.

With Step Functions' built-in controls, you examine the state of each step in your workflow to make sure that your application runs in order and as expected. Depending on your use case, you can have Step Functions call AWS services, such as Lambda, to perform tasks. You can create workflows that process and publish machine learning models. You can have Step Functions control AWS services, such as AWS Glue, to create extract, transform, and load (ETL) workflows. You also can create long-running, automated workflows for applications that require human interaction.

#### Standard and Express workflows
* Standard workflows: have exactly-once workflow execution and can run for up to one year
    - Ideal fro long-running, auditable workflows, as they show execution history and visual debugging
    - 2,000 per second execution rate
    - 4,000 per second state transition rate
    - Priced per state transition
    - Shows execution history and visual debugging
    - Supports all service integrations and patterns 
* Express workflows: have at-least-once workflow execution and can run for up to 5 minutes
    - Express workflows are ideal for high event rate workloads, such as streaming data processing and IoT data ingestion
    - 100,000 per second execution rate
    - Nearly unlimited state transition rate
    - Priced per number and duration of executions
    - Sends execution history to Amazon CloudWatch
    - Supports all service integrations and most patterns

Executions are instances where you run your workflow to perfom tasks.

#### State Fields
* Type: the state's type
* Next: The name of the nest state that is run when the current state finishes. Some state types, such as `Choice`, allow multiple transition states.
* End: Designates this state as a terminal state if set to true. There can be any number of terminal states per machine. Only one of `Next` or `End` can be used in a state. Some state types, such as `Choice` don't support or use the `End` field.
* Comment: holds a human readable description of the state
* InputPath: A path that select a portion of the state's input to be passed to the state's task for processing. if omitted, it has the value `$` which designates the entire input.
* OutputPath: A path that selects a portion of the state's input to be passed to the state's output. If omitted, it has the value `$` which designates the entire output.

**Pass**: a pass state, passes its input to its output, without performing work. Pass states are useful when constructing and debugging state machines.
* Result: treated as the output of a virtual task to be passed to the next state, and filtered as specified by the `ResultPath` field if present
* ResultPath: specifies where in the input to place the "output" of the virtual task specified in `Result` The input is further filtered as specified by the `OutputPath` field (if present) before being used as the state's output.
* Parameters: create a collection of key-value pairs that will be passed as input. Values can be static or selected from the input with a path.

# AWS Elastic Beanstalk
With Elastic Beanstalk, you can quickly deploy and manage applications in the AWS Cloud without having to learn about the infrastructure that runs those applications. Elastic Beanstalk reduces management complexity without restricting choice or control. You simply upload your application, and Elastic Beanstalk automatically handles the details of capacity provisioning, load balancing, scaling, and application health monitoring.

Elastic Beanstalk supports applications developed in:
* Go
* Java
* .NET
* NodeJS
* PHP
* Python
* Ruby

When you deploy your application, Elastic BeanStalk builds the selected supported platform version and provisions one or more AWS resources, such as EC2 instances to run your application.

# CodeDeploy
CodeDeploy is a deployment service that automates application deployments to Amazon EC2 instances, on-premises instances, serverless Lambda functions, or Amazon ECS services.

You can deploy a nearly unlimited variety of application content, including:
* Code
* Serverless AWS Lambda functions
* Web and configuration files
* Executables
* Packages
* Scripts
* Multimedia files

CodeDeploy can deploy application content that runs on a server and is stored in Amazon S3 buckets, GitHub repositories, or Bitbucket repositories. CodeDeploy can also deploy a serverless Lambda function. You do not need to make changes to your existing code before you can use CodeDeploy.

CodeDeploy makes it easier for you to:
* Rapidly release new features.
* Update AWS Lambda function versions.
* Avoid downtime during application deployment.
* Handle the complexity of updating your applications, without many of the risks associated with error-prone manual deployments.

#### Benefits
* Server, serverless, and container applications: CodeDeploy lets you deploy both traditional applications on servers and applications that deploy a serverless AWS Lambda function version or an Amazon ECS application.
* Automated deployments: CodeDeploy fully automates your application deployments across your development, test, and production environments. CodeDeploy scales with your infrastructure so that you can deploy to one instance or thousands.
* Minimize downtime: if your application is on EC2 or onPrem, CodeDeploy helps maximize application availability. During an in-place deployment, CodeDeploy performs a rolling update across EC2 instances. You can specify the number of instances offline at a time during updates. During a blue/green deployment, that latest application revision is installed on replacement instances. Traffic is rerouted to thes instances when you choose, either immediately or as soon as you are done testing the new environment. For both deployment types, CodeDeploy tracks application health according to rules you configure.
* Stop and roll back: You can automatically or manually stop and roll back deployments if there are errors.
* Centralized control: You can launch and track the status of your deployments through the CodeDeploy console or the AWS CLI. You receive a report that lists when each application revision was deployed and to which Amazon EC2 instances.
* Easy to adopt: CodeDeploy is platform-agnostic and works with any application. You can easily reuse your setup code. CodeDeploy can also integrate with your software release process or continuous delivery toolchain.

#### Deployment Platforms
* EC2/On-Prem
* AWS Lambda
* Amazon ECS

#### Components
| Component | EC2/On-Prem | Lambda | ECS |
| --------- | ----------- | ------ | --- |
| Deployment group | Deploys a revision to a set of instances | Deploys a new version of the lambda function | Specifies the ECS service to deploy as a task set, a production and optional test listener used to serve traffic to the deployment application, when to reroute traffic and terminate the deployment applications original task set, and optional trigger, alarm, and rollback settings |
| Deployment |  Deploys a new revision that consists of an application and AppSpec file. The AppSpec specifies how to deploy the application to the instances in a deployment group. | Shifts production traffic from one version of a Lambda function to a new version of the same function. The AppSpec file specifies which Lambda function version to deploy. | Deploys an updated version of an Amazon ECS containerized application as a new, replacement task set. CodeDeploy reroutes production traffic from the task set with the original version to the new replacement task set with the updated version. When the deployment completes, the original task set is terminated. |
| Deployment configuration | Settings that determine the deployment speed and the minimum number of instances that must be healthy at any point during a deployment. | Settings that determine how traffic is shifted to the updated Lambda function versions. | Settings that determine how traffic is shifted to the updated Amazon ECS task set. |
| Revision | A combination of an AppSpec file and application files, such as executables, configuration files, and so on. | An AppSpec file that specifies which Lambda function to deploy and Lambda functions that can run validation tests during deployment lifecycle event hooks. | An AppSpec file that specifies: The Amazon ECS task definition for the Amazon ECS service with the containerized application to deploy. The container where your application is deployed. A port for the container where production traffic is rerouted. Optional network configuration settings and Lambda functions that can run validation tests during deployment lifecycle event hooks. |
| Application | A collection of deployment groups and revisions. An EC2/On-Premises application uses the EC2/On-Premises compute platform. | A collection of deployment groups and revisions. An application used for an AWS Lambda deployment uses the serverless AWS Lambda compute platform. | A collection of deployment groups and revisions. An application used for an Amazon ECS deployment uses the Amazon ECS compute platform. |

#### Deployment Options
* In place deployment
* Blue/green deployment
    - Canary: Traffic is shifted in two increments. You can choose from predefined canary options that specify the percentage of traffic shifted tou your updated application in the first interval, in minutes, before shifting the remaining traffic to the second increment.
    - Linear: Traffic is shifted in equal increments with an equal number of minutes between each increment. You can choose from predefined linear options that specify the percentage of traffic shifted in each increment and the number of min between each increment.
    - All at once: All traffic is shifted over at once
 
# CodePipeline

#### Pipeline Terms
Pipeline: a pipeline is a workflow construct that describes how software changes through a release process. Each pipeline is made up of a series of stages.
- Stages: a stage is a logical unit you can use to isolate and environment and to limit the number of concurrent changes in that environment. Each stage contains actions that are performed on the application artifacts. Source code is an example of an artifact.
- Actions: an action is a set of operations performed on application code and configured so that the actions run in the pipeline at a specified point. Multiple actions can run in a stage and they can run in either parallel or serial order. Valid action types are:
    - source 
    - build
    - test 
    - deploy
    - approval
    - invoke

Pipeline executions: An execution is a set of changes released by a pipeline. Each pipeline execution is unique and has its own ID. An execution corresponds to a set of changes, such as a merged commit or a manual release of the latest commit. Two executions can release the same set of changes at different times.
- Stopped executions: The pipeline execution can be stopped manually so that the in-progress pipeline execution does not continue through the pipeline. If stopped manually, a pipeline execution shows a Stopping status until it is completely stopped. Then it shows a Stopped status. A Stopped pipeline execution can be retried.
- Failed executions: If an execution fails, it stops and does not completely traverse the pipeline. Its status is FAILED status and the stage is unlocked.
- Superseded executions: To deliver the latest set of changes through a pipeline, newer executions pass and replace less recent executions already running through the pipeline. When this occurs, the older execution is superseded by the newer execution.

Stage executions: A stage execution is the process of completing all of the actions within a stage. Valid statuses for stages are InProgress, Stopping, Stopped, Succeeded, and Failed.

Action executions: An action execution is the process of completing a configured action that operates on designated artifacts. These can be input artifacts, output artifacts, or both. Valid statuses for actions are InProgress, Abandoned, Succeeded, or Failed.  

Action Types: Action types are preconfigured actions that are available for selection in CodePipeline. The action type is defined by its owner, provider, version, and category. The action type provides customized parameters that are used to complete the action tasks in a pipeline.

Transitions: A transition is the point where a pipeline execution moves to the next stage in the pipeline. You can disable a stage's inbound transition to prevent executions from entering that stage, and then you can enable the transition to allow executions to continue.

Artifacts: Artifacts refers to the collection of data, such as application source code, built applications, dependencies, definitions files, templates, and so on, that is worked on by pipeline actions. Artifacts are produced by some actions and consumed by others. In a pipeline, artifacts can be the set of files worked on by an action (input artifacts) or the updated output of a completed action (output artifacts).

Source revisions: When you make a source code change, a new version is created. A source revision is the version of a source change that triggers a pipeline execution. An execution processes that source revision only

# CodeBuild
CodeBuild compiles your source code, runs unit tests, and produces artifacts that are ready to deploy. CodeBuild eliminates the need to provision, manage, and scale your own build servers.

#### Supported Source Code Sources
* CodeCommit
* Amazon S3
* Github
* Bitbucket

#### Build Specification Reference
The buildspec has the following syntax:
```yaml
version: 0.2

run-as: Linux-user-name

env:
  shell: shell-tag
  variables:
    key: "value"
    key: "value"
  parameter-store:
    key: "value"
    key: "value"
  exported-variables:
    - variable
    - variable
  secrets-manager:
    key: secret-id:json-key:version-stage:version-id
  git-credential-helper: no | yes

proxy:
  upload-artifacts: no | yes
  logs: no | yes

batch:
  fast-fail: false | true
  # build-list:
  # build-matrix:
  # build-graph:
        
phases:
  install:
    run-as: Linux-user-name
    on-failure: ABORT | CONTINUE
    runtime-versions:
      runtime: version
      runtime: version
    commands:
      - command
      - command
    finally:
      - command
      - command
  pre_build:
    run-as: Linux-user-name
    on-failure: ABORT | CONTINUE
    commands:
      - command
      - command
    finally:
      - command
      - command
  build:
    run-as: Linux-user-name
    on-failure: ABORT | CONTINUE
    commands:
      - command
      - command
    finally:
      - command
      - command
  post_build:
    run-as: Linux-user-name
    on-failure: ABORT | CONTINUE
    commands:
      - command
      - command
    finally:
      - command
      - command
reports:
  report-group-name-or-arn:
    files:
      - location
      - location
    base-directory: location
    discard-paths: no | yes
    file-format: report-format
artifacts:
  files:
    - location
    - location
  name: artifact-name
  discard-paths: no | yes
  base-directory: location
  exclude-paths: excluded paths
  enable-symlinks: no | yes
  s3-prefix: prefix
  secondary-artifacts:
    artifactIdentifier:
      files:
        - location
        - location
      name: secondary-artifact-name
      discard-paths: no | yes
      base-directory: location
    artifactIdentifier:
      files:
        - location
        - location
      discard-paths: no | yes
      base-directory: location
cache:
  paths:
    - path
    - path
```

The buildspec contains the following:
* version: the buildspec version to use
* run-as: available to linux users only. Specifies the user that runs commands in the buildspec file
* env: operational sequence. Represents information for one or more custom environment varialbes
    - env/shell: specifies the supported shell for Linux or Windows
        * Linux shell tags are `bash` or `/bin/sh`
        * Windows shell tags are `powershell.exe` or `cmd.exe`
    - env/variables: Required if env is specified, and you want to define custom environment variables in plain text. Contains a mapping of key/value scalars, where each mapping represents a single custom environment variable in plain text
    - env/parameter-store: Required if env is specified, and you want to retrieve custom environment variables stored in Amazon EC2 Systems Manager Parameter Store. 
    - env/secrets-manager: Required if you want to retrieve custom environment variables stored in AWS Secrets Manager. Specify a Secrets Manager reference-key.
    - env/exported-variables: Optional mapping. Used to list environment variables you want to export. 
    - env/git-credential-helper: Optional mapping. Used to indicate if CodeBuild uses its Git credential helper to provide Git credentials. yes if it is used. Otherwise, no or not specified. For more information, see gitcredentials on the Git website.
* proxy: Optional sequence. Used to represent settings if you run your build in an explicit proxy server.
* phases: Required sequence. Represents the commands CodeBuild runs during each phase of the build.
    - phases/*/run-as: Optional sequence. Use in a build phase to specify a Linux user that runs its commands.
    - phases/*/on-failure: Optional sequence. Specifies the action to take if a failure occurs during the phase. This can be one of the following values:
        * ABORT - abort the build
        * CONTINUE - continue to the next build phase
    - phases/install: Optional sequence. Represents the commands, if any, that CodeBuild runs during installation.
    - phases/pre_build: Optional sequence. Represents the commands, if any, that CodeBuild runs before the build. For example, you might use this phase to sign in to Amazon ECR, or you might install npm dependencies.
    - phase/build: Optional sequence. Represents the commands, if any, that CodeBuild runs during the build. For example, you might use this phase to run Mocha, RSpec, or sbt.
    - phases/post_build: Optional sequence. Represents the commands, if any, that CodeBuild runs after the build. For example, you might use Maven to package the build artifacts into a JAR or WAR file, or you might push a Docker image into Amazon ECR. Then you might send a build notification through Amazon SNS.
* reports: Optional sequence. Specifies the report group that the reports are sent to. A project can have a maximum of five report groups. Specify the ARN of an existing report group, or the name of a new report group.
    - reports/<report-group>/files: Required sequence. Represents the locations that contain the raw data of test results generated by the report. 
    - reports/<report-group>/file-format: Optional mapping. Represents the report file format. If not specified, JUNITXML is used.
    - reports/<report-group>/base-directory: Optional mapping. Represents one or more top-level directories, relative to the original build location, that CodeBuild uses to determine where to find the raw test files.
    - reports/<report-group>/discard-paths: Optional. Specifies if the report file directories are flattened in the output. If this is not specified, or contains no, report files are output with their directory structure intact. 
* artifacts: Optional sequence. Represents information about where CodeBuild can find the build output and how CodeBuild prepares it for uploading to the S3 output bucket.
    - artifacts/files: Required sequence. Represents the locations that contain the build output artifacts in the build environment.
    - artifacts/name: Optional name. Specifies a name for your build artifact. This name is used when one of the following is true.
    - artifacts/discard-paths: Optional. Specifies if the build artifact directories are flattened in the output. 
    - artifacts/base-directory: Optional mapping. Represents one or more top-level directories, relative to the original build location, that CodeBuild uses to determine which files and subdirectories to include in the build output artifact.
* cache: Optional sequence. Represents information about where CodeBuild can prepare the files for uploading cache to an S3 cache bucket. This sequence is not required if the cache type of the project is No Cache.
    - cache/paths: Required sequence. Represents the locations of the cache. Contains a sequence of scalars, with each scalar representing a separate location where CodeBuild can find build output artifacts, relative to the original build location or, if set, the base directory. 

#### Phases
![image](https://user-images.githubusercontent.com/6731333/125178374-fcaf4680-e1a9-11eb-84e3-0858c20ba3b4.png)

#### Order of Precedence
1. Overrides passed in with the start-build command override everything
1. Values set in the buildspec override values set in the build project
1. Build project values are set globally but can be overridden at any point
    
# CodeStar
AWS CodeStar is a cloud-based service for creating, managing, and working with software development projects on AWS. You can quickly develop, build, and deploy applications on AWS with an AWS CodeStar project. An AWS CodeStar project creates and integrates AWS services for your project development toolchain. Depending on your choice of AWS CodeStar project template, that toolchain might include source control, build, deployment, virtual servers or serverless resources, and more. AWS CodeStar also manages the permissions required for project users (called team members). By adding users as team members to an AWS CodeStar project, project owners can quickly and simply grant each team member role-appropriate access to a project and its resources.

It's basically a project management dashboard which gives you a single interface where you can manage everything from one place. It also offers integration with JIRA for issue tracking. 

CodeStar allows you to:
* Start new software projects on AWS in minutes using templates for web applications, web services, and more
* Manage project access for your team: AWS CodeStar provides a central console where you can assign project team members the roles they need to access tools and resources. These permissions are applied automatically across all AWS services used in your project, so you don't need to create or manage complex IAM policies.
* Visualize, operate, and collaborate on your projects in one place: AWS CodeStar includes a project dashboard that provides an overall view of the project, its toolchain, and important events. You can monitor the latest project activity, like recent code commits, and track the status of your code changes, build results, and deployments, all from the same webpage. You can monitor what's going on in the project from a single dashboard and drill into problems to investigate.

# CodeCommit
AWS CodeCommit is a version control service hosted by Amazon Web Services that you can use to privately store and manage assets (such as documents, source code, and binary files) in the cloud.

#### Integrations
* Amplify
* Cloud9
* CloudTrail
* CloudWatch Events
* CodeBuild
* CodeGuru
* CodePipeline
* CodeStar
* Elastic Beanstalk
* KMS
* Lambda
* SNS
