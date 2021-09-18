# Cluster Architecture

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
You can create and modify node objects using kubectl. When a Node object is 