import logging
import azure.functions as func
from __app__.frontend_helper import render_template

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return render_template('index.html',name = 'Jinja')
