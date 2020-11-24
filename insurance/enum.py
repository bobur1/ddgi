from enum import Enum


class ContractType:
    LEASING = (1, 'Leasing')
    CONTRACT = (2, 'Loan')

    __list__ = [LEASING, CONTRACT]


class InputType:
    TEXT = (1, 'Text')
    NUMBER = (2, 'Number')
    SINGLE_SELECTION = (3, 'Single selection')
    MULTI_SELECTION = (4, 'Multi selection')
    CURRENCY = (5, 'Currency')
    DATE = (6, 'Date')

    __list__ = [TEXT, NUMBER, SINGLE_SELECTION, MULTI_SELECTION, CURRENCY]


class CurrencyType:
    SUM = (1, 'Sum')
    USD = (2, 'USD')

    __list__ = (SUM, USD)


class ClientType:
    INDIVIDUAL = (1, 'Физическое лицо')
    LEGAL_PERSON = (2, 'Юридик лицо')

    __list__ = [INDIVIDUAL, LEGAL_PERSON]

    @staticmethod
    def client_type_by(type_id):
        if type_id == 1 or '1':
            return True
        return False
