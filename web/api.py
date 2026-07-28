from flask import Blueprint
from flask import jsonify
from flask import request

from web.controller import SimulationController

api = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)


@api.route("/health")
def health():

    return jsonify({
        "status": "ok"
    })


@api.route("/run", methods=["POST"])
def run():

    payload = request.get_json(silent=True) or {}

    secure = payload.get("secure", True)

    controller = SimulationController(
        secure_mode=secure
    )

    result = controller.execute()

    return jsonify(result)
