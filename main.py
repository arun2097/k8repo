from fastapi import FastAPI, Request, 
from fastapi.templating import jinja2Templates

app = FastAPI()
#templates = jinja2Templates(directory="/code")
templates = jinja2Templates(directory="C:/Users/ELCOTm/Downloads/k8_project")

@app.get("/")
def form_post(request: Request):
    return templates.TemplateResponse('form.html', context={'request': request})




