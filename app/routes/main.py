"""
Main routes for the application
"""
from flask import Blueprint, render_template

# Create blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Render the main page of the application"""
    return render_template('home.html')