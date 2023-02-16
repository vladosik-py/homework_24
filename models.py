from marshmallow import Schema, fields

VALID_CMD_COMMANDS = ('filter', 'unique', 'map', 'limit', 'sort', 'regex')


class RequestSchema(Schema):
    cmd_1 = fields.Str(required=True)
    value_1 = fields.Str(required=True)
    file_name = fields.Str(required=True)


class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema, many=True)
    file_name = fields.Str(required=True)