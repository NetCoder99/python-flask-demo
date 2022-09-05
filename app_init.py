from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_login import LoginManager
login = LoginManager()

from app.routes  import AppRoutes
appRoutes = AppRoutes()