from marshmallow import Schema, fields, validates, ValidationError


class TweetValidator(Schema):
    content = fields.Str(required=True)
    image_name = fields.Str(allow_none=True)
    image_path = fields.Str(allow_none=True)

    @validates("content")
    def validate_content(self, value: str):
        if len(value.strip()) == 0:
            raise ValidationError("Length of content must be greather than 0")


tweet_validator = TweetValidator()
