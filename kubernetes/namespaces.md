# Namespaces

Most Kubernetes distros ship with 3 default namespaces:
1. default: Nothing special and can be deleted. Don't use this in large systems.
1. kube-system: Leave this alone
1. kube-public: Not used for much

Create different namespaces to separate your services into manageable chunks.

When deploying a pod the namespace can be specified in two ways:
- `--namespace my-namespace` in kubectl
- namespace specified in yml which will always override any namespace specified in the kubectl command

All kubectl commands are run in the active namespace

`kubens` tool is very nice for managing the current namespace context

## Cross Namespace Communication
It is possible to have one service in a namespace communicate with a service in another namespace.

By using the expanded DNS name: `service-name.svc.cluster.local` -> `service-name.namespace-name.svc.cluster.local`

Namespace communication can be restricted using namespace network policies.

## Organizational Structure
- Less than 10 microservices: one namespace is probably fine
- More than 10 microservices: one namespace per team (maybe)
- More than 100 microservices: more than one namespace per team and maybe more than one cluster

## Namespace Level Resource and Limits 
To prevent teams setting request and limit numbers too high, namespaces can set ResourceQuotas and 
LimitRanges.

ResourceQuotas: After creating Namespaces, you can lock them down using ResourceQuotas. ResourceQuotas are very powerful, 
but let’s just look at how you can use them to restrict CPU and Memory resource usage.
* requests.cpu: the maximum combined CPU requests for all the containers in the Namespace
* requests.memory: the max combined memory requests for all the containers in the Namespace
* limits.cpu: the maximum combined CPU limits for all the containers in the namespace
* limits.memory: the maximum combined memory limits for all the containers in the namespace

LimitRange: You can also create a LimitRange in your Namespace. Unlike a Quota, which looks at the Namespace as a whole, 
a LimitRange applies to an individual container. This can help prevent people from creating super tiny or super large 
containers inside the Namespace.
* default section: sets the default limits for a container in a pod. If a container doesn't explicitly set the limits then
these values will be applied to the container.
* defaultRequest: sets the default requests for a container in a pod
* max section: sets the amximum limits that a container in a pod can set
* min section: sets the minimum limits that a container in a pod can set

## Network Policies
In order to control traffic flow at the IP or port level (layer 3 or 4), then consider using Kubernetes 
NetworkPolicies for particular applications in your cluster. NetworkPolicies are an application centric
construct which allows you to specify how a pod is allowed to communicate with various network entities.

Entities that a Pod can communicate with are identifies through a combo of the following 3 identifiers:
1. Other pods that are allowed (exception: a pod cannot block access to itself)
1. Namespaces that are allowed
1. IP blocks (exception: traffic to and from the node where a Pod is running is always allowed, regardless of the Pod or node)

IP blocks are identified via CIDR blocks



## More Reading
- Kubernetes aware CD system called spinnaker
- Namespace network policies
