"""
Application entry point
"""
import os
from app import create_app
from config import get_config

# Create application with configuration
app = create_app(get_config())

if __name__ == '__main__':
    # Get port from environment or use default
    port = int(os.environ.get('PORT', 5002))
    
    # Get debug mode from configuration
    debug_mode = app.config.get('DEBUG', False)
    
    # Print startup message
    print(f"Starting Post-Quantum Cryptography Demo on port {port}")
    print(f"Debug mode: {'Enabled' if debug_mode else 'Disabled'}")
    
    # Run the application
    app.run(host='0.0.0.0', port=port, debug=debug_mode)