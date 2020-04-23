from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    full_name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean())
    posts = db.relationship("Post", backref='account', lazy=True)

    def __init__(self, full_name, username, password, role, admin):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.role = role
        self.admin = admin

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return [self.role]
