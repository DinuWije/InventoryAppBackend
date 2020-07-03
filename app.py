import os
import json
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = 'sqlite:///{}'.format(os.path.join(project_dir, "productdatabase.db"))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)

current_id = 10

class Product(db.Model):
    __tablename__ = 'products'

    id = Column('id', Integer, primary_key=True)
    item_name = Column('name', String, nullable=False, default="N/A")
    school_event = Column('event', String, nullable=False, default="N/A")
    storage_location = Column('location', String, nullable=False, default="N/A")
    quantity = Column('quantity', Integer, nullable=False, default=0)
    price = Column('price', Integer, nullable=False, default=0)
    pic_location = Column('picture', String, nullable=True)

@app.route("/", methods=['GET'])
def home():
    
    price = request.args.get('price', 'All')
    event = request.args.get('event', 'All')
    all_products =  Product.query.all()

    name_array = []
    product_array = []

    for product in all_products:
        temp_dict = {
            "id" : product.id,
            "name" : product.item_name,
            "event" : product.school_event,
            "location" : product.storage_location,
            "quantity" : product.quantity,
            "price" : product.price,
            "picture" : product.pic_location
        }
        product_array.append(temp_dict)
        
    return jsonify(product_array)

@app.route('/add_item', methods=['POST'])
def add_item():
    req_data = request.get_json()

    name = req_data.get('name')
    event = req_data.get('event')
    location = req_data.get('location')
    quantity = req_data.get('quantity')
    price = req_data.get('price')
    picture = req_data.get('pic_location')

    temp_product = Product(item_name=name, school_event=event, storage_location=location, quantity=quantity, price=price, pic_location=picture)

    db.session.add(temp_product)
    db.session.commit()
    #app.logger.info(temp_product.id)

    return jsonify({"status" : "success"}), 200

@app.route('/delete_item', methods=['DELETE'])
def delete_item():
    id = request.args.get('id')
    if id != None:
        item_to_delete = Product.query.get(id)
        db.session.delete(item_to_delete)
        db.session.commit()
        return jsonify({"status": "item deleted"}), 200
    else: 
        return jsonify({"status" : "none deleted"})

@app.route('/edit_item', methods=['PUT'])
def edit_item():
    req_data = request.get_json()
    id = req_data.get('id')
    if id != None:
        item_to_edit = Product.query.get(id)
        if item_to_edit!=None:
            name = req_data.get('name')
            event = req_data.get('event')
            location = req_data.get('location')
            quantity = req_data.get('quantity')
            price = req_data.get('price')
            picture = req_data.get('picture')
            if name!=None: item_to_edit.item_name = name
            if event!=None: item_to_edit.school_event = event
            if location!=None: item_to_edit.storage_location = location
            if quantity!=None: item_to_edit.quantity = quantity
            if price!=None: item_to_edit.price = price
            if picture!=None: item_to_edit.pic_location = picture
            db.session.commit()
            return jsonify({"status": "item edited"}), 200
        else: return jsonify({"status": "item by that ID DNE"}), 200
    else: return jsonify({"status": "nothing changed"}), 200


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
