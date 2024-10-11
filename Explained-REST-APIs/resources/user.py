
from flask import request
import uuid
from db.usersdb import UserDatabase
from flask.views import MethodView # Helps when Get api will be called it will provoke get function and so on.
from flask_smorest import Blueprint, abort 
from schemas import UserSchema, UserQuerySchema, SuccessMessageSchema
import hashlib # To convert password into hash value
from flask_jwt_extended import create_access_token, jwt_required, get_jwt # creates the token for users by taking naem and their password.
from blocklist import BLOCKLIST


blp = Blueprint("myUsers", __name__, description = "operation on users")



@blp.route("/login")
class UserLogin(MethodView):

    def __init__(self):
        self.db = UserDatabase()


    @blp.arguments(UserSchema)
    def post(self, request_data):
        username = request_data['username']
        password = hashlib.sha256(request_data['password'].encode()).hexdigest()
        password = request_data['password']
        user_id = self.db.verify_user(username, password)
        if user_id:
            return {
                      "access token" : create_access_token(identity = user_id)
                    }
        abort(400, message="Invalid username or password")
        



@blp.route("/logout")
class UserLogOut(MethodView):

    def __init__(self):
        self.db = UserDatabase()


    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        BLOCKLIST.add(jti)
        return {"message":"User Successfully logged out."}
        
        
        



@blp.route("/user")
class User(MethodView):

    def __init__(self):
        self.db = UserDatabase()

    @blp.arguments(UserQuerySchema, location='query') 
    @blp.response(200, UserSchema) 
    def get(self, args):
        id = args.get("id")
        result = self.db.get_user(id) 
        if result == None:
            abort(404, message = "user not found")
        return result


    @blp.arguments(UserSchema)
    @blp.response(200, SuccessMessageSchema)
    def post(self, request_data):
        username = request_data['username']
        password = hashlib.sha256(request_data['password'].encode()).hexdigest()
        if self.db.add_user(username, password):
            return {"message" : "User added successfully"}, 201
        abort(403, message = "User already exists")

    @blp.arguments(UserQuerySchema, location = "query")
    @blp.response(200, SuccessMessageSchema)
    def delete(self, args):
        id = args.get("id")
        if self.db.delete_user(id):
            return {"message" : "User deleted successfully"}
        abort(404, message = "User not found")



