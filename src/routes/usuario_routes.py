from flask import Blueprint

from controllers.usuario_controller import UsuarioController



#CRIANDO ROTAS DE USUARIO

usuario_bp = Blueprint('usuario_bp',__name__)
usuario_bp.add_url_rule('/create' , view_func=UsuarioController.as_view('create_user'), methods=["POST"])