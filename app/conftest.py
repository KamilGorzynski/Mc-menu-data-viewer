import pytest

from app.app import create_app


@pytest.fixture(scope='session')
def app():
    test_app, db = create_app()
    test_app.config['TESTING'] = True
    test_app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@db:5432/test_db"

    with test_app.app_context():
        db.init_app(test_app)
        db.create_all()

        yield test_app

        with test_app.app_context():
            db.session.remove()
            db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

