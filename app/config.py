import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@db:5432/mc_menu_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
