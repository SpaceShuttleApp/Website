import fastapi
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware


app = fastapi.FastAPI()
pages = Jinja2Templates(directory="static")
app.add_middleware(CORSMiddleware, allow_origins=["*"])
app.mount("/styles", StaticFiles(directory="styles"), name="styles")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")


@app.get("/")
async def home(request: fastapi.Request):
    return pages.TemplateResponse("home.html", {"request": request})


@app.get("/install", response_class=fastapi.responses.HTMLResponse)
def install(request: fastapi.Request):
    return fastapi.responses.HTMLResponse(
        """
        <meta http-equiv="refresh" content="0; url = https://alpha.deta.space/discovery/spaceshuttle-sbm-v0.1.0" />
        """
    )
