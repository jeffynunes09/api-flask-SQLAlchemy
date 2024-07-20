from flask import request, jsonify
from flask.views import MethodView
from models.categoria import Categoria
from db import db


#CONTROLLER DE CATEGORIAS
class CategoriaController(MethodView):
    
    #CRIAR NOVA CATEGORIA
    def post(self):
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        if not name or not description:
            return jsonify({"error": "Missing required fields"}), 400

        new_categoria = Categoria(name=name, description=description)

        try:
            db.session.add(new_categoria)
            db.session.commit()
            return jsonify(new_categoria.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500
