from flask import Flask
from api.routes.redflag import redflag
from api.routes.user import user_blueprint
from api.helpers.welcome import welcome_message
from flask_jwt_extended import JWTManager


app = Flask(__name__)

jwt = JWTManager(app)

app.register_blueprint(redflag)
app.register_blueprint(user_blueprint)

from api import errors

@app.route('/')
def index():
   return welcome_message
