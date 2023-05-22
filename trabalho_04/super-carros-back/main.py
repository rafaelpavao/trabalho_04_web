from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from exceptions import VeiculoException, VendaException, VendedorException, EnderecoException, GastoException, CorException
from database import get_db, engine
import crud, models, schemas
from fastapi import FastAPI, Depends, HTTPException, Body
from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer
import uvicorn

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# usuário
@app.get("/api/vendedores/{vendedor_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Vendedor)
def get_vendedor_by_id(vendedor_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_vendedor_by_id(db, vendedor_id)
    except VendedorException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/vendedores", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedVendedor)
def get_all_vendedores(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_vendedores = crud.get_all_vendedores(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_vendedores}
    return response

@app.post("/api/vendedores", dependencies=[Depends(JWTBearer())], response_model=schemas.Vendedor)
def create_vendedor(vendedor: schemas.VendedorCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_vendedor(db, vendedor)
    except VendedorException as cie:
        raise HTTPException(**cie.__dict__)

@app.put("/api/vendedores/{vendedor_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Vendedor)
def update_vendedor(vendedor_id: int, vendedor: schemas.VendedorCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_vendedor(db, vendedor_id, vendedor)
    except VendedorException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/api/vendedores/{vendedor_id}", dependencies=[Depends(JWTBearer())])
def delete_vendedor_by_id(vendedor_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_vendedor_by_id(db, vendedor_id)
    except VendedorException as cie:
        raise HTTPException(**cie.__dict__)

# veiculo    

@app.get("/api/veiculos/{veiculo_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Veiculo)
def get_veiculo_by_id(veiculo_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_veiculo_by_id(db, veiculo_id)
    except VeiculoException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/veiculos", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedVeiculo)
def get_all_veiculos(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_veiculos = crud.get_all_veiculos(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_veiculos}
    return response

@app.post("/api/veiculos", dependencies=[Depends(JWTBearer())], response_model=schemas.Veiculo)
def create_veiculo(veiculo: schemas.VeiculoCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_veiculo(db, veiculo)
    except VeiculoException as cie:
        raise HTTPException(**cie.__dict__)
    
#### TESTE PARA CRIAR VALOR JUNTO AO VEICULO ####
# @app.post("/api/veiculos", dependencies=[Depends(JWTBearer())], response_model=schemas.Veiculo)
# def create_veiculo(veiculo: schemas.VeiculoCreate, valor: schemas.ValorCreate, db: Session = Depends(get_db)):
#     try:
#         return crud.create_veiculo(db, veiculo, valor)
#     except VeiculoException as cie:
#         raise HTTPException(**cie.__dict__)

@app.put("/api/veiculos/{veiculo_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Veiculo)
def update_veiculo(veiculo_id: int, veiculo: schemas.VeiculoCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_veiculo(db, veiculo_id, veiculo)
    except VeiculoException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/api/veiculos/{veiculo_id}", dependencies=[Depends(JWTBearer())])
def delete_veiculo_by_id(veiculo_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_veiculo_by_id(db, veiculo_id)
    except VeiculoException as cie:
        raise HTTPException(**cie.__dict__)
    
# venda
@app.post("/api/vendas", dependencies=[Depends(JWTBearer())], response_model=schemas.Venda)
def create_venda(venda: schemas.VendaCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_venda(db, venda)
    except VendaException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/vendas/{venda_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Venda)
def get_venda_by_id(venda_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_venda_by_id(db, venda_id)
    except VendaException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/vendas", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedVenda)
def get_all_vendas(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_vendas = crud.get_all_vendas(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_vendas}
    return response

@app.put("/api/vendas/{venda_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Venda)
def update_venda(venda_id: int, venda: schemas.VendaUpdate, db: Session = Depends(get_db)):
    return crud.update_venda(db, venda_id, venda)

# login
@app.post("/api/signup", tags=["vendedor"])
async def create_vendedor_signup(vendedor: schemas.VendedorCreate = Body(...), db: Session = Depends(get_db)):
    try:
        crud.create_vendedor(db, vendedor)
        return signJWT(vendedor.email)
    except VendedorException as cie:
        raise HTTPException(**cie.__dict__)

# login
@app.post("/api/login", tags=["vendedor"])
async def user_login(vendedor: schemas.VendedorLoginSchema = Body(...), db: Session = Depends(get_db)):
    if crud.check_vendedor(db, vendedor):
        return signJWT(vendedor.email)
    return {
        "error": "E-mail ou senha incorretos!"
    }

@app.post("/api/enderecos", dependencies=[Depends(JWTBearer())], response_model=schemas.Endereco)
def create_endereco(endereco: schemas.EnderecoCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_endereco(db, endereco)
    except EnderecoException as cie:
        raise HTTPException(**cie.__dict__)
    

# gastos
@app.post("/api/gastos", dependencies=[Depends(JWTBearer())], response_model=schemas.Gasto)
def create_gasto(gasto: schemas.GastoCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_gasto(db, gasto)
    except GastoException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/gastos/{gasto_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Gasto)
def get_gasto_by_id(gasto_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_gasto_by_id(db, gasto_id)
    except GastoException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/gastos", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedGasto)
def get_all_gastos(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_gastos = crud.get_all_gastos(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_gastos}
    return response

# cores
@app.post("/api/cores", dependencies=[Depends(JWTBearer())], response_model=schemas.Cor)
def create_cor(cor: schemas.CorCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_cor(db, cor)
    except CorException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/cores/{cor_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Cor)
def get_cor_by_id(cor_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_cor_by_id(db, cor_id)
    except CorException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/cores", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedCor)
def get_all_cores(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_cores = crud.get_all_cores(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_cores}
    return response