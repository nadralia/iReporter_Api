from flask import Flask
from api.routes.redflag import redflag
from api.routes.user import user

app = Flask(__name__)

app.register_blueprint(redflag)
app.register_blueprint(user)

@app.route('/')
def index():
    pass
