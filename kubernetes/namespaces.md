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
* max section: sets the maximum limits that a container in a pod can set
* min section: sets the minimum limits that a container in a pod can set

## More Reading
- Namespace network policies

## Notes
- Could be nice to have one namespace to make service discovery easier

Isto vs Namespace to make public or private
* One private & one public load balancer 
* Isto may supersede some of the namespace networking options
