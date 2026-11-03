from flask import Blueprint, flash, render_template, request, redirect, url_for, session
from services.user_service import (get_user, get_user_by_id, create_user, get_user_by_email, update_user, delete_user)
from .auth_decorator import login_required


user_bp = Blueprint('user', __name__, url_prefix='/user', template_folder='templates')


@user_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro_usuario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        senha = request.form.get('senha')

        try: 
            user = create_user(nome, email, telefone, senha)
            return redirect(url_for('user.servicos'))
        except ValueError as e:
            return str(e), 400
        
    return render_template('cadastro.html')

@user_bp.route("/dados", methods=["GET"])
@login_required
def meus_dados():
    
    user_id = session.get("user_id")
    user = get_user_by_id(user_id)

    return render_template("dados.html", user=user)


@user_bp.route('/edit_user/<int: user_id>', methods=['GET', 'POST'])
@login_required
def editar_usuario(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return flash("Usuário não encontrado.", "alert-danger")

    if request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']

        try:
            update_user(user_id, nome, email, telefone)
            flash("Usuário atualizado com sucesso. ", "alert-success")
            return redirect(url_for("user.meus_dados"))
                  
            
        except ValueError as e:
           return str(e)

    return render_template("edit_user.html", usuario=user)



@user_bp.route("/servicos")
def servicos():
    return render_template("servicos.html")