# 🧩 Break-Fix Scenario 08: RBAC Role Missing Permissions

## 🔍 Summary

Role is missing required permissions to list pods.

---

## ✅ Tasks

1. Apply the manifest:  
   ```bash
   kubectl apply -f manifest.yaml
   ```

2. Troubleshoot:  
   ```bash
   Check RBAC access denied error using 'kubectl auth can-i'
   ```

3. Fix the issue. Hint:  
   _Add 'list' and 'watch' to the Role's verbs._

4. Re-apply and verify.

---

## ⛔ Teardown

```bash
kubectl delete -f manifest.yaml
```
