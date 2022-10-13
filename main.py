from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
pages = Jinja2Templates(directory="static")
app.mount("/styles", StaticFiles(directory="styles"), name="styles")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return pages.TemplateResponse("home.html", {"request": request})


@app.get("/install", response_class=RedirectResponse)
async def install():
    return RedirectResponse("https://alpha.deta.space/discovery/spaceshuttle-sbm-v0.1.0")
