from flask import Blueprint, request, jsonify,Response

from app.api.processing.procces_request import execute_statistics_function

front_blueprint = Blueprint("front",__name__)

@front_blueprint.route("/",methods= ["POST"])
def make_query():
    try:
        req = request.get_json()
        html_content = execute_statistics_function(req.get("statistic"),req.get("filter"))
        return Response(html_content,content_type="text/html")
    except Exception as e:
        print(e)
        return jsonify({
            "message":str(e)
        }),500