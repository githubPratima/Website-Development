from shop import db, app
import enum 
from flask_login import UserMixin
from flask_migrate import upgrade, migrate, init, stamp
from shop.products.models import Brand

class Roles(enum.Enum):
    generic_user = 'General User'
    site_manager = 'Site Manager'
    retail_user = 'Retail User'

class User(UserMixin,db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    role = db.Column(
        db.Enum(Roles, values_callable=lambda x: [str(member.value) for member in Roles]), 
        default=Roles.generic_user,
        nullable=False
    )
    brand = db.relationship("Brand",back_populates="user", uselist=False)
    def __repr__(self):
        return '<User %r>' % self.username




