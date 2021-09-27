# [Cluster Architecture](https://kubernetes.io/docs/concepts/architecture/)

## [Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/)
Kubernetes runs workloads by placing containers into Pods and running them on Nodes. A node may be a 
virtual or physical machine depending on the cluster. Nodes are managed by the control plane.

#### Management
Nodes can be added to the API server wither manually or by self registering. Once a node is registered
Kubernetes creates a Nodde object internally. Then Kubernetes checks that a kubelet has registered to the API 
server that matches the `metadata.name` field for the Node. If the Node is healthy, then it is eligible to run a 
pod. 

#### Self Registration of Nodes
When the kubelet flag `--register-node` is true, the kubelet will attempt to register itself with the API server.

When the Node authorization mode and NodeRestriction admission plugin are enabled, kubelets are only authorized
to create/modify their own Node resource.

#### Manual Node Administration
You can create and modify node objects using kubectl. 

To mark a node as unschedulable, run `kubectl cordon $NODENAME`

Note: Before cordoning a node you'll want to safetly drain it

#### Node Status
A nodes status contains:
* Addresses
  - HostName: The hostname reported by the node's kernel. Can be overriden using the `--hostname-override` flag.
  - ExternalIP: The IP of the node that is externally routable
  - InternalIP: Ip on the node that is routable within the cluster
* Conditions
  - Ready: True if Node is healthy and ready to accept pods, False if Node is not healthy and not accepting pods.
    If the status of the Ready condition remains `Unkown` or `False` for longer than the `pod-eviction-timeout` then
    the node controller triggers an API initiated eviction for all Pods assigned to that node. The default
    eviction timeout is 5 minutes.
  - DiskPressure: True if pressure exists on the disk size; otherwise False
  - MemoryPressure: True if pressure exists on node memory; otherwise False
  - PIDPressure: True if pressure exists on processes i.e. too many processes; otherwise False
  - NetworkUnavailable: True if network on Node is not configured correctly; otherwise False
* Capacity and Allocatable: Describes teh resources available on the node: CPU, memory, and maximum number of 
  pods that can be scheduled on that node.
* Info: General information about the node, kernel version, Kubernetes version, container runtime details, and which
  os the node uses.

#### Heartbeats
Hearbeats sent by the nodes help the cluster determine the availability of each node and take action if failures
are detected. 

Two forms of heartbeats:
* updates to the `.status` of a Node
* Lease objects within the `kube-node-lease` namespace. Each node has an associated Lease object.

Lease is a lightweight resource, using Leases for heartbeats in larger clusters reduces the performance impact
of these updates for large clusters.

#### Node Controller
The node controller is a Kubernetes control plane component that manages various aspects of nodes. The controller 
does the following:
1. Assigns a CIDR block to the node when it is registered
1. Keeps an internal list of nodes and when running in a cloud environment and whenever a node is unhealthy, the node 
   controller asks the cloud provider if the VM is still available. If not the node controller deletes it from it's list.
1. Monitoring the nodes' health.
  * If a node is unreachable, it updates the Node's `.status` to be `ConditionUnknown`
  * If a node remains unreachable, triggers an API initiated eviction for all the pods on the unreachable node.

#### Rate Limits on Eviction
By default the `--node-eviction-rate` is set to 0.1 so it won't evict more than 1 node per 10 seconds.

The node eviction behavior changes when a node in a give AZ becomes unhealthy. The node controller checks the 
percentage of nodes in the zone that are unhealthy at the same time.

#### Resource Capacity Tracking
Node objects track information about the Node's resource capacity e.g. CPU & memory 

The Kubernetes scheduler ensures that there are enough resources for all the pods on a Node.

## [Control Plane-Node Communication](https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/)
This section covers the communication paths between the control plane (apiserver) and the Kubernetes cluster.
The intent is to allow users to customize their installation ato harden the network configuration such that the
cluster can be run on an untrusted network.

#### Node to Control Plane
Kubernetes has a hub and spoke API pattern. All API usage from the node or pods terminates at the apiserver.

Nodes should be provisioned with the public root certificate for each cluster such that they can connect securely
to the apiserver along with valid client credentials. 

Pods that wish to connect to the apiserver can do so securely by leveraging a service account so that Kubernetes
will automatically inject the public root cert and a valid bearer token into the pod when instantiated. The 
kubernetes service in the default namespace is configured with a viratual IP that is redirected via kube-proxy
to the HTTPS endpoint on the apiserver.

#### Control Plane to Node
There are two communication paths from the control plane (apiserver) to the nodes.
1. From the apiserver to the kubelet process which runs on each node
1. From the apiserver to any node, pod, or service running through the apiserver's proxy functionality

**apisever to kubelet** the connections from the apiserver to the kubelet are used for:
* Fetching logs from pods
* Attaching through kubectl to running pods
* Providing the kubelet's port-forwarding functionality

These connections terminate at the kubelet's HTTPS endpoint. By default the apiserver doesn't verify the 
kubelet's cert, which makes the connection subject to man in the middle attacks. To verify this connection,
use the `--kubelet-certificate-authority` flag to provide the apiserver with a root cert bundle. If that's not
possible use SSH tunneling to avoid using an untrusted network.

**SSH tunnels** (deprecated) Kubernets supports SSH tunnels to protect the control plane to nodes communication path.

## Controllers
In Kubernetes, controllers are control loops that watch the state of your cluster, then make or request changes
where needed. Each controller tries to move the current cluster state closer to the desired state.

#### Controller Pattern
A controller tracks at least one Kubernetes resource type. These objects have a spec field that represents
the desired state. The controller(s) for that resource are responsible for making the current state come
closer to that desired state.

In Kubernetes the controller usually sends messages to the apiserver that have useful side effects.

#### Design
Kubernetes uses lots of controllers that each manage a particular aspect of cluster state. Most commonly,
a particular control loop (controller) uses one kind of resource as its desired state, and has a different
kind of resource that it manages to make that desired state happen.

#### Ways of Running Controllers
Kubernetes comes with a set of built-in controllers that run inside the `kube-controller-manager`. These
built in controllers provide important core behaviors.

You can find controllers that run outside of the control plane, to extend Kubernetes (e.g. istio). Or if 
you want, you can write a new controller yourself. Controllers can be written as a set of Pods, or externally
to Kubernetes. What fits best depends on what the controller does.

## Cloud Controller Manager
The cloud-controller-manager is a Kubernetes control plane component that embeds cloud-specific control logic.
The cloud controller manager lats you link your cluster into a specific cloud provider's API, and seperates
out the components that interact with that cloud platform from components that only interact with your cluster.

By decoupling the logic between Kubernetes and underlying cloud infrastructure, the cloud controller managers
component enables cloud providers to release features at a different pace compared with the Kubernetes project.

The cloud controller manager runs in the control plane as a replica set of processed usually as containers inside
Pods. Each cloud-controller-manager implements multiple controllers in a single process.

#### Cloud Controller Manager Functions
**Node Controller**: The node controller is responsible for creating Node objects when new servers are created
in the cloud infra. The node controller performs the following functions:
1. Initialize the Node object for each server that the controller discovers
1. Annotating and labelling the Node object with cloud-specific information, such as the region and available
  CPU, memory, etc. that is available
1. Verifying the node's health. In case the node becomes unresponsive, this controller checks the cloud provider's
   API to see if the server has been deactivated / deleted / terminated. If the node has been deleted from the 
   cluster the controller deletes the Node object from the cluster.
   
**Route Controller**: The route controller is responsible for configuring routes in the cloud appropriately so
that containers on different nodes in the cluster can communicate with each other. Depending on the cloud 
prover, the route controller may also allocate blocks of IP addresses for the Pod network.

**Service Controller**: service integrated with cloud components such as load balancers, IP addresses, network
packet filtering, and target health checking. The service controller interacts with the cloud provider's 
APIs to setup this infrastructure.

#### Authorization
The cloud controller manager requires access to various API objects such as Node, Route, Service, Event, & ServiceAccount
to function properly.

## Garbage Collection 
Garbage collection is a term Kubernetes uses when cleaning up various resources:
* Failed pods
* Completed jobs
* Objects w/o owner references
* Unused containers and container images
* Dynamically provisioned PersistentVolumes with StorageClass reclaim policy of Delete
* Stale or expired CertificateSigningRequests(CSRs)
* Nodes deleted in the following scenarios
  - On a cloud when the cluster uses the cloud controller manager 
  - On premises when the cluster uses an addon similar to a cloud controller manager
* Node lease objects

#### Owners and Dependents
Many objects in Kubernetes link to eachother through owner references. Owner references tell the control plane
which objects depend on others. Kubernetes uses the owner references to give the control plane, and other API
clients, the opportunity to clean up related resources before deleting objects.

#### Cascading Deletion
Kubernetes checks for and deletes objects that no longer have owner references, like the pods left behind when
you delete a ReplicaSet. 

#### Garbage Collection of Unused Containers & Images
The kubelet performs garbage collection on unused images every 5 minutes and on unused containers every minute.
You should avoid using external garbage collection tools, since these can break the kubelet behavior.

**Container image lifecycle** Kubernetes manages the lifecycle of all images through its image manager, which
is part of the kubelet. The kubelet considers the following disk usage limits when making collection decisions:
* HighThresholdPercent
* LowThresholdPercent

Disk usage above the configured HighThresholdPercent triggers garbage collection, which deletes images in
order based on the last time they were used, starting with the oldest first. The kubelet deletes images until
disk usage reaches the LowThresholdPercent value.

**Container image garbage collection** kubelet garbage collects unused containers based on the following variables:
* MinAge: The min age at which kubelet can garbage collect a container (disable by setting to 0)
* MaxPerPodContainer: the max number of dead containers each Pod pair can have. (disable by setting to 0)
* MaxContainers: the max number of dead containers the cluster can have (disable by setting to 0)

