class VeiculoException(Exception):
    ...

class VeiculoNotFoundError(VeiculoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "VEICULO_NAO_ENCONTRADO"

class VeiculoAlreadyExistError(VeiculoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "VEICULO_DUPLICADO"

class VendaException(Exception):
    ...

class VendaNotFoundError(VendaException):
    def __init__(self):
        self.status_code = 404
        self.detail = "VENDA_NAO_ENCONTRADA"



class VendedorException(Exception):
    ...

class VendedorNotFoundError(VendedorException):
    def __init__(self):
        self.status_code = 404
        self.detail = "VENDEDOR_NAO_ENCONTRADO"


class VendedorAlreadyExistError(VendedorException):
    def __init__(self):
        self.status_code = 409
        self.detail = "EMAIL_DUPLICADO"

class EnderecoException(Exception):
    ...

class EnderecoAlreadyExistError(EnderecoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "ENDEREÇO_DUPLICADO"

class GastoException(Exception):
    ...

class GastoNotFoundError(GastoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "GASTO_NAO_ENCONTRADA"

class CorException(Exception):
    ...

class CorNotFoundError(CorException):
    def __init__(self):
        self.status_code = 404
        self.detail = "COR_NAO_ENCONTRADA"
