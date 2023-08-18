from src.db.settings.connection import DBConnectionHandler
from src.db.entities.pessoas import Pessoas as PessoasEntity


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
    def update_pessoa(cls, id, request):
        try:
            

            with DBConnectionHandler() as db_connection:
                db_connection.session.query(PessoasEntity).filter(PessoasEntity.id_pessoa == id).update(request)
                db_connection.session.commit()

                pessoa = db_connection.session.query(PessoasEntity).filter(PessoasEntity.id_pessoa == id).first()
                db_connection.session.close()
                return pessoa
        except Exception as error:
            raise error