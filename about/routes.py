from flask import Blueprint, render_template

about_bp = Blueprint(
    'about_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@about_bp.route('/about')   # Focus here
def about_home():
    return render_template('about.html', title='About')
