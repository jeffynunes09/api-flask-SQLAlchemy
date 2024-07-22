# src/controllers/usuario_controller.py
from flask import request, jsonify
from flask.views import MethodView
from models.usuario import Usuario
from app import bcrypt
from db import db
from flask_jwt_extended import JWTManager


class UsuarioController(MethodView):
    def post(self):
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not name or not email or not password:
            return jsonify({"error": "Missing required fields"}), 400

        hashed_password = bcrypt.generate_password_hash(password,10).decode('utf-8')

        new_usuario = Usuario(name=name, email=email, password=hashed_password)
        db.session.add(new_usuario)
        db.session.commit()
        return jsonify(new_usuario.to_dict()), 201