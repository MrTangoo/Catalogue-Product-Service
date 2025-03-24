from pydantic import BaseModel

class ProduitBase(BaseModel):
    id: str | None = None
    nom: str
    description: str | None = None
    prix: float
    quantite_en_stock: int