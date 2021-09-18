# Network Policies
In order to control traffic flow at the IP or port level (layer 3 or 4), then consider using Kubernetes 
NetworkPolicies for particular applications in your cluster. NetworkPolicies are an application centric
construct which allows you to specify how a pod is allowed to communicate with various network entities.

Entities that a Pod can communicate with are identifies through a combo of the following 3 identifiers:
1. Other pods that are allowed (exception: a pod cannot block access to itself)
1. Namespaces that are allowed
1. IP blocks (exception: traffic to and from the node where a Pod is running is always allowed, regardless of the Pod or node)

IP blocks are identified via CIDR blocks