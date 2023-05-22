from datetime import date
from typing import List  
from pydantic import BaseModel

class VendedorBase(BaseModel):
    nome: str
    email: str
class VendedorCreate(VendedorBase):
    nome: str
    senha: str
    email: str
    comissao: int
    data_nascimento: date
    data_admissao: date
    cpf: str
    status: int
    id_endereco: int

    
class Vendedor(VendedorBase):
    id: int
    class Config:
        orm_mode = True
class PaginatedVendedor(BaseModel):
    limit: int
    offset: int
    data: List[Vendedor]

class VeiculoBase(BaseModel):
    nome: str
    status: int
    id_cor: int
    id_valor:int ## COMENTAR CASO VOLTE A CRIAR JUNTO AO VEICULO
    id_modelo : int

class VeiculoCreate(VeiculoBase):
    # gasto_ids: List[int] = []
    pass

class Veiculo(VeiculoBase):
    id: int
    class Config:
        orm_mode = True

class PaginatedVeiculo(BaseModel):
    limit: int
    offset: int
    data: List[Veiculo]


class EnderecoBase(BaseModel):
    cep: str
    rua: str
    numero: int
    complemento: str
    bairro: str
    id_cidade:int

class EnderecoCreate(EnderecoBase):

    pass

class Endereco(EnderecoBase):
    id: int
    class Config:
        orm_mode = True

class PaginatedEndereco(BaseModel):
    limit: int
    offset: int
    data: List[Endereco]

class VendaBase(BaseModel):
    valor_venda: float
    forma_pagamento:int
    id_veiculo:int

class VendaUpdate(BaseModel):
    valor_venda: int
    status : int

class VendaCreate(VendaBase):

    id_vendedor: int
    pass

class Venda(VendaBase):
    id: int
    veiculos: List[Veiculo] = []
    class Config:
        orm_mode = True

class PaginatedVenda(BaseModel):
    limit: int
    offset: int
    data: List[Venda]

class VendedorLoginSchema(BaseModel):
    email: str
    senha: str
    class Config:
        orm_mode = True

class GastoBase(BaseModel):
    valor_gasto : float
    descricao : str
    id_veiculo : int

class GastoCreate(GastoBase):
    pass

class Gasto(GastoBase):
    id: int
    class Config:
        orm_mode = True

class PaginatedGasto(BaseModel):
    limit: int
    offset: int
    data: List[Gasto]

class CorBase(BaseModel):
    nome : str

class CorCreate(CorBase):
    pass

class Cor(CorBase):
    id: int
    class Config:
        orm_mode = True

class PaginatedCor(BaseModel):
    limit: int
    offset: int
    data: List[Cor]

class ValorBase(BaseModel):
    valor_pago : float
    valor_fipe : float
    valor_venda : float

class ValorCreate(ValorBase):
    pass

class Valor(ValorBase):
    id: int
    class Config:
        orm_mode = True

