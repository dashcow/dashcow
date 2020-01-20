from flask import jsonify, request

from . import api


@api.route('/cattle')
def get_all_cattle():
    return jsonify([{'cattle_id': '0'}, {'cattle_id': '1'}])
