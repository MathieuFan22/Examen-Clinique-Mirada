from fastapi import FastAPI
from app.api.endpoints import autocomplete, correction, bigram
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API Backend",
    version="1.0.0",
    docs_url="/docs",
    root_path=settings.ROOT_PATH    # Chemin de base pour l'API
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Vérifiez bien l'orthographe ici
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#app.include_router(autocomplete.router, tags=["Text processing"])
app.include_router(autocomplete.router, prefix="/autocomplete", tags=["Autocomplétion"])
app.include_router(correction.router, prefix="/correction", tags=["correcteur_orthographique"])
app.include_router(bigram.router, prefix="/bigram", tags=["Bigram"])

@app.get("/")
def root():
    return {"message": "API Gestion Tickets fonctionne !"}