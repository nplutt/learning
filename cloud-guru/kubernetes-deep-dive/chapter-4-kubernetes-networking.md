# Kubernetes Networking

## Common Networking Requirements
* Need scalable networks & service discovery
* Highly dynamic networks are the new normal

## Sample App Requirements
When deploying a load balancer in AWS, an AWS ALB will be deployed with a listener that
points to the pods in the cluster

## Kubernetes Networking Basics
* All nodes can talk
* All pods can talk
* Every pod gets its own ip

Pod network:
* Implements a 3rd party CNI plugin
* Big flat network
* The address that the pods see itself as

Node network:
* 443 HTTPS
* Pod networking

## Kubernetes Services
Pods are ephemeral meaning that they come and go. If demand ramps up ips are created and 
destroyed. How does everything keep up with what pods are deployed and where they are?

Kubernetes uses service objects to provide a level of network abstraction. Every service 
gets a name and an ip address. Kubernetes gurantees that the name and ip of the service
will never change once it's created. This means that all pods in the cluster can access
a service if it exists.

Services know what pods to send traffic to based off of labels. The service knows what 
pods are alive and kicking based off of the end point object for the service. The endpoint
list is always up to date so when a service receives a request it picks one from the list
and sends the request on to that pod.

## Service Types
There a different types of services that all behave a bit differently. They do all provide
the same networking abstraction for a group of pods.
* LoadBalancer: 
  - Provisions a cloud based load balancer with the public cloud platform
  - Some cloud based load balancer services will create a node port service   
* NodePort: 
  - Get cluster wide port
  - Also accessible from the outside of the cluster
  - Can specify the cluster wide port if none is specified a random one is choosen  
* ClusterIP: This is the default
  - Gets its own IP
  - Only accessible from within the pod
    
## Service Network
The service IPs live on the service network is not on a real network. 

Every node on the network has kube-proxy running on it. Once of its main job is to write a bunch of 
pivs/iptables rules on each node that say, any request that you see addressed to this service
network, rewtrite the headers and forward the request to the service network. 

cbr0: dumb bridge to send packets which looks at where to send requests to

#### kube-proxy IPTABLES Mode
* Default since Kubernetes 1.2
* Doesn't scale great
* Not really designed for load balancing

#### kube-proxy IPVS Mode
* Stable (GA) since Kubernetes 1.11
* Uses Linux kernel IP Virtual Server
* Native layer 4 load balancer

## Recap
Node Network
* All nodes need to talk to each other
  - Kubelet <-> API server
  - Pod network ports  
* Not implemented by Kubernetes

Pod Network
* Implemented via CNI plugins
* Big & flat 
* IP per pod

Should never reach out to a pod directly. Communication should always be done via a service.



