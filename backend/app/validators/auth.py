from marshmallow import Schema, fields, validates, ValidationError


class LoginValidator(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)

    @validates("password")
    def validate_password(self, value: str):
        if len(value.strip()) == 0:
            raise ValidationError("Length of password must be greather than 0")


login_validator = LoginValidator()
