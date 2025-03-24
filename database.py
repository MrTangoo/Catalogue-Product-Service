from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Connexion à une base de données SQLite stockée dans un fichier
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

# Création de l'engine SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Création du sessionmaker pour gérer les sessions de la base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe de base pour les modèles
class Base(DeclarativeBase):
    pass

# Fonction pour obtenir une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
