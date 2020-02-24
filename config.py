import os
from pathlib import Path
basedir = Path(__file__).parent


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        'sqlite:///' + str(basedir.joinpath('db-dev.sqlite'))

    @classmethod
    def init_app(cls, app):
        pass


config = {'development': DevelopmentConfig, 'default': DevelopmentConfig}
