from sqlalchemy.orm import sessionmaker
from models import Produto
from db import engine
Session = sessionmaker(bind=engine)
session = Session()

novo_produto = Produto(
    nome = "Camiseta Básica",
    categoria = "Camiseta",
    tamanho = "M",
    cor = "Branca",
    quantidade = 10
)

session.add(novo_produto)
session.commit()
print("Produto inserido com sucesso!")