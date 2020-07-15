from app import db, login_manager, config
from sqlalchemy import Column, String, Integer, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from flask_login import UserMixin
import pymysql

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(120), nullable=False, unique=True) 
    password = Column('password', String(60), nullable=False)
    #todo can set lazy=True
    products = relationship("Product", back_populates='user')

class Product(db.Model):
    __tablename__ = 'products'

    id = Column('id', Integer, primary_key=True)
    item_name = Column('name', String(300), nullable=False, default="N/A")
    school_event = Column('event', String(300), nullable=False, default="N/A")
    storage_location = Column('location', String(300), nullable=False, default="N/A")
    quantity = Column('quantity', Integer, nullable=False, default=0)
    price = Column('price', Integer, nullable=False, default=0)
    pic_location = Column('picture', String(500), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="products")

db.create_all()
db.session.commit()

def getDatabaseConnection(ipaddress, usr, passwd, charset, curtype):
    sqlCon  = pymysql.connect(host=ipaddress, user=usr, password=passwd, charset=charset, cursorclass=curtype);
    return sqlCon;

def createUser(cursor, userName, password, database,
               querynum=0, 
               updatenum=0, 
               connection_num=0):
    try:
        sqlCreateUser = "CREATE USER '%s'@'%%' IDENTIFIED BY '%s';" %(userName, password)
        cursor.execute(sqlCreateUser)
    except Exception as Ex:
        print("Error creating MySQL User: %s"%(Ex))
    
    try:
        grant_permissions = "GRANT ALL PRIVILEGES ON %s.* TO '%s'@'%%';"%(database, userName)
        cursor.execute(grant_permissions)
    except Exception as Ex:
        print("Error Granting Permissions: %s"%(Ex));
    
    try:
        flush_permissions = "FLUSH PRIVILEGES;"
        cursor.execute(flush_permissions)
    except Exception as Ex:
        print("Error flushing: %s"%(Ex))

ipaddress = "127.0.0.1"  # MySQL server is running on local machine
usr = "root"      
passwd = "db_pass"            
charset = "utf8mb4"    
curtype = pymysql.cursors.DictCursor
database = config.get('database')

mySQLConnection = getDatabaseConnection(ipaddress, usr, passwd, charset, curtype);
mySQLCursor = mySQLConnection.cursor()

createUser(mySQLCursor, "main_user_nine","password", database)