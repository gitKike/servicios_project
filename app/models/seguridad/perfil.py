from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

#from app.core.db import Base    #Definir si es mediante app.core.db o mediante from app.database.db import Base
from app.database.db import Base

class Perfil(Base):
    __tablename__ = "perfiles"

    id_perfil = Column(String(4), primary_key=True)
    nombre = Column(String(30), nullable=False)
    smart = Column(Boolean, nullable=False, default=False)

    # Relación inversa: un perfil tiene muchos usuarios
    usuarios = relationship("Usuario", back_populates="perfil")
