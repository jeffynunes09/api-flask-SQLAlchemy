from flask import Flask
from db import db
from routes.produto_routes import produto_bp
from routes.categoria_routes import categoria_bp
from dotenv import load_dotenv
import os
load_dotenv()



app = Flask(__name__)

# Configurações do banco de dados usando PyMySQL como driver
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Registrando os blueprints
app.register_blueprint(produto_bp)
app.register_blueprint(categoria_bp)

# Rota de teste
@app.route('/')
def home():
    return "Hello, Flask with MySQL!"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
