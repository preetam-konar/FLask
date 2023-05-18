from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/store")
def get_store():
    return {"stores": stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if name==store["name"]:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "store not found"}, 404

@app.get("/store/<string:name>")
def get_store_by_name(name):
    for store in stores:
        if store["name"]==name:
            return store
    return {"message": "store not found"}, 404

@app.get("/store/<string:name>/item")
def get_store_items(name):
    for store in stores:
        if store["name"]==name:
            return {"items": store["items"]}
    return {"message": "store not found"}, 404