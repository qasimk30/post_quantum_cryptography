from flask import Flask
from flask_talisman import Talisman
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    app = Flask(__name__)
    Talisman(app)
    from .routes import main
    app.register_blueprint(main)
    return app
