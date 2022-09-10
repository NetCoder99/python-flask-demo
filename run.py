import os
from flask         import Flask
from config        import Config
from flask_migrate import Migrate

from app_init      import db, login, appRoutes

app = Flask(__name__, template_folder='app/templates', static_folder=os.path.join(os.getcwd(),'app','static'))
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)
login.login_view = 'login'

appRoutes.init_app(app)

from app.models import User, Post, BeerDetails