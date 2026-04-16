from flask import Flask
from flask_cors import CORS
from routes.matrix_routes import matrix_bp


app=Flask(__name__)
CORS(app)

app.register_blueprint(matrix_bp,url_prefix="/api")
PORT=5000

if __name__=="__main__":
    print(f"servidor corriendo en el puerto:{PORT}")
    app.run(debug=True,port=PORT)


