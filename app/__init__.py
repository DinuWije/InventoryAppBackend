# import os
# import json
# from flask import Flask, jsonify, request
# from flask_bcrypt import Bcrypt
# from flask_sqlalchemy import SQLAlchemy
# from models import User, Product

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = 'sqlite:///{}'.format(os.path.join(project_dir, "productdatabase.db"))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)

from app import routes