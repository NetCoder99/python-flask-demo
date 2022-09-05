from flask         import Flask
from config        import Config
from flask_migrate import Migrate

from app_init import db, login, appRoutes
from app      import routes

app = Flask(__name__, template_folder='app/templates')
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)
login.login_view = 'login'

appRoutes.init_app(app)

#app.add_url_rule('/',        view_func=routes.index)
#app.add_url_rule('/index/',  view_func=routes.index)
#app.add_url_rule('/hello/',            view_func=login_required(routes.hello))
#app.add_url_rule('/hello/<userName>',  view_func=login_required(routes.helloName))
#app.add_url_rule('/hello/',            view_func=routes.hello)
#app.add_url_rule('/hello/<userName>',  view_func=routes.helloName)

app.add_url_rule('/login/',  view_func=routes.login,  methods=['GET', 'POST'])
app.add_url_rule('/logout/', view_func=routes.logout, methods=['GET', 'POST'])

from models import User, BeerDetails, Post