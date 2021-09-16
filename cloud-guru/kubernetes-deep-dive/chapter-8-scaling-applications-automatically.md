# Scaling Applications Automatically

## Big Picture
As demand goes up, spin up more pods and nodes. The HPA will increase the replica count in a deployment.
The cluster autoscaler will scale up the nodes.

## Horizontal Pod AutoScaler (HPA)
Define the HPA like any other resource in the API and there is only one HPA per deployment.

The HorizontalPodAutoscaler defines:
* the deployment it is tied too
* the min replicas
* the max replicas
* the target CPU utilization

The deployment defines:
* resource CPU request (soft limit)
* resource CPU limit (hard limit)

Autoscaling V2 will support memory and metrics as well.

## Cluster AutoScaler Theory
Build your Kubernetes cluster with autoscaling enabled.

Cluster AutoScaling only works if your pods have resource requests, the CAT only looks at the 
requested resources.

Cluster AutoScaler wakes up and checks things every 10 seconds.

Warnings:
* Don't mess with the node pools.
* Check your cloud for support
* Test performance on big clusters

