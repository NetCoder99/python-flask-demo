from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@auth_bp.route('/login', methods=["GET", "POST"])   # Focus here
def auth_login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', title='Login', error=error)
