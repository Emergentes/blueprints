from flask import Flask
from blueprints.holamundo import holamundo_bp
from blueprints.calculadora import calculadora_bp

app = Flask(__name__)
app.register_blueprint(holamundo_bp)
app.register_blueprint(calculadora_bp,url_prefix="/calculadora")

if __name__ == "__main__":
    app.run(debug=True)