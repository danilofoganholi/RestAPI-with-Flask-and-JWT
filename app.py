from flask import Flask, jsonify
from flask_restful import Resource, Api
from resources.hotel import Hoteis, Hotel
from resources.usuario import User, UserRegister, UserLogin,UserLogout
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['JWT_SECRET_KEY'] = '@codingISamanzing#'
app.config['JWT_BLACKLIST_ENABLED']=True

jwt = JWTManager(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blacklist_loader
def verifica_blacklist(token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    return jsonify({'message':'You have been logged out'}),401


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hotel/<string:hotelId>')
api.add_resource(User, '/usuarios/<int:userId>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=False)

#http://127.0.0.1:5000/hoteis