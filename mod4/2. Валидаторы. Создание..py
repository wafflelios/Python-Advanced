from flask import Flask
from wtforms import IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, ValidationError
from dataclasses import Field
from typing import Optional

app = Flask(__name__)


def number_length(minimum: int, maximum: int, message: Optional[str] = None):
    if message is None:
        message = f'Input should be integer that greater than {minimum} and less than {maximum}.'

    def _number_length(form: FlaskForm, field: Field):
        for key, value in form.data.items():
            if value is None or value < minimum or value > maximum:
                raise ValidationError(message)

    return _number_length


class NumberLength:
    def __init__(self, minimum: int, maximum: int, message: Optional[str] = None):
        self.minimum, self.maximum = minimum, maximum
        if message is None:
            self.message = f'Input should be integer that greater than {minimum} and less than {maximum}.'
        else:
            self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        for key, value in form.data.items():
            if value is None or value < self.minimum or value > self.maximum:
                raise ValidationError(self.message)


class RegistrationForm(FlaskForm):
    number = IntegerField(validators=[InputRequired(), NumberLength(1000000000, 9999999999)])


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        number = form.number.data
        return f'Phone number: +7{number}'
    return f'Invalid input: {form.number.errors[0]}', 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
