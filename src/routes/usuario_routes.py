from flask import Blueprint
from controllers.usuario_controller import *



#CRIANDO ROTAS DE USUARIO


auth_bp = Blueprint('auth_bp', __name__)
usuario_bp = Blueprint('usuario_bp',__name__)
usuario_bp.add_url_rule('/create' , view_func=UsuarioController.as_view('create_user'), methods=["POST"])
usuario_bp.add_url_rule("/login", view_func=LoginController.as_view('login_user'), methods=["POST"])