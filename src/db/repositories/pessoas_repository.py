from src.db.settings.connection import DBConnectionHandler
from src.db.entities.pessoas import Pessoas as PessoasEntity
from src.db.repositories.pessoas_validator import Validator


class PessoaRepository:
    @classmethod
    def select_pessoas(cls):
        try:
            with DBConnectionHandler() as db_connection:
                query = db_connection.session.query(PessoasEntity).all()
                db_connection.session.close()
                return query
        except Exception as error:
            raise error

    @classmethod
    def create_pessoa(cls, request):
        try:
            cpf = request.get("cpf")
            rg = request.get("rg")

            if not Validator.validar_cpf(cpf):
                raise ValueError("CPF inválido")

            if not Validator.validar_rg(rg):
                raise ValueError("RG inválido")
            
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
            with DBConnectionHandler() as db_connection:
                db_connection.session.query(PessoasEntity).filter(
                    PessoasEntity.id_pessoa == id
                ).delete()
                db_connection.session.commit()
                db_connection.session.close()
                return "Pessoa deletada com sucesso!"
        except Exception as error:
            raise error
