# Kubernetes Deployments

## Theory of Deployments

* Kubernetes doesn't allow you to just run a container, it needs to be wrapped in a pod.
* Pods can be wrapped in a deployment
* Replica sets are created via a deployment
* Deployments can only have one pod
* Never modify a replica set
* Deployments know what pods to manage based off of labels

```bash
# Waits for a deployment to finish and outputs logs statements
kubectl rollout status deployment/eidos-deployment

# Tails logs from deployment
kubectl logs -f deployment/eidos-deployment

# Tails logs from deployment replica set
kubectl logs -f rs/eidos-deployment-658f79dfbb
```