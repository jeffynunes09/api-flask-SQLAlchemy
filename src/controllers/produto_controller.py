from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.produto import Produto
from db import db

class ProdutoController(MethodView):

    @jwt_required()
    
    def get(self):
        try:
            produtos = Produto.query.all()
            return jsonify([produto.to_dict() for produto in produtos]), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @jwt_required()
   
    def post(self):
        current_user_id = get_jwt_identity()
        data = request.get_json()
        name = data.get('name')
        stock = data.get('stock')
        value = data.get('value')
        id_category = data.get('id_category')

        if not name or not stock or not value or not id_category:
            return jsonify({"error": "Missing required fields"}), 400

        new_produto = Produto(name=name, stock=stock, value=value, id_category=id_category, id_user=current_user_id)

        try:
            db.session.add(new_produto)
            db.session.commit()
            return jsonify(new_produto.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500
