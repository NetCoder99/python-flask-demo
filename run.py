from flask         import Flask

from about.routes import about_bp
from auth.routes import auth_bp
from config        import Config
from flask_migrate import Migrate

from app_init      import db, login, appRoutes

#app = Flask(__name__, template_folder='app/templates', static_folder=os.path.join(os.getcwd(),'app','static'))
app = Flask(__name__, template_folder='app/templates')
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)
login.login_view = 'login'

appRoutes.init_app(app)

app.register_blueprint(about_bp)
app.register_blueprint(auth_bp)
