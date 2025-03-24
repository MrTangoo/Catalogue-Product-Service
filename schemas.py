from pydantic import BaseModel, validator
from decimal import Decimal


class ProduitBase(BaseModel):
    id: str | None = None
    nom: str
    description: str | None = None
    prix: Decimal
    quantite_en_stock: int

    @validator('quantite_en_stock')
    def check_quantite_en_stock(cls, value):
        if value < 0:
            raise ValueError('La quantité en stock ne peut pas être inférieure à 0')
        return value
