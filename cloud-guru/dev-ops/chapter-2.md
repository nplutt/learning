# SDLC Automation

## What is CI/CD

#### Definitions
* Continuous: forming a series with no exceptions or reversals.
* Integraton: combine one thing with another to form a whole.
* Deployment: the action of bringing resources into effective action.

#### Benefits
* Build faster
* Decrease code review time
* Automatic
* Faster fault isolation
* Additional deployment features

## AWS CodeBuild

#### What is CodeBuild
* A fully managed build service
* Compiles your code
* Runs unit tests
* Produces artifacts that are ready to deploy
* Eliminates the need to provision/manage/scale your own build servers
* Provides pre-packaged build environments
* Allows you to build your own customized build environment
* Scales automatically to meet your build requirements

#### Benefits of CodeBuild
* It's fully managed
* It's on demand
* It's preconfigured

## AWS CodeDeploy

#### What is CodeDeploy
A managed deployment service that automates deployments to:
* Amazon EC2 instances
* On-premises instances
* AWS Lambda functions

Makes it easier to:
* Rapidly deploy new features
* Update Lambda function versions
* Avoid downtime during deployment

#### Using CodeDeploy
1. Create EC2 instance role with full access code deploy policy
2. Create IAM role for code deploy to use with aws code deploy access policy
3. Create load balancer for instances to use
4. Create a target group
5. Launch instances into the autoscaling group with user data that installs the code deploy agent and
starts it
6. Go to code deploy
7. Create application & deployment group
8. Select deployment type
9. Select the autoscaling group
10. Create a deployment & run it

A appspec.yml in the root of the project is what defines the install and deployment process once 
on the server.

## AWS CodePipeline

#### Using CodePipeline
1. Create a pipeline
2. Add a source stage
3. Add a build stage
4. Add deploy stage
5. Create the pipeline
6. Run the pipeline

## Testing

#### Why do we test
* Meet the requirements defined
* Ensures the code performs in an acceptable time
* Ensure it's usable
* Ensure it responds correctly to all kinds of inputs
* Achieves the result that the program desires

#### Automated testing
* Automatic execution of tests
* Comparison of acutal outcomes to predicted outcomes
* Fast, continuous feedback
* Immediate notification
* Save resources

#### Where to implement tests
* Add a test stage to code pipeline
* Can add manual approval at pipeline stage

## Artifacts

#### What are artifacts
An artifact is a product or byproduct produced during the software development process:
* Compiled binaries
* Source code
* Documentation
* Use cases
* Class diagrams

AWS has a service called artifact and it has nothing to do with artifacts

## Deployment Strategies

#### Single Target Deployment
* Used for small development projects, especially when legacy or non-ha infrastructure is involved
* When it's initiated a new application version is installed on the target server
* A brief outage occurs during installation. There's no secondary servers, so testing is limited. Rollback
involves removing the new version and installing the previous.

#### All at once deployment
* Deployment happens in once step, just like single target deployments
* With this method the destination is multiple targets
* More complicated than single target, often requiring orchestration tooling
* Shares negatives of single target. No ability to test, still has deployment outages, and less than ideal 
rollback

#### Minimum in-service deployment
* Deployment happens in multiple stages
* Deployment happens to as many targets as possible while maintaining the minimum in service targets
* A few moving parts, orchestration and health checks are required
* Allows automated testing, deployment targets are assessed and tested prior to continuing
* Generally no downtime
* Often quicker and less stages than rolling deployment

#### Rolling deployment
* Deployment happens in multiple stages, number of targets per stage is user defined
* Moving parts, orchestration and health checks are required
* Overall applicable health isn't necessarily maintained
* Can be the least efficient deployment based on time taken
* Allows automated testing, deployment targets are assessed and tested prior to continuing
* Generally no downtime, assuming the number of targets per run isn't large enough to impact the application
* Can be paused, allowing limited version testing

#### Blue green deployment
* Requires advanced orchestration tooling
* Carries significatn cost - maintaining 2 environments for the duration of the deployments
* Deployment process is rapid - entire environment is deployed all at once
* Cutover and migration is clean and controlled (DNS change)
* Rollback is clean, DNS regression
* Health and performance of entire green environment can be tested prior to cutover
* Using advanced template systems, such as cloudformation , entire process can be fully automated

#### Canary deployment
* Keep blue active
* Use Route53 weighted round robin



 
 