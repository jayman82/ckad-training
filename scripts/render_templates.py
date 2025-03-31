import sys, yaml
from jinja2 import Template

def render(values_path, template_path):
    with open(values_path) as f:
        values = yaml.safe_load(f)
    with open(template_path) as f:
        template = Template(f.read())
    print(template.render(**values))

if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2])
