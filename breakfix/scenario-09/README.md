# 🧩 Break-Fix Scenario 09: Ingress Backend Mismatch

## 🔍 Summary

Ingress refers to a service that doesn't exist.

---

## ✅ Tasks

1. Apply the manifest:  
   ```bash
   kubectl apply -f manifest.yaml
   ```

2. Troubleshoot:  
   ```bash
   kubectl describe ingress test-ingress
   ```

3. Fix the issue. Hint:  
   _Update the service name to match an actual running service._

4. Re-apply and verify.

---

## ⛔ Teardown

```bash
kubectl delete -f manifest.yaml
```
