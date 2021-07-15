from flask import Flask, jsonify, make_response
from flask_login import LoginManager, login_manager
from flask_cors import CORS
from login_view import login
from login_control.user_control import User

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secret_key = 'login_server2'

app.register_blueprint(login.my_login, url_prefix='/myhome')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8081')
    