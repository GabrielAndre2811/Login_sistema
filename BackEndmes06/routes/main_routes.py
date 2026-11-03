from flask import Blueprint, render_template, request, redirect, url_for, session

main_bp = Blueprint('main', __name__, url_prefix='/', template_folder='templates')

@main_bp.route("/")
def home():
    return render_template("index.html")
    
@main_bp.route("/login")
def login():
    return render_template("login.html")

@main_bp.route("/contatos")
def contatos():
    return render_template("contatos.html")

@main_bp.route("/config")
def config():
    return render_template("config.html")
