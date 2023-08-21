from flask import Flask
from src.main.routes.routes import routes_bp

from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.register_blueprint(routes_bp)
