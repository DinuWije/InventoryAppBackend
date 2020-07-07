import json
from flask import jsonify, request
from flask_bcrypt import Bcrypt
from app.models import User, Product
from app import app, db

bcrypt = Bcrypt(app)

@app.route("/", methods=['GET'])
def home():
    
    # price = request.args.get('price', 'All')
    # event = request.args.get('event', 'All')

    all_products =  Product.query.all()

    product_array = []

    for product in all_products:
        temp_dict = {
            "id" : product.id,
            "name" : product.item_name,
            "event" : product.school_event,
            "location" : product.storage_location,
            "quantity" : product.quantity,
            "price" : product.price,
            "picture" : product.pic_location,
            "user_id" : product.user_id
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
    user_id = req_data.get('user_id')

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

@app.route('/register', methods=['POST'])
def register():
    req_data = request.get_json()
    username = req_data.get('username')
    password = req_data.get('password')
    hashed_pass = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(username=username, password=hashed_pass)
    db.session.add(user)
    db.session.commit()
    return jsonify({"status": "user created"}), 200

@app.route('/get_users', methods=['GET'])
def get_users():
    all_users =  User.query.all()
    user_array = []

    for user in all_users:
        temp_dict = {
            "user_id" : user.id,
            "username" : user.username,
            "password" : user.password
        }
        user_array.append(temp_dict)
        
    return jsonify(user_array)

@app.route('/get_user', methods=['GET'])
def get_user():
    req_data = request.get_json()
    username = req_data.get('username')
