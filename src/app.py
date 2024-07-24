
#IMPORTES NECESSARIOS
from flask import Flask
from db import db
from dotenv import load_dotenv
import os
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

load_dotenv()

app = Flask(__name__)

# Configurações do banco de dados usando PyMySQL como driver
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

#INSTANCIANDO LIBS
db.init_app(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


#FUNCTION PARA INICIAR ROTAS ANTES DE CHAMA-LAS
def create_app():
    from routes.usuario_routes import auth_bp
    from routes.usuario_routes import usuario_bp
    from routes.produto_routes import produto_bp
    from routes.categoria_routes import categoria_bp
   

    # Registrando os blueprints
   
    app.register_blueprint(usuario_bp, url_prefix='/usuarios')
    app.register_blueprint(categoria_bp, url_prefix='/categorias')
    app.register_blueprint(auth_bp,url_prefix='/')

    
    app.register_blueprint(produto_bp, url_prefix='/')

    # Rota de teste
    @app.route('/api')
    def home():
        return "Hello, Flask with MySQL!"

    return app


#CONFIG PARA RODAR SERVER
if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)
