from flask import Blueprint
from controllers.categoria_controller import CategoriaController

categoria_bp = Blueprint('categoria_bp', __name__)

categoria_bp.add_url_rule('/categorias', view_func=CategoriaController.as_view('categoria_create'), methods=['POST'])
