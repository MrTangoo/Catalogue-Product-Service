from sqlalchemy import Column, String, Integer, DECIMAL, CheckConstraint
import uuid
from database import Base

# Définition de la classe Produit, qui hérite de la classe Base de SQLAlchemy
class Produit(Base):
    __tablename__ = "produits"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
    nom = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    prix = Column(DECIMAL(10, 2), nullable=False)
    quantite_en_stock = Column(Integer, nullable=False, default=0)

    __table_args__ = (
        CheckConstraint('quantite_en_stock >= 0', name='check_quantite_en_stock'),
    )