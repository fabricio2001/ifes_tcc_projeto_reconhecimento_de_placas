from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, DateTime, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

NOME_BANCO = "tcc"

engine = create_engine(f"sqlite:///./{NOME_BANCO}.sqlite", echo=True)
Base = declarative_base()

# Declaracao das classes


class Pessoa(Base):

    __tablename__ = "pessoa"

    id = Column(Integer, primary_key=True)
    cpf = Column(String, nullable=False)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    cargo = Column(String, nullable=False)
    
    def __repr__(self):
        return f"{self.nome}"
    
class Carro(Base):

    __tablename__ = "carro"

    id = Column(Integer, primary_key=True)
    placa = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    marca = Column(String, nullable=False)
    cor = Column(String, nullable=False)
    pessoa = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"{self.placa}"

class Registro(Base):

    __tablename__ = "registro"

    id = Column(Integer, primary_key=True)
    placa = Column(String, nullable=False)
    direcao = Column(Integer, nullable=False)
    data = Column(DateTime, nullable=False)
    tip = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"{self.placa}"
# fim da declaracao

class Cor(Base):

    __tablename__ = "cor"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    
    def __repr__(self):
        return f"{self.placa}"

class Marca(Base):

    __tablename__ = "marca"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    
    def __repr__(self):
        return f"{self.placa}"
    
class Modelo(Base):

    __tablename__ = "modelo"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    
    def __repr__(self):
        return f"{self.placa}"

class Cargo(Base):

    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    
    def __repr__(self):
        return f"{self.placa}"

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
