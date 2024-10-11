from flask import Flask
from resources.item import blp as ItemBlp
from resources.user import blp as UserBlp
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from blocklist import BLOCKLIST


app = Flask(__name__)



#######################################
"""
    To registre all apis for the developers to test all the api blueprint we have created.
    To run it --> localhost:port/swagger-ui
"""


app.config["PROPAGATE_ERROR"] = True
app.config["API_TITLE"] = "Items Rest Api"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


app.config["JWT_SECRET_KEY"] = "103187861313941785993458505198815670702"
api = Api(app)
jwt = JWTManager(app)   

# Registering ItemBlp simmilarly we can register usersBlp also.
api.register_blueprint(ItemBlp)
api.register_blueprint(UserBlp)

# This function will envoked for those apis using jwt_required and if returned true then revoked_token_callback will be called. 
@jwt.token_in_blocklist_loader
def is_token_blocklisted(jwt_header, jwt_payload):
    return jwt_payload['jti'] in BLOCKLIST

@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return (
        {
            "description": "user has been logged out",
            "error": "token has been revoked"
        },
        401
    )

################################################










########################################################## code to run before creating blueprints #####################################



# from flask import Flask, request
# import uuid
# from db import items


# app = Flask(__name__)


# """
# http://127.0.0.1:5000/get-items
# host name/Domain name --> http://127.0.0.1:
# port number --> 5000
# by adding this route function get_items will called 

# here to make it rest api we need to make it common path for all requests so commented lines will also work.
# """
# # # @app.get('/get-items')
# # @app.get('/items')
# # def get_items():
# #     return {"items are" : items}


# """
# '/get-item/<string:name>' --> for passing 1 query parameter
# /get-item' and use request.args.get() --> multiple query parameters
# """


# # @app.get('/get-item')  # name is a dynamic data user will pass, data type is string
# @app.get('/item')
# def get_item():
#     id = request.args.get('id')
#     if id is None:
#         return {"items are" : items}
#     try:
#         return items[id]
#     except KeyError:
#         return {"message" : "Item not found"}, 404


# # @app.delete('/delete-item')  # name is a dynamic data user will pass, data type is string in url it will pass like http../..?name=".."
# @app.delete('/item')
# def delete_item():
#     id = request.args.get('id')
#     if id in items.keys():
#         del items[id]
#         return {"message" : "Item deleted successfully"}
#     return {"message" : "Item not found"}, 404


# # @app.post('/add-items')
# @app.post('/item')
# def add_item():
#     request_data = request.get_json()
#     if "name" and "price" not in request_data:
#         return {"message" : "name and price are required"}, 400  # 400 Bad Request status code
#     items[uuid.uuid4().hex] = request_data # gets json data but returns dic
#     return {"message" : "items added successfully"}, 201


# # @app.put('/update-item')
# @app.put('/item')
# def update_item():
#     id = request.args.get('id')
#     if id in items.keys():
#         request_data = request.get_json()
#         if "name" and "price" not in request_data:
#             return {"message" : "name and price are required"}, 400  # 400 Bad Request status code
#         items[id] = request.get_json()
#         return {"message" : "items updated successfully"}, 201
#     return {'message' : 'item not found'}, 404