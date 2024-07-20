from flask import Blueprint
from controllers.produto_controller import ProdutoController


#CRIANDO ROTAS DE PRODUTOS
produto_bp = Blueprint('produto_bp', __name__)
produto_bp.add_url_rule('/produtos', view_func=ProdutoController.as_view('produto_create'), methods=['POST'])
produto_bp.add_url_rule('/api/allprodutos',view_func=ProdutoController.as_view('produto_list'), methods=["GET"])