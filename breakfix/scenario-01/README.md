# 🧩 Break-Fix Scenario 01: CrashLoopBackOff Pod

## 🔍 Summary

Pod fails to start due to an invalid command.

---

## ✅ Tasks

1. Apply the manifest:  
   ```bash
   kubectl apply -f manifest.yaml
   ```

2. Observe the issue and investigate using:  
   ```bash
   kubectl describe pod example-pod
   ```

3. Fix the problem. Hint:  
   _Change the command to a valid one like ['sleep', '3600']._

4. Confirm the fix by checking resource status again.

---

## ⛔ Teardown

```bash
kubectl delete -f manifest.yaml
```
