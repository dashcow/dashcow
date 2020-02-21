from sqlalchemy.sql import func

from . import db


class Cattle(db.Model):
    __tablename__ = 'cattle'
    cattle_id = db.Column(db.Integer, primary_key=True)
    back_id = db.Column(db.String(20))
    ear_id = db.Column(db.String(10))
    group = db.Column(db.Integer, db.ForeignKey('group_meta.group_id'))
    birthday = db.Column(db.DateTime, default=func.now())
    is_pregnant = db.Column(db.Boolean)
    modify_day = db.Column(db.DateTime, default=func.now())

    def __repr__(self):
        return '<Cattle %r>' % self.back_id


class CattleGroupMeta(db.Model):
    __tablename__ = 'group_meta'
    group_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), default='newGroup')
    tag_color = db.Column(db.String(7), default='#000000')
