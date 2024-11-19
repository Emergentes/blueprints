from flask import Blueprint, render_template, redirect

holamundo_bp = Blueprint("holamundo",__name__,template_folder="templates")

@holamundo_bp.route("/")
def index():
    return "Hola mundo desde Blueprint"

@holamundo_bp.route("/hola/<nombre>")
def hola_nombre(nombre):
    return "Hola "+nombre+", Bienvenido"

@holamundo_bp.route("/holahtml")
def hola_html():
    return render_template("hola.html")