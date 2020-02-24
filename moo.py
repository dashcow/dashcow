import os

from app import create_app, db
from app.models import Cattle, GroupMeta

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Cattle=Cattle, GroupMeta=GroupMeta)


@app.cli.command('create-db')
def create_db():
    db.create_all()
