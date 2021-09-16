# Storage in Kubernetes

## Kubernetes Big Picture Storage
Kubernetes Volumes: All about decoupling storage from pod. 
  * Pod lays claim to volume 
  * Multiple pods can claim the same volume

Volumes are a persistent place to store data for pods. 

Storage is vital! File and block are first class citizens in Kubernetes.
* Standards based
* Pluggable backend
* Rich API

Fundamental storage requirements
* Speed
* Replicated
* Resiliency
* Etc..

Storage providers give pods multiple interfaces to consume storage through.

CSI: Container Storage Interface
* Makes it easy to interface many different storage options with Kubernetes

* PersistentVolume (PV) [Stroage: 20GB]
* PersistentVolumeClaim (PVC) [Ticket to use PV]
* StorageClass (SC) [Makes it dynamic]

## Container Storage Interface (CSI)

All of the code that hooks storage providers into Kubernetes lives outside of the project.
CSI is an open standard that can be used across any container orchestration tool that 
supports CSI.

## Persistent Volumes and Persistent Volume Claims

PV: On GCP persistent disk comes in two forms of Standard and SSD
PVC: Used like a ticket to allow a pod to use a persistent volume

PV access modes:
* RWO: ReadWriteOnce
* RWM: ReadWriteMany
* ROM: ReadOnlyMany

* Not all volumes support all modes
* A PV can only have one active PVC/AccessMode

Reclaim policy: What the cluster does when a claim on the volume is released
* Retain: Released or pod fails and the volume sticks around
* Delete: Release a claim on the volume and kubernetes will delete it

To use the volume in a pod, it must define a PVC and mount the storage on the pod.

## Dynamic Provisioning with StorageClasses
A StorageClass is defined in the yaml config. 
