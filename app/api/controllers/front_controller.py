from flask import Blueprint, request, jsonify

from app.api.processing.procces_request import execute_function_by_name

front_blueprint = Blueprint("front",__name__)

@front_blueprint.route("/",methods= ["POST"])
def make_query():
    req = request.get_json()
    res = execute_function_by_name(req.get("statistic"),req.get("filter"))
    return jsonify({
        "message":""
    })