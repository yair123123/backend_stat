from flask import Flask
from flask_cors import CORS

from app.api.controllers.front_controller import front_blueprint

app = Flask(__name__)
CORS(app)
app.register_blueprint(front_blueprint,url_prefix="/")
if __name__ == '__main__':
    app.run(debug=False)