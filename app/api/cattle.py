from flask import jsonify, request

from . import api
from .. import db
from app.models import Cattle, GroupMeta
from app.exceptions import ValidationError


@api.route('/cattle', methods=['POST'])
def create_cattle():
    cattle = Cattle.from_json(request.json)
    db.session.add(cattle)
    db.session.commit()
    return jsonify(cattle.to_json()), 201


@api.route('/cattle')
def get_all_cattle():
    return jsonify([c.to_json() for c in Cattle.query.all()])


@api.route('/cattle/<int:id>/group', methods=['PUT'])
def update_cattle_group(id):
    group_id = request.json.get('group')
    if group_id is None or group_id == '':
        raise ValidationError('group column is empty.')
    GroupMeta.query.get_or_404(
        group_id, description='group id {} is not found.'.format(group_id))
    cattle = Cattle.query.get_or_404(
        id, description='cattle id {} is not found.'.format(id))
    cattle.group = group_id
    db.session.add(cattle)
    db.session.commit()
    return jsonify(cattle.to_json())
