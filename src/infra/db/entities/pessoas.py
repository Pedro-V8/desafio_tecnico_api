"""

Arquivo contendo a entidade modelo representando a tabela no banco de dados.

"""

from sqlalchemy import Column, String, Integer, DateTime, inspect

from src.infra.db.settings.base import Base


class Pessoas(Base):
    __tablename__ = "pessoas"

    # Atributos
    id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    rg = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    data_nascimento = Column(DateTime(timezone=True))
    data_admissao = Column(DateTime(timezone=True))
    funcao = Column(String, nullable=False)

    # Representação da Entidade
    def __repr__(self):
        return f"Pessoa [id={self.id_pessoa}, nome={self.nome}]"

    # Retorna o objeto em forma de Dicionário para o Json
    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
