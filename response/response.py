import flask
from .messages import OK
from .status_codes import STATUS_OK


def generate_response(code: int, msg: str, data=None):
    if data is None:
        return flask.make_response(flask.jsonify({"msg": msg, "data": data}), code)
    else:
        return flask.make_response(flask.jsonify({"msg": msg}), code)


def generate_OK(data=None):
    return generate_response(STATUS_OK, OK, data)
