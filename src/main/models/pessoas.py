class Pessoas:
    def __init__(
        self,
        id_pessoa: int,
        nome: str,
        rg: str,
        cpf: str,
        data_nascimento: str,
        data_admissao: str,
        funcao: str,
    ) -> None:
        self.id_pessoa = id_pessoa
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.data_admissao = data_admissao
        self.funcao = funcao
