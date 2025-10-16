from flask import Flask, jsonify, request

API_KEY=('FLASK_API_KEY')
def ip_requeste(self, client):
    ip=request.headers.get('X-Forwarded-For', client)
    return str(ip)

# def require_key(func):
#    def wrapper():
       
def create_app():
    app=Flask(__name__)

    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app