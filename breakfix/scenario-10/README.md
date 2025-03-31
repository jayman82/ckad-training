# 🧩 Break-Fix Scenario 10: Multi-container Pod Crash

## 🔍 Summary

One container crashes and causes overall pod status to fail.

---

## ✅ Tasks

1. Apply the manifest:  
   ```bash
   kubectl apply -f manifest.yaml
   ```

2. Troubleshoot:  
   ```bash
   kubectl describe pod multi-pod
   ```

3. Fix the issue. Hint:  
   _Replace the exit command with ['sleep', '3600'] to keep it running._

4. Re-apply and verify.

---

## ⛔ Teardown

```bash
kubectl delete -f manifest.yaml
```
