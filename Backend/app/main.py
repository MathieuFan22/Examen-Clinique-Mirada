from fastapi import FastAPI
from app.api.endpoints import autocomplete, correction
from app.core.config import settings


app = FastAPI(
    title="API Backend",
    version="1.0.0",
    docs_url="/docs",
    root_path=settings.ROOT_PATH    # Chemin de base pour l'API
)

#app.include_router(autocomplete.router, tags=["Text processing"])
app.include_router(autocomplete.router, prefix="/autocomplete", tags=["Autocomplétion"])
app.include_router(correction.router, prefix="/correction", tags=["correcteur_orthographique"])

@app.get("/")
def root():
    return {"message": "API Gestion Tickets fonctionne !"}