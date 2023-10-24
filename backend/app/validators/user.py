from marshmallow import Schema, fields, validate, validates, ValidationError


class UserValidator(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    role = fields.Str(
        validate=validate.OneOf(["user", "admin"]), allow_none=True, load_default="user"
    )

    @validates("username")
    def validate_username(self, value: str):
        if len(value.strip()) == 0:
            raise ValidationError("Length of name must be greather than 0")

    @validates("password")
    def validate_password(self, value: str):
        if len(value.strip()) == 0:
            raise ValidationError("Length of password must be greather than 0")


user_validator = UserValidator()
