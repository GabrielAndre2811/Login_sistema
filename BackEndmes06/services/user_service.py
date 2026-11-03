from flask import flash
from models.models import User, db

def get_user() -> list[User]:
    return db.session.query(User).limit(25).all()

def get_user_by_id(user_id: int) -> User:
    return db.session.query(User).filter_by(id=user_id).first()

def get_user_by_email(email: str) -> User:
    return db.session.query(User).filter_by(email=email).first()

def create_user(nome: str, email: str,
                telefone: str, senha: str) -> User:
    if not nome or not email or not telefone or not senha:
        raise ValueError("Todos os campos são obrigatórios.")

    existing_email_user  = User.query.filter_by(email=email).first()
    if existing_email_user:
        raise ValueError("Este email já está cadastrado!")

    user = User(nome=nome, email=email, telefone=telefone, senha=senha)
    db.session.add(user)
    db.session.commit()
    return user

def update_user(user_id: int, nome: str, email: str, telefone: str) -> User:
    user = get_user_by_id(user_id)
    if not user:
        raise ValueError("Usuario não encontrado ")

    if not nome or not email or not telefone:
        raise ValueError("Por favor, preencha todos os campos.")

    existing_email_user = User.query.filter_by(email=email).first()
    if existing_email_user and existing_email_user.id != user.id:
        raise ValueError("Este email já está cadastrado!")

    user.nome = nome
    user.email = email
    user.telefone = telefone
    db.session.commit()
    return user

def delete_user(user_id: int) -> None:
    user = get_user_by_id(user_id)
    if not user:
        raise ValueError("Usuario não encontrado")

    db.session.delete(user)
    db.session.commit()


def authenticate_user(email, senha):
    user = get_user_by_email(email)

    if not user:
        return None

    if user.senha != senha:
        flash("Senha incorreta. Tente novamente.", "error")
        return None

    flash("Login realizado com sucesso!", "success")
    return user