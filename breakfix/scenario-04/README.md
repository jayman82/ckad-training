# 🧩 Break-Fix Scenario 04: Job with Bad Command

## 🔍 Summary

Job fails to complete due to a bad container command.

---

## ✅ Tasks

1. Apply the manifest:  
   ```bash
   kubectl apply -f manifest.yaml
   ```

2. Troubleshoot:  
   ```bash
   kubectl logs job/fail-job
   ```

3. Fix the issue. Hint:  
   _Fix the command to use something valid like ['echo', 'Hello World']._

4. Re-apply and verify.

---

## ⛔ Teardown

```bash
kubectl delete -f manifest.yaml
```
