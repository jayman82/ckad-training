# 🔧 Multi-Tenant Templating with YAML & Jinja2

This structure allows defining tenants via YAML values and rendering full Kubernetes manifests using Jinja2.

## Example Structure

```
templates/
  deployment.j2
values/
  tenant1.yaml
scripts/
  render_templates.py
```

## Run Example

```bash
python3 scripts/render_templates.py values/tenant1.yaml templates/deployment.j2 > output/tenant1.yaml
```

Great for:
- Generating tenant-specific apps
- Scaling environments
- Reusing baseline templates with variable input
