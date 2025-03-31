# 🧩 Break-Fix Scenario 07: PVC Not Bound

## 🔍 Summary

Pod fails to mount volume because PVC is unbound.

---

## ✅ Tasks

1. Apply the manifest:  
   ```bash
   kubectl apply -f manifest.yaml
   ```

2. Troubleshoot:  
   ```bash
   kubectl describe pvc mypvc
   ```

3. Fix the issue. Hint:  
   _Make sure a matching PersistentVolume exists._

4. Re-apply and verify.

---

## ⛔ Teardown

```bash
kubectl delete -f manifest.yaml
```
