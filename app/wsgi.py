from app.app import create_app
from flask_migrate import Migrate

application, db = create_app()


# placed here instead app.py to avoid: A 'SQLAlchemy' instance has already been registered on this Flask app
db.init_app(application)
Migrate(application, db)

if __name__ == "__main__":
    application.run(debug=True)
