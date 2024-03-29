
from datetime      import datetime
from flask         import render_template, request, flash, redirect, url_for, current_app
from app.forms     import LoginForm, RegistrationForm
from flask_login   import current_user, login_user, logout_user, login_required
from app.models    import User
from werkzeug.urls import url_parse
from app_init      import db

class AppRoutes(object):
  def init_app(self, app):

    # -------------------------------------------------------------------------------
    @app.route('/')
    @app.route('/index/')
    def index():
      return render_template('index.html', title='Home', secret=current_app.config['SECRET_KEY'])  

    # -------------------------------------------------------------------------------
    @app.route('/hello/')
    @login_required    
    def hello(userName=None):
      return helloName(userName)

    @app.route('/hello/<userName>')
    def helloName(userName=None):
      args = request.args
      return render_template('hello.html', title='Hello', date=datetime.now(), args=args)  

    # # -------------------------------------------------------------------------------
    # @app.route('/login/', methods=['GET', 'POST'])
    # def login():
    #     if current_user.is_authenticated:
    #         return redirect(url_for('index'))
    #
    #     form = LoginForm()
    #
    #     if form.validate_on_submit():
    #         user = User.query.filter_by(username=form.username.data).first()
    #         if user is None or not user.check_password(form.password.data):
    #             flash('Invalid username or password', 'error')
    #             return redirect(url_for('login'))
    #
    #         login_user(user, remember=form.remember_me.data)
    #         next_page = request.args.get('next')
    #         if not next_page or url_parse(next_page).netloc != '':
    #             next_page = url_for('index')
    #         return redirect(next_page)
    #
    #     return render_template('login.html', title='Sign In', form=form)
    #

    # # -------------------------------------------------------------------------------
    # @app.route('/logout/')
    # def logout():
    #     logout_user()
    #     return redirect(url_for('index'))


    # # -------------------------------------------------------------------------------
    # @app.route('/addUser/', methods=['GET', 'POST'])
    # def addUser():
    #     form = LoginForm()
    #
    #     if form.validate_on_submit():
    #         user = User()
    #         user.set_username(form.username.data)
    #         user.set_password(form.password.data)
    #         db.session.add(user)
    #         db.session.commit()
    #         flash('Congratulations, you are now a registered user!')
    #         return redirect(url_for('index'))
    #
    #     return render_template('login.html', title='Add User', form=form)

    # -------------------------------------------------------------------------------
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))
        return render_template('register.html', title='Register', form=form)

    # -------------------------------------------------------------------------------
    @app.route('/posts/', methods=['GET'])
    def posts():
        return render_template('posts.html', title='Posts', posts=[])
