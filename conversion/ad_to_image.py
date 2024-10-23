from flask import Blueprint

bp = Blueprint("ad_to_image", __name__)

@bp.route("/", method=['GET'])
def home():
    greetings = 'Hello, world!'
    if not greetings:
        abort(404, description="Greetings not found")
    return jsonify({"message": greetings})
