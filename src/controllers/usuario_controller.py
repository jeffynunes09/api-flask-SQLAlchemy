# src/controllers/usuario_controller.py
from flask import request, jsonify
from flask.views import MethodView
from models.usuario import Usuario
from app import bcrypt,jwt
from db import db
from flask_jwt_extended import create_access_token


#CRIAÇÃO DE USUARIO
class UsuarioController(MethodView):
    def post(self):
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not name or not email or not password:
            return jsonify({"error": "Missing required fields"}), 400
        #CRYPTOGRAFIA DE SENHA
        hashed_password = bcrypt.generate_password_hash(password,10).decode('utf-8')
        #MANDANDO DADOS PARA O BANCO
        new_usuario = Usuario(name=name, email=email, password=hashed_password)
        db.session.add(new_usuario)
        db.session.commit()
        return jsonify(new_usuario.to_dict()), 201
    



class LoginController(MethodView):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({
                "error" : "Missing required fields"
            }), 400
        
        user = Usuario.query.filter_by(email=email).first()

        if not user or not bcrypt.check_password_hash(user.password, password):
            return jsonify({
                "error":"Invalid email or password!"
            }), 401
        
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200