from pydantic import BaseModel

# Définition de la classe ProduitBase qui est utilisée pour la validation des données d'entrée/sortie
class ProduitBase(BaseModel):
    id: str | None = None
    nom: str
    description: str | None = None
    prix: float
    quantite_en_stock: int