"""
This file will contain information of how to do register using blueprint of 
  API endpoints, how to handle request parameters,and how to send responses back to the client.

This is required so that ui/ux designer can understand that what this item api takes and reurns to the user, 
instead of reading all the code for item api


I commented some condition so that we can use schemas which reduces the code complexity.

Author: Deependra Shukla
Date: 7-27-2024

"""



from flask import request
import uuid
from db.itemdb import ItemDatabase
from flask.views import MethodView # Helps when Get api will be called it will provoke get function and so on.
from flask_smorest import Blueprint, abort 
from schemas import ItemGetSchema, ItemSchema, SuccessMessageSchema, ItemQuerySchema, ItemOptionalQuerySchema
from flask_jwt_extended import jwt_required # Put Constraint that the user has token by asking token to them and match with ours.

blp = Blueprint("myItems", __name__, description = "operation on items")


@blp.route("/item")
class Item(MethodView):

    def __init__(self):
        self.db = ItemDatabase()
    @jwt_required()
    @blp.arguments(ItemOptionalQuerySchema, location = "query") # location is used to specify that schema to look at query for data not on body data
    @blp.response(200, ItemGetSchema(many = True)) # many allows to have multiple insstances of that class.
    def get(self, args):
        id = args.get("id")
        # id = request.args.get('id')
        if id is None:
            return self.db.get_items()
        else:
            result = self.db.get_item(id) 
            if result == None:
                abort(404, message = "Item not found")
            return result
        # return {"message" : "Item not found"}, 404   # abort is better than return becz swagger bydefault show error messages in a particular order

    @jwt_required()
    @blp.arguments(ItemSchema)
    @blp.response(200, SuccessMessageSchema)
    def post(self, request_data):
        # request_data = request.get_json() # data will be returned in 2nd pararmeter by decorator so now we don't need it 
        # if "name" and "price" not in request_data:  # data validation done by decorator
        #     return {"message" : "name and price are required"}, 400  # 400 Bad Request status code
        id = uuid.uuid4().hex
        self.db.add_item(id, request_data)
        return {"message" : "items added successfully"}, 201

    @jwt_required()
    @blp.arguments(ItemQuerySchema, location = "query")
    @blp.response(200, SuccessMessageSchema)
    def delete(self, args):
        id = args.get("id")
        # id = request.args.get('id') # arg.. decorator will give id to pararmeter and variables (name, pos:2 or 3) can be anything
        ##  for item in items:
        # #     if item["id"] == id:
        # #         items.remove(item)
        if self.db.delete_item(id):
            return {"message" : "Item deleted successfully"}
        abort(404, message = "Item not found")
        # return {"message" : "Item not found"}, 404  # abort over return becz swagger bydefault show error messages in a particular order
    @jwt_required()
    @blp.response(200, SuccessMessageSchema)
    @blp.arguments(ItemSchema)
    @blp.arguments(ItemQuerySchema, location = "query")
    def put(self, request_data, args):
        id = args.get('id')
        # id = request.args.get('id')
        ## for item in items:
        #     # if item["id"] ==  id:
        #     #     item["item"] = request_data
            # request_data = request.get_json() # decorators output in 2nd parameter
            # if "name" and "price" not in request_data: # data validation 
            #     return {"message" : "name and price are required"}, 400  # 400 Bad Request status code
        if self.db.update_item(id, request_data):
            return {"message" : "items updated successfully"}, 201
        abort(404, message = 'item not found')
        # return {'message' : 'item not found'}, 404
