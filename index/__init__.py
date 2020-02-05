import logging
import azure.functions as func
# from azfuncfrontendlib import render_template

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(
        "Frontend"
    )
    # return render_template('index.html',name = 'Jinja')    
    
