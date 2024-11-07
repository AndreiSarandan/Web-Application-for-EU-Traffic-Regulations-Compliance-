from flask import Flask, current_app, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from os import path
from flask_login import LoginManager
import sqlite3
from flask_migrate import Migrate

db = SQLAlchemy()
DB_NAME = 'users_databse.db'

from .views import views
migrate = Migrate()


# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'abc'
#     app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
#     db.init_app(app)
#     migrate = Migrate(app, db)

#     app.register_blueprint(views, url_prefix='/')
#     from .auth import auth
#     app.register_blueprint(auth, url_prefix='/')

#     with app.app_context():
#         db.create_all()

#     # Import here to avoid circular import
#     from .models import User, Car
#     login_manager = LoginManager()
#     login_manager.login_view = 'auth.login'  # Redirect to login page if user tries to access restricted tabs
#     login_manager.init_app(app)

#     @login_manager.user_loader
#     def load_user(id):
#         return User.query.get(int(id))

#     return app

def create_app(config_name='DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')
    
    db.init_app(app)
    migrate.init_app(app, db)

    from .views import views
    app.register_blueprint(views, url_prefix='/')
    
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')

    with app.app_context():
        db.create_all()

    from .models import User, Car
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')




if __name__ == "__main__":
    create_app().run(debug=True)
