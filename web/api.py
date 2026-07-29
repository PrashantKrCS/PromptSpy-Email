from flask import Blueprint
from flask import jsonify
from flask import request

from web.controller import SimulationController

api = Blueprint("api", __name__)


@api.route("/api/health")
def health():

    return jsonify(
        {
            "status": "ok"
        }
    )


@api.route("/api/run", methods=["POST"])
def run():

    body = request.get_json(silent=True) or {}

    secure_mode = body.get(
        "secure_mode",
        True
    )

    controller = SimulationController(
        secure_mode=secure_mode
    )

    results = controller.execute()

    return jsonify(results)
