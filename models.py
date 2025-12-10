from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    categoria = Column(String)
    tamanho = Column(String)
    cor = Column(String)
    quantidade = Column(Integer)