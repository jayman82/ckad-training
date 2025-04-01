
# 🧪 CKAD Lab – Demo App & Troubleshooting Guide

## 📦 Deployable App Stack (demo-api + postgres)

This demo includes:
- A Flask API with `/write` and `/read`
- PostgreSQL as a StatefulSet
- Namespaces: `app`, `db`
- PVC-backed storage, ConfigMap, Secret, Service, Ingress

---

## 🚀 How to Deploy

1. **Build the Docker Image** (if using local version):
```bash
cd demo-app/app
docker build -t demo-api:latest .
```

2. **Switch to the project root and run:**
```bash
bash scripts/deploy.sh
```

3. **Access the App** (if using Ingress):
- URL: `http://demo.local` (requires local DNS like `/etc/hosts`)
- Or use `kubectl port-forward`:
```bash
kubectl port-forward -n app svc/demo-api 8080:80
```

---

## 🧼 How to Tear Down
From the project root:
```bash
bash scripts/teardown.sh
```

---

## 🧰 Common Issues & Fixes

### ❌ `ImagePullBackOff`
You didn’t build `demo-api:latest` OR your cluster can’t access it.
- Make sure you ran:
```bash
docker build -t demo-api:latest .
```
- If using `kind`, run:
```bash
kind load docker-image demo-api:latest
```

### ❌ `CreateContainerConfigError` on `postgres-0`
Usually means missing secrets or configmap.
Check:
```bash
kubectl describe pod postgres-0 -n db
kubectl get secrets -n db
```

---

## 🌐 Alternative: Use a Public Image (Optional)

You can use this prebuilt image:
```yaml
image:
  repository: ghcr.io/your-org/demo-api
  tag: latest
```

Update your `deployment.yaml` or `values.yaml` to reference it instead of `demo-api:latest`.

---

## 📁 Where to Deploy From

Always run deploy/teardown scripts from the project root:
```bash
ckad-lab/
├── demo-app/
├── scripts/
├── k8s/
```

Otherwise, `k8s/base` won’t be found.

---

Happy learning! 🧠🐳💻
