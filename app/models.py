from sqlalchemy.sql import func

from .exceptions import ValidationError
from . import db


def any_empty(json, columns: list):
    is_empty = lambda x: x is None or x == ''
    return any([is_empty(json.get(c)) for c in columns])


class Cattle(db.Model):
    __tablename__ = 'cattle'
    id = db.Column(db.Integer, primary_key=True)
    back_id = db.Column(db.String(20))
    ear_id = db.Column(db.String(10))
    group = db.Column(db.Integer, db.ForeignKey('group_meta.id'))
    birthday = db.Column(db.DateTime, default=func.now())
    is_pregnant = db.Column(db.Boolean, default=False)
    modify_day = db.Column(db.DateTime, default=func.now())

    @staticmethod
    def from_json(json_cattle):
        validation_comlumns = ['back_id', 'ear_id']
        if any_empty(json_cattle, validation_comlumns):
            raise ValidationError(
                'comlumn: {} not nullable.'.format(validation_comlumns))
        return Cattle(back_id=json_cattle.get('back_id'),
                      ear_id=json_cattle.get('ear_id'),
                      group=json_cattle.get('group'),
                      birthday=json_cattle.get('birthday'),
                      is_pregnant=json_cattle.get('is_pregnant'))

    def to_json(self):
        json_cattle = {
            'id': self.id,
            'back_id': self.back_id,
            'ear_id': self.ear_id,
            'group': self.group,
            'birthday': self.birthday,
            'is_pregnant': self.is_pregnant,
            'modify_day': self.modify_day
        }
        return json_cattle

    def __repr__(self):
        return '<Cattle {}>'.format(self.back_id)


class GroupMeta(db.Model):
    __tablename__ = 'group_meta'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), default='newGroup')
    tag_color = db.Column(db.String(7), default='#000000')

    @staticmethod
    def from_json(json_cattle):
        pass

    def to_json():
        pass

    def __repr__(self):
        return '<Cattle Group {}>'.format(self.name)
