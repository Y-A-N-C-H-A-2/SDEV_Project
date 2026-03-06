"""
CrossPaths Application Entry Point
Run this file to start the Flask development server
"""
from app import create_app
import os

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    # Get configuration from environment or use defaults
    host = os.environ.get('FLASK_HOST', '127.0.0.1')
    port = int(os.environ.get('FLASK_PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    print("=" * 60)
    print("CrossPaths - Culturally Adaptive Speed-Friending Platform")
    print("=" * 60)
    print(f"Running on: http://{host}:{port}")
    print(f"Environment: {'Development' if debug else 'Production'}")
    print(f"Supported locales: en_IE, uk_UA, pt_BR")
    print("=" * 60)
    print("\nPress Ctrl+C to stop the server\n")
    
    # Run the application
    app.run(host=host, port=port, debug=debug)
