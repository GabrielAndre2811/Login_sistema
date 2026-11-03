from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

db = SQLAlchemy(model_class=Base)

def init_db(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all


class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    telefone = db.Column(db.String(20), unique=False)
    senha = db.Column(db.String(100), nullable=True)


class Produto(db.Model):
    __tablename__ = 'produtos'
    id_p = db.Column(db.Integer, primary_key=True)
    nome_produto = db.Column(db.String(100), nullable=True)
    valor = db.Column(db.Integer, nullable=False)
    qtd_produto = db.Column(db.Integer)
    descricao_produto = db.Column(db.String(300), nullable=False)
