from app_init import db, login

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# -------------------------------------------------------------------------------------------
class User(UserMixin, db.Model):
    id        = db.Column(db.Integer,     primary_key=True)
    username  = db.Column(db.String(64),  index=True, unique=True)
    email     = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_username(self, username):
        self.username = username
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def set_email(self, email):
        self.email = email
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# -------------------------------------------------------------------------------------------
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


# -------------------------------------------------------------------------------------------
class BeerDetails(db.Model):
  rec_id    = db.Column(db.Integer,       primary_key=True)
  name      = db.Column(db.String(128),   index=True, unique=True)

  def __init__(self, id:int, name: str, tagline:str, first_brewed:str, description:str, image_url:str):
    self.id        = id 
    self.name      = name
    self.tagline   = tagline
    self.first_brewed = first_brewed
    self.description  = description
    self.image_url    = image_url

  def __repr__(self):
      return '<Name {}>'.format(self.name)