# 🧩 Break-Fix Scenario 03: Readiness Probe Fails

## 🔍 Summary

Readiness probe is misconfigured and fails to detect the pod as ready.

---

## ✅ Tasks

1. Apply the manifest:  
   ```bash
   kubectl apply -f manifest.yaml
   ```

2. Troubleshoot:  
   ```bash
   kubectl describe pod probe-pod
   ```

3. Fix the issue. Hint:  
   _Update the readinessProbe path to '/' for nginx._

4. Re-apply and verify.

---

## ⛔ Teardown

```bash
kubectl delete -f manifest.yaml
```
