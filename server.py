from flask import Flask, request, jsonify 
from flask_cors import CORS
import uuid

app= Flask(__name__) # instance of Flask
CORS(app, origins=["http://localhost:5173", "https.myapp.com"])
# get http://127.0.0.1:5000/home
@app.route("/home", methods=["GET"])
def home():
    return {"message":"Welcome to flask cohort#65"}


@app.route("/cohort-65", methods=["GET"])
def get_students_65():
    students_list = ["sergio", "leonar", "Charles", "Aymon", "Dejanirra", "Freysy", "Trishon"]
    return students_list
  
#------path parameters-------
@app.route("/greet/<string:name>", methods={"GET"})
def say_hi(name):
    return jsonify({"massage": f"Hello {name}"}), 200

@app.route('/api/users/<int:user_id>', methods=["GET"])
def get_user_by_id(user_id):
    return jsonify({"This is the user id": user_id}), 200 # ok


#  ------ Products
products = [
  {
    "_id": 1, 
    "title": "Nintendo Switch", 
    "price": 499.99, 
    "category": "Electronics", 
    "image": "https://picsum.photos/seed/1/300/300"
  },
  {
    "_id": 2, 
    "title": "Smart Refrigerator", 
    "price": 999.99, 
    "category": "Kitchen", 
    "image": "https://picsum.photos/seed/2/300/300"
  },
  {
    "_id": 3, 
    "title": "Bluetooth Speaker", 
    "price": 79.99, 
    "category": "Electronics", 
    "image": "https://picsum.photos/seed/3/300/300"
  },
]
#get http:/127.0.0.1:5000/api/products
@app.route("/api/products", methods=["GET"])
def get_products():
    return {"data": products}

#get http:/127.0.0.1:5000/api/products/2
@app.route('/api/products/<int:product_id>', methods=["GET"] )
def get_product_by_id(product_id):
    for product in products:  # for loop
        print(product["_id"]) #squal brackes acess the property
        if product["_id"] == product_id:
            return jsonify({
                "success": True,
                "message": "product retrieved successfully",
                "data":product
            }), 200# ok

        
    return jsonify ({
        "success": False,
        "messege": "product not found"
    }), 404 #Not Found

@app.route("/api/products", methods=["POST"])
def create_product():
    print(f"New product: {request.get_json()}")
    new_product = request.get_json()
    # new_product["_id"]=len(products) +1
    new_product["_id"] = uuid.uuid4()
    products.append(new_product)
    return jsonify({
        "success": True,
        "message": "product added successfully",
        "data": new_product
    }), 201 #created

    return "working on it"






# put
@app.route("/api/products/<int:product_id>", methods=["PUT"])
def update_product_by_id(product_id):
    updated_product = request.get_json()
    print(updated_product)
    for product in products:
        if product["_id"] == product_id:
            product["title"] = updated_product["title"]
            product["price"] = updated_product["price"]
            product["category"] = updated_product["category"]
            product["image"] = updated_product["image"]
            return jsonify({
                "success": True,
                "messege":"product updated successfully",
                "data": product
            }), 200
    
    return jsonify({
            "success": False,
            "message": "product not found"
        }), 404


#delete http://127.0.0.1:5000/api/products/2
#delete_product_by_id()
#return "working on it"
@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product_by_id(product_id):
    for product in products:
        if product["_id"] == product_id:
            products.remove(product)
            return jsonify({
                "success": True,
                "message": "product deleted successfully"
            }), 200 # ok
    
    return jsonify({
        "success": False,
        "message": "product not found"
    }), 404 # not found

#---Coupons-------
coupons = [
  {"_id": 1, "code": "WELCOME10", "discount": 10},
  {"_id": 2, "code": "SPOOKY25", "discount": 25},
  {"_id": 3, "code": "VIP50", "discount": 50}
]


# get /api/coupons
@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return({
        "coupons_list": coupons
    })

#/api/coupons count
@app.route("/api/coupons/count", methods=['GET'] )
def coupons_count():
    return ({"coupons_count": len(coupons)})

   #/api/coupons Add a coupon
@app.route("/api/coupons", methods=["post"])
def create_coupon():
    print(f"New product: {request.get_json()}")
    new_coupon = request.get_json()
    new_coupon["_id"] = uuid.uuid4()
    coupons.append(new_coupon)
    return jsonify({
        "success": True,
        "message":"coupon added successfully",
        "data": new_coupon
    }), 201 #created



# get/api/coupons/<int: id coupon_id
 # http://127.0.0.1:5000/api/coupons
@app.route('/api/coupons/<int:coupon_id>', methods=["GET"] )
#access the ID using square brackets
def get_coupon_by_id(coupon_id):
    for coupon in coupons:  # for loop
        print(coupon["_id"]) #squal brackes acess the property
        if coupon["_id"] == coupon_id:
            return jsonify({
                "success": True,
                "message": "coupon retrieved successfully",
                "data":coupon
            }), 200# ok
        
        return jsonify({
            "success": False,
            "message": "coupon not found"
        }), 404 #not found 


 


# put
@app.route("/api/coupons/<int:coupon_id>", methods=["PUT"])
def update_coupon_by_id(coupon_id):
    updated_coupon = request.get_json()
    print(updated_coupon)
    for coupon in coupons:
        if coupon["_id"] == coupon_id:
            coupon["code"] = updated_coupon["code"]
            coupon["discount"] = updated_coupon["discount"]
            return jsonify({
                "success": True,
                "message":"coupon updated successfully",
                "data": coupon
            }), 200
    
    return jsonify({
            "success": False,
            "message": "coupon not found"
        }), 404


        

  # http://127.0.0.1:5000/api/coupon/id      
@app.route("/api/coupons/<int:coupon_id>", methods=["DELETE"])
def delete_coupon_by_id(coupon_id):
        for coupon in coupons:
            if coupon["_id"] == coupon_id:
                coupons.remove(coupon)
                return jsonify({
                 "success": True,
                 "message": "coupon deleted successfully"
                }),200 # ok
        
        return jsonify({
            "success": False,
            "message": "coupon not found"
        }), 404 #not found        

if __name__ == "__main__":
    app.run(debug=True)
#when this file is run directluy:__name__ == "__maim__"
#when this file is imported as module: __name__ == "server.py"


