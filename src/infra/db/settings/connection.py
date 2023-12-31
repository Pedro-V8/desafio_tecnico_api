"""

Arquivo contendo a Classe de Conexão com o Banco de Dados

"""

import os

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            os.getenv("ENGINE"),
            os.getenv("USER"),
            os.getenv("PASS"),
            os.getenv("HOST"),
            os.getenv("PORT"),
            os.getenv("DB"),
        )

        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()

        return self

    def __exit__(self, exec_type, exec_val, exec_tb):
        self.session.close()
