"""
Routes package initialization
"""
from flask import Flask
from flask_wtf.csrf import generate_csrf

def register_after_request(app: Flask):
    """Register after_request handlers for the application"""
    
    @app.after_request
    def add_csrf_token(response):
        """Add CSRF token to all responses if they are HTML"""
        if response.mimetype == 'text/html':
            csrf_token = generate_csrf()
            response.set_cookie('csrf_token', csrf_token)
        return response