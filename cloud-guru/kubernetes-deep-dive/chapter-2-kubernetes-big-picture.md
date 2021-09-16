# Kubernetes Big Picture

## Kubernetes API
* Restful API to do CRUD on resources in Kubernetes
* Interact with the API via kubectl
* Define different parts of apps in yaml files that will change overall
  desired state in the cluster, which will kick off the control plane to change
  the current state of the cluster to be the desired state.

#### Multiple API groups
* Core: pod, svc
* Apps: deploy, sts, ds
* Authorization: role, rb
* Storage: pv, pvc  

#### Feature Levels
`kubectl get apiservices`

* Alpha: hairy and user beware e.g. v1alpha1
* Beta: taking shape and becoming stable e.g. v1beta1
* GA: ready for production e.g. v1, v2, etc.

## Kubernetes Objects

#### Pods
Kubernetes doesn't run containers, it deploys pods which can contain one or more containers.
* Contains one or more containers
* Atomic unit of scheduling
* Object on the cluster
* Defined in the v1 API group

#### Deployment
Scalability and application releases
* Object on the cluster
* Defined in the apps/v1 API group
* Scaling
* Rolling updates

#### Daemon Sets
Ensures that one and only one pod is running on every node

#### Statesful Sets
For pods or applications with particular stateful requirements

#### Review the kubernetes api documentation

## Setting Up Your Own Cluster
* Docker desktop
* Docker has an online version

