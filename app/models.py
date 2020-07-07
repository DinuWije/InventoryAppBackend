from app import db  
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(120), nullable=False, unique=True) 
    password = Column('password', String(60), nullable=False)
    #can set lazy=True
    products = relationship("Product", back_populates='user')

def load_user(username):
    return User.query.get(username)

class Product(db.Model):
    __tablename__ = 'products'

    id = Column('id', Integer, primary_key=True)
    item_name = Column('name', String, nullable=False, default="N/A")
    school_event = Column('event', String, nullable=False, default="N/A")
    storage_location = Column('location', String, nullable=False, default="N/A")
    quantity = Column('quantity', Integer, nullable=False, default=0)
    price = Column('price', Integer, nullable=False, default=0)
    pic_location = Column('picture', String, nullable=True)
    #!!remember to change nullable to false in the user_id
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    user = relationship("User", back_populates="products")
