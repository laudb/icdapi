from marshmallow import Schema, fields

class CreateRecordInputSchema(Schema):
    """ /api/record - POST

    Parameters:
      -  code 
      -  desc_short 
      -  desc_long 
      -  type 
      -  year 
    """
    # ensure the following fields exist
    code = fields.Str(required=True)
    desc_short = fields.Str(required=True)
    type = fields.Str(required=True)
    year = fields.Str(required=True)

