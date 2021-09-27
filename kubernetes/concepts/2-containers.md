# [Containers](https://kubernetes.io/docs/concepts/containers/)

Each container run is repeatable; the standardization from having dependencies 
included means that you get the same behavior wherever you run it.

A container image is a ready to run software package, containing everything needed
to run an application. By design a container is immutable: you cannot change the code
of a container that is already running. To make a change you need to build a new container.

The container runtime is the software that is responsible for running containers.
Kubernetes supports several runtimes: Docker, containerd, CRI-O and any implementation
of the Kubernetes CRI (container runtime interface)

## Images
A container image represents binary data that encapsulates an application and all its
software dependencies. Container images are executables software bundles that can
run standalone.

#### Updating Images
The `imagePullPolicy` for a container and the tag of the image affect when the kubelet
attempts to pull the image. Here's a list of the values:
* IfNotPresent: the image is pulled if it isn't already present
* Always: everytime the kubelet launches a container the kubelet queries the container
  image registry to resolve the name of the digest. If the kubelet has a container image 
  with that exact digest cached locally, the kubelet uses its cached image.
* Never: the kubelet doesn't try to fetch the image. If the image is already present locally
  the kubelet attempts to launch the container.
  
If the imagePullPolicy is not set it defaults to Always.

## Container Environment
The Kubernetes Container environment provides several important resources to Containers:
* A filesystem, which is a combination of an image and one or more volumes
* Information about the Container itself
* Information about other objects in the cluster

#### Container Information
The hostname of a Container is the name of the Pod in which the Container is running.
It is available through the hostname command or the gethostname function call in libc.

The Pod name and namespace are available as environment variables through the downward API.

#### Cluster Information
A list of all services that were running when a Container was created is available to that Container as
environment variables. The list is limited to services within the same namespace as the new Container's Pod 
and Kubernetes control plane services.

## Runtime Class
RuntimeClass is a feature for selecting the container runtime configuration. The container
runtime configuration is used to run a Pod's containers.

#### Motivation
Setting a different RuntimeClass between different Pods to provide a balance of performance vs security.
For example, if part of your workload deserves a high level of information security assurance, you might 
choose to schedule those Pods so that they run in a container runtime that uses hardware virtualization. 

## Container Lifecycle Hooks
Kubernetes provides Conatiners with lifecycle hooks, which enable Containers to be aware of
events in their management lifecycle and run code implemented in a handler when the corresponding 
hook is executed.

#### Container Hooks
There are two hooks exposed to Containers:
* PostStart hook is executed immediately after a container is created. However there is no guarantee
  that the hook will execute before the container ENTRYPOINT. 
* PreStop hook is called immediately before a container is terminated due to an API request or management
event such as liveness/startup probe failure, preemption, resource contention, and others. 