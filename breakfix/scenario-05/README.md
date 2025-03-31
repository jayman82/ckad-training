# 🧩 Break-Fix Scenario 05: ConfigMap Not Mounted

## 🔍 Summary

Pod is missing required config values from ConfigMap.

---

## ✅ Tasks

1. Apply the manifest:  
   ```bash
   kubectl apply -f manifest.yaml
   ```

2. Troubleshoot:  
   ```bash
   kubectl logs app-pod
   ```

3. Fix the issue. Hint:  
   _Add 'envFrom' with configMapRef to the container._

4. Re-apply and verify.

---

## ⛔ Teardown

```bash
kubectl delete -f manifest.yaml
```
