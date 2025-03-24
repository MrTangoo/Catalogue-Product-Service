from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Produit
from schemas import ProduitBase

router = APIRouter(prefix="/produits", tags=["Produits"])

@router.post("/", response_model=ProduitBase)
def creer_produit(produit: ProduitBase, db: Session = Depends(get_db)):
    db_produit = Produit(**produit.dict(exclude={"id"}))
    db.add(db_produit)
    db.commit()
    db.refresh(db_produit)
    return db_produit

@router.get("/", response_model=List[ProduitBase])
def lire_produits(db: Session = Depends(get_db)):
    return db.query(Produit).all()

@router.get("/{produit_id}", response_model=ProduitBase)
def lire_produit(produit_id: str, db: Session = Depends(get_db)):
    produit = db.query(Produit).filter(Produit.id == produit_id).first()
    if not produit:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return produit

@router.put("/{produit_id}", response_model=ProduitBase)
def mettre_a_jour_produit(produit_id: str, produit: ProduitBase, db: Session = Depends(get_db)):
    db_produit = db.query(Produit).filter(Produit.id == produit_id).first()
    if not db_produit:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    for key, value in produit.dict(exclude={"id"}).items():
        setattr(db_produit, key, value)
    db.commit()
    db.refresh(db_produit)
    return db_produit

@router.delete("/{produit_id}")
def supprimer_produit(produit_id: str, db: Session = Depends(get_db)):
    produit = db.query(Produit).filter(Produit.id == produit_id).first()
    if not produit:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    db.delete(produit)
    db.commit()
    return {"message": "Produit supprimé avec succès"}
