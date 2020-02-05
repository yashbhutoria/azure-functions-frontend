import pathlib
from jinja2 import Template

def sibling_path(name):
    return pathlib.Path(__file__).parent / name

def render_template(template_name,**kwargs):
    with open(sibling_path(f"templates/{template_name}")) as f:
        template = Template(f.read())
        return func.HttpResponse(
            template.render(**kwargs),
            mimetype='text/html'
        )