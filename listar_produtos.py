from sqlalchemy.orm import sessionmaker
from models import Produto
from db import engine

Session = sessionmaker(bind=engine)
session = Session()

produtos = session.query(Produto).all()

print('Produtos cadastrados:')
for p in produtos:
    print(f"ID: {p.id}, Nome: {p.nome}, Categoria: {p.categoria}, "
          f"Tamanho: {p.tamanho}, Cor: {p.cor}, Quantidade: {p.quantidade}")
