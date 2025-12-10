from sqlalchemy import create_engine
from models import Base, Produto 
engine = create_engine('sqlite:///estoque.db')

Base.metadata.create_all(engine)

print("Banco de dados e tabela 'produtos' criados com sucesso!")
