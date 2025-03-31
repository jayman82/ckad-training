# 🧠 Kubernetes Command Cheat Sheet

Quick reference for common kubectl commands and examples:

## 🔍 Cluster & Resource Info

```bash
kubectl get nodes
kubectl get pods -A             # View all pods across namespaces
kubectl get svc                 # List services
kubectl describe pod <pod-name>  # Detailed info about a pod
kubectl logs <pod-name>        # View pod logs
kubectl exec -it <pod> -- bash # Open a shell inside a container
```

## ⚙️ Create & Apply Resources

```bash
kubectl apply -f <file.yaml>     # Apply manifest
kubectl delete -f <file.yaml>    # Delete resources
kubectl create deployment nginx --image=nginx --dry-run=client -o yaml > nginx.yaml
```

## 🧪 Debugging & Testing

```bash
kubectl explain pod              # Get field definitions for a resource
kubectl get events --sort-by='.metadata.creationTimestamp'
kubectl rollout status deployment/<name>
kubectl rollout undo deployment/<name>
```

## 🔐 ConfigMaps & Secrets

```bash
kubectl create configmap my-config --from-literal=MODE=prod
kubectl create secret generic my-secret --from-literal=PASSWORD=pass123
```

## 📦 Namespaces

```bash
kubectl get ns
kubectl create ns dev
kubectl get pods -n dev
```

## 🔁 Job & CronJob

```bash
kubectl create job hello --image=busybox -- echo "Hello!"
kubectl get jobs
```

## 🔒 RBAC

```bash
kubectl create role pod-reader --verb=get,list,watch --resource=pods -n default
kubectl create rolebinding read-pods --role=pod-reader --user=jane -n default
```

## 🌐 Services & Ingress

```bash
kubectl expose pod mypod --port=80 --target-port=8080 --type=ClusterIP
kubectl get ingress
```

## 🧼 Cleanup

```bash
kubectl delete pod <name>
kubectl delete all --all         # Delete all resources in current namespace
```

🧠 Pro Tip: Use aliases in your shell config:
```bash
alias k=kubectl
complete -F __start_kubectl k
```
