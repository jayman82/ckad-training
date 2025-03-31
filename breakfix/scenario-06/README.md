# 🧩 Break-Fix Scenario 06: Secret Key Not Found

## 🔍 Summary

Pod fails due to referencing a nonexistent secret key.

---

## ✅ Tasks

1. Apply the manifest:  
   ```bash
   kubectl apply -f manifest.yaml
   ```

2. Troubleshoot:  
   ```bash
   kubectl describe pod secret-pod
   ```

3. Fix the issue. Hint:  
   _Change 'key' to 'password' to match the secret definition._

4. Re-apply and verify.

---

## ⛔ Teardown

```bash
kubectl delete -f manifest.yaml
```
