from flask import Flask
from wtforms import IntegerField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, NumberRange

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberRange(min=1000000000, max=9999999999)])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email = form.email.data
        phone = form.phone.data
        name = form.name.data
        address = form.address.data
        index = form.index.data
        comment = form.comment.data
        return f'User {name} with email: {email} and phone: +7{phone} was registered.' \
               f'\n Address with index: {address} {index}. \n {"Comment: " + comment if comment else ""}'
    return f'Invalid input: {form.errors}', 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
