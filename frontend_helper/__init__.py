from jinja2 import Template
import azure.functions as func

def render_template(template_name,**kwargs):
    with open(f"templates/{template_name}") as f:
        template = Template(f.read())
        return func.HttpResponse(
            template.render(**kwargs),
            mimetype='text/html'
        )