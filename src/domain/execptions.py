"""

Arquivo contendo as validações de CPF e RG

"""
import re


class ExceptionAPI:
    @staticmethod
    def validate_cpf(cpf):
        pattern = re.compile(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$")
        return pattern.match(cpf) is not None

    @staticmethod
    def validate_rg(rg):
        pattern = re.compile(r"^\d{1,2}\.\d{3}\.\d{3}(-\d{1}|)$")
        return pattern.match(rg) is not None
