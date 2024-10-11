"""
While creating Item file we found that we have to put a lot of if condition to check
the parameters type and data validation. So to reduce the complexity of condition we 
have a library {marshmallow} , to ensure data validation.

"""


from marshmallow import  Schema, fields


class ItemSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Int(required=True)

class ItemGetSchema(Schema):
    id = fields.Str(dump_only = True)
    name = fields.Str(required=True)
    price = fields.Int(required=True)

class SuccessMessageSchema(Schema):
    message = fields.Str(dump_only =True)

class ItemQuerySchema(Schema):
    id = fields.Str(required = True)

class ItemOptionalQuerySchema(Schema):
    id = fields.Str(required = False)

class UserSchema(Schema):
    id = fields.Int(dump_only = True)
    username = fields.String(required = True)
    password = fields.String(load_only = True)
    
class UserQuerySchema(Schema):
    id = fields.Int(required = True)