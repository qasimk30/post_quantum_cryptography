"""
Application factory for the Flask application
"""
from flask import Flask
from flask_wtf.csrf import CSRFProtect

# Initialize CSRF protection
csrf = CSRFProtect()

def create_app(config_object=None):
    """Create and configure the Flask application"""
    app = Flask(__name__)
    
    # Load configuration
    if config_object:
        app.config.from_object(config_object)
    
    # Initialize extensions
    csrf.init_app(app)
    
    # Register blueprints
    from app.routes.main import main_bp
    from app.routes.kyber import kyber_bp
    from app.routes.dilithium import dilithium_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(kyber_bp)
    app.register_blueprint(dilithium_bp)
    
    # Register after_request handlers
    from app.routes import register_after_request
    register_after_request(app)
    
    return app