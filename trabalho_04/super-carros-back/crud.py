from datetime import date
from sqlalchemy.orm import Session
from exceptions import VeiculoAlreadyExistError, VeiculoNotFoundError, VeiculoNotFoundError, VendaNotFoundError, VendedorNotFoundError, VendedorAlreadyExistError, GastoNotFoundError, CorNotFoundError
import models, schemas, bcrypt


def create_endereco(db: Session, endereco: schemas.EnderecoCreate):
    db_endereco = models.Endereco(**endereco.dict())
    db.add(db_endereco)
    db.commit()
    db.refresh(db_endereco)
    return db_endereco


# vendedor
def get_vendedor_by_id(db: Session, vendedor_id: int):
    db_vendedor = db.query(models.Vendedor).get(vendedor_id)
    if db_vendedor is None:
        raise VendedorNotFoundError
    return db_vendedor

def get_all_vendedores(db: Session, offset: int, limit: int):
    return db.query(models.Vendedor).offset(offset).limit(limit).all()

def get_vendedor_by_email(db: Session, vendedor_email: str):
    return db.query(models.Vendedor).filter(models.Vendedor.email == vendedor_email).first()

def create_vendedor(db: Session, vendedor: schemas.VendedorCreate):
    db_vendedor = get_vendedor_by_email(db, vendedor.email)
    vendedor.senha = bcrypt.hashpw(vendedor.senha.encode('utf8'), bcrypt.gensalt())
    if db_vendedor is not None:
        raise VendedorAlreadyExistError
    db_vendedor = models.Vendedor(**vendedor.dict())
    db.add(db_vendedor)
    db.commit()
    db.refresh(db_vendedor)
    return db_vendedor

def update_vendedor(db: Session, vendedor_id: int, vendedor: schemas.VendedorCreate):
    db_vendedor = get_vendedor_by_id(db, vendedor_id)
    db_vendedor.nome = vendedor.nome
    db_vendedor.email = vendedor.email
    db_vendedor.senha = vendedor.senha
    db_vendedor.comissao = vendedor.comissao
    db_vendedor.data_nascimento = vendedor.data_nascimento
    db_vendedor.data_admissao = vendedor.data_admissao
    db_vendedor.cpf = vendedor.cpf
    db_vendedor.status = vendedor.status
    db_vendedor.id_endereco = vendedor.id_endereco
    if vendedor.senha != "":
        # O parâmetro rounds do gensalt determina a complexidade. O padrão é 12.
        db_vendedor.senha = bcrypt.hashpw(vendedor.senha.encode('utf8'), bcrypt.gensalt())
    db.commit()
    db.refresh(db_vendedor)
    return db_vendedor

def delete_vendedor_by_id(db: Session, vendedor_id: int):
    db_vendedor = get_vendedor_by_id(db, vendedor_id)
    db.delete(db_vendedor)
    db.commit()
    return

# veiculo
def get_veiculo_by_id(db: Session, veiculo_id: int):
    db_veiculo = db.query(models.Veiculo).get(veiculo_id)
    if db_veiculo is None:
        raise VeiculoNotFoundError
    return db_veiculo

def get_all_veiculos(db: Session, offset: int, limit: int):
    return db.query(models.Veiculo).offset(offset).limit(limit).all()

def create_veiculo(db: Session, veiculo: schemas.VeiculoCreate):
    db_veiculo = models.Veiculo(**veiculo.dict())
    db.add(db_veiculo)
    db.commit()
    db.refresh(db_veiculo)
    return db_veiculo

#### TESTE PARA CRIAR VALOR JUNTO AO VEICULO ####
# def create_veiculo(db: Session, veiculo: schemas.VeiculoCreate, valor: schemas.ValorCreate):
#     db_valor = models.Valor(**valor.dict())
#     db_veiculo = models.Veiculo(**veiculo.dict())
#     db_veiculo.id_valor = valor.id
#     db.add(db_veiculo)
#     db.commit()
#     db.refresh(db_veiculo)
#     return db_veiculo

def create_valor(db: Session, valor : schemas.ValorCreate):
    db_valor = models.Valor(**valor.dict())
    db.add(db_valor)
    db.commit()
    db.refresh(db_valor)
    return db_valor

def update_veiculo(db: Session, veiculo_id: int, veiculo: schemas.VeiculoCreate):
    db_veiculo = get_veiculo_by_id(db, veiculo_id)

    db_veiculo.nome = veiculo.nome
    db_veiculo.status = veiculo.status

    db_veiculo.id_cor = veiculo.id_cor
    db_veiculo.id_valor = veiculo.id_valor

    db.commit()
    db.refresh(db_veiculo)
    return db_veiculo

def delete_veiculo_by_id(db: Session, veiculo_id: int):
    db_veiculo = get_veiculo_by_id(db, veiculo_id)
    db.delete(db_veiculo)
    db.commit()
    return

# venda
def create_venda(db: Session, venda: schemas.VendaCreate):
    db_venda = models.Venda(**venda.dict())
    db.add(db_venda)
    db.commit()
    db.refresh(db_venda)
    return db_venda

def get_venda_by_id(db: Session, venda_id: int):
    db_venda = db.query(models.Venda).get(venda_id)
    if db_venda is None:
        raise VendaNotFoundError
    return db_venda

def get_all_vendas(db: Session, offset: int, limit: int):
    return db.query(models.Venda).offset(offset).limit(limit).all()

def update_venda(db: Session, venda_id: int, venda: schemas.VendaUpdate):
    db_venda = get_venda_by_id(db, venda_id)
    db_venda.status = venda.status
    db_venda.valor_venda = venda.valor_venda

    db.commit()
    db.refresh(db_venda)
    return db_venda

def check_vendedor(db: Session, vendedor: schemas.VendedorLoginSchema):
    db_vendedor = db.query(models.Vendedor).filter(models.Vendedor.email == vendedor.email).first()
    if db_vendedor is None:
        return False
    return bcrypt.checkpw(vendedor.senha.encode('utf8'), db_vendedor.senha.encode('utf8'))


# gastos
def create_gasto(db: Session, gasto: schemas.GastoCreate):
    db_gasto = models.Gasto(**gasto.dict())
    db.add(db_gasto)
    db.commit()
    db.refresh(db_gasto)
    return db_gasto

def get_gasto_by_id(db: Session, gasto_id: int):
    db_gasto = db.query(models.Gasto).get(gasto_id)
    if db_gasto is None:
        raise GastoNotFoundError
    return db_gasto

def get_all_gastos(db: Session, offset: int, limit: int):
    return db.query(models.Gasto).offset(offset).limit(limit).all()

# cores
def create_cor(db: Session, cor: schemas.CorCreate):
    db_cor = models.Cor(**cor.dict())
    db.add(db_cor)
    db.commit()
    db.refresh(db_cor)
    return db_cor

def get_cor_by_id(db: Session, cor_id: int):
    db_cor = db.query(models.Cor).get(cor_id)
    if db_cor is None:
        raise CorNotFoundError
    return db_cor

def get_all_cores(db: Session, offset: int, limit: int):
    return db.query(models.Cor).offset(offset).limit(limit).all()






