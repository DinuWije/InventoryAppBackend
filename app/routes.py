import json
from flask import jsonify, request
from app.models import User, Product
from app import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/", methods=['GET'])
#@login_required
def home():
    #all_products =  Product.query.filter_by(user_id=current_user.id).all()
    all_products = Product.query.all()
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
@login_required
def add_item():
    req_data = request.get_json()

    name = req_data.get('name')
    event = req_data.get('event')
    location = req_data.get('location')
    quantity = req_data.get('quantity')
    price = req_data.get('price')
    picture = req_data.get('pic_location')
    user_id = current_user.id

    temp_product = Product(item_name=name, school_event=event, storage_location=location, quantity=quantity, price=price, pic_location=picture, user_id=user_id)

    db.session.add(temp_product)
    db.session.commit()
    #app.logger.info(temp_product.id)

    return jsonify({"status" : "success"}), 200

@app.route('/delete_item', methods=['DELETE'])
@login_required
def delete_item():
    id = request.args.get('id')
    if id != None:
        item_to_delete = Product.query.get(id)
        if item_to_delete.user_id==current_user.id:
            db.session.delete(item_to_delete)
            db.session.commit()
            return jsonify({"status": "item deleted"}), 200
    else: 
        return jsonify({"status" : "none deleted"})

@app.route('/edit_item', methods=['PUT'])
@login_required
def edit_item():
    req_data = request.get_json()
    id = req_data.get('id')
    if id != None:
        item_to_edit = Product.query.get(id)
        if item_to_edit!=None and item_to_edit.user_id==current_user.id:
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
    user = User.query.filter_by(username=username).first()
    status = "Error: that username is already taken"
    if user==None:
        user = User(username=username, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        status = "success"
    return status

@app.route('/login', methods=['POST'])
def login():
    req_data = request.get_json()
    username = req_data.get('username')
    password = req_data.get('password')

    status = "Error: incorrect username or password"
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user, remember=True)
        if current_user.is_authenticated:
            status = "success"

    return status

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({"status": "logged out"})


@app.route('/this_user')
def this_user():
    if current_user.is_authenticated:
        user = {
            "id" : current_user.id,
            "username" : current_user.username
        }
        return jsonify(user)
    return "No user logged in"

@app.route('/get_users')
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
