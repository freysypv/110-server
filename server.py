from flask import Flask

app= Flask(__name__) # instance of Flask

# get http://127.0.0.1:5000/home
@app.route("/home", methods=["GET"])
def home():
    return {"message":"Welcome to flask cohort#65"}


@app.route("/cohort-65", methods=["GET"])
def get_students_65():
    students_list = ["sergio", "leonar", "Charles", "Ay,on", "Dejanirra", "Freysy", "Trishon"]
    return students_list

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

@app.route("/api/products", methods=["GET"])
def get_products():
    return {"data": products}


#---Coupons ___
coupons = [
  {"_id": 1, "code": "WELCOME10", "discount": 10},
  {"_id": 2, "code": "SPOOKY25", "discount": 25},
  {"_id": 3, "code": "VIP50", "discount": 50}
]


# get /api/coupons
@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return{
        "data": coupons
    }

#/api/coupons count
@app.route("/api/coupons/count", methods=['GET'] )
def coupons_count():
    return {"count": len(coupons)}

if __name__ == "__main__":
    app.run()
#when this file is run directluy:__name__ == "__maim__"
#when this file is imported as module: __name__ == "server.py"


