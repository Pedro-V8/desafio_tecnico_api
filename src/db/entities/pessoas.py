from sqlalchemy import Column, String, Integer, DateTime

from src.db.settings.base import Base

class Pessoas(Base):
    __tablename__ = "pessoas"

    id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    rg = Column(String, nullable=False)
    cpf = Column(String, nullable=False)  
    data_nascimento = Column(DateTime(timezone=True))
    data_admissao = Column(DateTime(timezone=True))  
    funcao = Column(String, nullable=False)

    def __repr__(self):
        return f"Pessoas [id={self.id_pessoa}, nome={self.nome}]"
    