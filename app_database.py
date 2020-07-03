from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "postgres://admin:donotusethispassword@aws-us-east-1-portal.19.dblayer.com:15813/compose"

db = create_engine(db_string)  
base = declarative_base()

class Product(base):
    __tablename__ = 'products'

    item_name = Column(String, primary_key=True, default="N/A")
    school_event = Column(String, primary_key=True, default="N/A")
    storage_location = Column(String, primary_key=True, default="N/A")
    quantity = Column(Integer, primary_key=True, default=0)
    price = Column(Integer, primary_key=True, default=0)

Session = sessionmaker(db)