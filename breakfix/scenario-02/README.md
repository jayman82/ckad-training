# 🧩 Break-Fix Scenario 02: Service Misrouting

## 🔍 Summary

Service does not match any pods due to selector mismatch.

---

## ✅ Tasks

1. Apply the manifest:  
   ```bash
   kubectl apply -f manifest.yaml
   ```

2. Observe the issue and investigate using:  
   ```bash
   kubectl describe svc broken-service
   ```

3. Fix the problem. Hint:  
   _Update service selector to match pod label: app: myapp_

4. Confirm the fix by checking resource status again.

---

## ⛔ Teardown

```bash
kubectl delete -f manifest.yaml
```
