from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import shutil

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/upload")
async def upload_image(request: Request, file: UploadFile = File(...)):
    with open("static/profile.jpg", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return templates.TemplateResponse(request=request, name="index.html")