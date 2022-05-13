from datetime import datetime
from shop import db, app


class Brand(db.Model):
    __tablename__ = 'brand'
    id = db.Column(db.Integer, primary_key=True) #unique brand
    name = db.Column(db.String(60), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id')) #unique owner
    user = db.relationship("User", back_populates="brand")
    products = db.relationship("Product", back_populates="brand")

    def __repr__(self):
        return '<Brand %r>' % self.name

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    products = db.relationship("Product", back_populates="category")
    def __repr__(self):
        return '<Category %r>' % self.name

class Product(db.Model):
    __tablename__="product"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(130), unique=False, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    price = db.Column(db.Numeric(10,2), nullable= False)
    stock = db.Column(db.Integer)
    img_1 = db.Column(db.String(150), nullable=False, default='image.jpg')
    img_2 = db.Column(db.String(150), nullable=False, default='image.jpg')
    img_3 = db.Column(db.String(150), nullable=False, default='image.jpg')
    desc =  db.Column(db.Text, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default= datetime.utcnow())
    last_modified = db.Column(db.DateTime, nullable=False)
    visibility = db.Column(db.Boolean, default = False, nullable = False)
    brand = db.relationship("Brand", back_populates="products") 
    category = db.relationship("Category", back_populates="products")

    def __repr__(self):
        return '<Product %r>' % self.title
