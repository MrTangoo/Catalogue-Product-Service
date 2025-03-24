from fastapi import FastAPI
from database import engine
from models import Base
from routers import produit

# Créer toutes les tables dans la base de données
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inclure les routes pour les produits
app.include_router(produit.router)
