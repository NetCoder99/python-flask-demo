
from datetime    import datetime
from flask       import render_template, request, flash, redirect, url_for, current_app
from app.forms   import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from models      import User


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
      if userName:
        user = {'userName': userName}
      else:
        user = {'userName': None}
      return render_template('hello.html', title='Hello', user=user, date=datetime.now(), args=args)  






# -------------------------------------------------------------------------------
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)


# -------------------------------------------------------------------------------
def logout():
    logout_user()
    return redirect(url_for('index'))