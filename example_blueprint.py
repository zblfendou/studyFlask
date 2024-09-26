from flask import Blueprint, Flask

# Create the blueprint and define its routes
bp = Blueprint('simple_page', __name__)

@bp.route('/')
def index():
    return 'Hello, world! study flask blueprint'

# Create the Flask app and register the blueprint
app = Flask(__name__)
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run()