from flask import jsonify
from app.exceptions import ValidationError
from . import api


@api.errorhandler(ValidationError)
def validation_error(e):
    response = jsonify({'error': 'bad request', 'message': e.args[0]})
    response.status_code = 400
    return response


@api.app_errorhandler(404)
def page_not_found(e):
    response = jsonify({'error': e.name, 'message': e.description})
    response.status_code = 404
    return response
