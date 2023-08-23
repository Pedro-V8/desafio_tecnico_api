"""

Arquivo contendo as definições das ações que ocorrem direto no bando de dados.

"""
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.pessoas import Pessoas as PessoasEntity
from src.domain.execptions import ExceptionAPI


class PessoaRepository:
    @classmethod
    def select_pessoas(cls):
        try:
            # Select
            with DBConnectionHandler() as db_connection:
                query = db_connection.session.query(PessoasEntity).all()
                db_connection.session.close()
                return query
        except Exception as error:
            raise error

    @classmethod
    def create_pessoa(cls, request):
        try:
            # Validando CPF e RG
            cpf = request.get("cpf")
            rg = request.get("rg")

            if not ExceptionAPI.validate_cpf(cpf):
                raise ValueError("CPF inválido")

            if not ExceptionAPI.validate_rg(rg):
                raise ValueError("RG inválido")
            
            # Create
            with DBConnectionHandler() as db_connection:
                pessoa = PessoasEntity(**request)
                db_connection.session.add(pessoa)
                db_connection.session.commit()
                db_connection.session.refresh(pessoa)
                db_connection.session.close()
                return pessoa
        except Exception as error:
            raise error

    @classmethod
    def update_pessoa(cls, id, request):
        try:
            # Update
            with DBConnectionHandler() as db_connection:
                db_connection.session.query(PessoasEntity).filter(
                    PessoasEntity.id_pessoa == id
                ).update(request)
                db_connection.session.commit()

                pessoa = (
                    db_connection.session.query(PessoasEntity)
                    .filter(PessoasEntity.id_pessoa == id)
                    .first()
                )
                db_connection.session.close()
                return pessoa
        except Exception as error:
            raise error

    @classmethod
    def delete_pessoa(cls, id):
        try:
            # Delete
            with DBConnectionHandler() as db_connection:
                db_connection.session.query(PessoasEntity).filter(
                    PessoasEntity.id_pessoa == id
                ).delete()
                db_connection.session.commit()
                db_connection.session.close()
                return "Pessoa deletada com sucesso!"
        except Exception as error:
            raise error
