
# 🧪 CKAD Lab Project – Kubernetes Learning Toolkit

Welcome to the ultimate hands-on Kubernetes learning environment, built to help you prepare for the **Certified Kubernetes Application Developer (CKAD)** exam and beyond!

---

## 🎯 What's Included

### ✅ Core Modules
- **Aggressively Commented YAML** for:
  - Pods, Deployments, Services, Ingress, Volumes, ConfigMaps, Secrets, and more
- **Multi-Tenant Templating** using Jinja2 + values files
- **Environment-Aware Helm Charts** (`dev`, `staging`, `prod`)
- **DevContainer** and `.gitignore` for GitHub/VS Code use

### 🔧 Break-Fix Challenge Labs (1–10)
Pre-built broken scenarios to fix, including:
- CrashLoopBackOff
- Probes and Jobs
- Volume/RBAC/Ingress issues
- Secret misconfigurations
- Includes manifest + README for each scenario

### 🌐 Deployable Demo App Stack
- Flask API with `/write` & `/read`
- PostgreSQL StatefulSet with PVC
- Namespaces, Secrets, ConfigMaps, Services, Ingress
- `deploy.sh` and `teardown.sh` for easy local testing
- Works great with Rancher Desktop

---

## 🛠️ How to Use

### 🚀 Quick Start (Standalone)
```bash
cd scripts/
bash deploy.sh  # deploys namespaces + demo stack
bash teardown.sh  # cleans up everything
```

### 🔨 Try a Break-Fix Lab
```bash
cd breakfix/scenario-01/
kubectl apply -f manifest.yaml
# Follow the README to fix and learn!
```

### 📦 Install with Helm
```bash
helm install demo-api ./demo-app/helm/demo-api -n app --create-namespace -f demo-app/helm/demo-api/values-dev.yaml
```

---

## 🧰 Developer Environment
This project includes:
- `.devcontainer` for VS Code with `kubectl`, `helm`, `kustomize`
- Shell aliases + autocompletion in `setup-aliases.sh`
- Templating system (`render_templates.py`) for YAML generation from values

---

## 📚 Learn & Customize
- `docs/` includes glossary, cheat sheet, and walk-throughs
- Use templating to create multi-tenant deployments with:
  ```bash
  python scripts/render_templates.py values/tenant1.yaml templates/deployment.j2
  ```

---

## 🤝 Contributing & Extending
This project is modular—use it to:
- Practice CKAD tasks
- Train new Kubernetes engineers
- Develop your own Helm charts or test suites

---

Built to be fully self-contained, flexible, and exam-focused.  
Happy learning and good luck with your CKAD! 🎓🐳
