from marshmallow import Schema, fields

class RequestInput(Schema):
    square_meters = fields.Integer(required=True, strict=True)
    number_of_rooms = fields.Integer(required=True, strict=True)
    price_per_month = fields.Integer(required=True, strict=True)

# Input Schema
request_input_schema_multiple = RequestInput(many=True)