from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Produit
from schemas import ProduitBase

# Définition d'un routeur FastAPI pour gérer les routes relatives aux produits
router = APIRouter(prefix="/produits", tags=["Produits"])

# Route POST pour créer un nouveau produit
@router.post("/", response_model=ProduitBase, status_code=status.HTTP_201_CREATED)
def create_product(produit: ProduitBase, db: Session = Depends(get_db)):
    db_produit = Produit(**produit.dict(exclude={"id"}))
    db.add(db_produit)
    db.commit()
    db.refresh(db_produit)
    return db_produit

# Route GET pour récupérer tous les produits
@router.get("/", response_model=List[ProduitBase])
def get_products(db: Session = Depends(get_db)):
    return db.query(Produit).all()

# Route GET pour récupérer un produit spécifique par ID
@router.get("/{produit_id}", response_model=ProduitBase)
def get_product_by_id(produit_id: str, db: Session = Depends(get_db)):
    produit = db.query(Produit).filter(Produit.id == produit_id).first()
    if not produit:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return produit

# Route PUT pour mettre à jour un produit existant
@router.put("/{produit_id}", response_model=ProduitBase)
def update_product(produit_id: str, produit: ProduitBase, db: Session = Depends(get_db)):
    db_produit = db.query(Produit).filter(Produit.id == produit_id).first()
    if not db_produit:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    for key, value in produit.dict(exclude={"id"}).items():
        setattr(db_produit, key, value)
    db.commit()
    db.refresh(db_produit)
    return db_produit

# Route DELETE pour supprimer un produit
@router.delete("/{produit_id}")
def delete_product(produit_id: str, db: Session = Depends(get_db)):
    produit = db.query(Produit).filter(Produit.id == produit_id).first()
    if not produit:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    db.delete(produit)
    db.commit()
    return {"message": "Produit supprimé avec succès"}
