from flask import Flask
from wtforms import IntegerField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, NumberRange
import logging
from collections import deque

app = Flask(__name__)
'''
Так и не поняла, в чем смысл задания, ведь машина все равно не сможет разобрать, что является словом или нет, 
без перебора всех значений.
Например пароль 'superstrongpassword' содержит в себе английские слова, но их невозможно определить без перебора 
всех слов, так как они ничем не разделены ни пробелами, ни нижним подчеркиванием, ничем.
'''

logger = logging.getLogger()
words = deque()

with open('/usr/share/dict/words') as file:
    for line in file:
        if len(line) >= 4 and line[0].isupper() is False:
            words.append(line)


def is_strong_password(password: str) -> bool:
    flag = 0
    for index in range(len(words)):
        if len(password) < 4 or words[index][:-1] in password.lower():
            flag = 1
            break
    if flag == 0:
        return True
    else:
        return False


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberRange(min=1000000000, max=9999999999)])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField()
    password = StringField(validators=[InputRequired()])


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
        password = form.password.data
        if is_strong_password(password):
            logger.info('Your password is strong.')
        else:
            logger.warning("Your password in weak! Its length is less than 4 or it includes english words.")
        return f'User {name} with email: {email} and phone: +7{phone} was registered.' \
               f'\n Address with index: {address} {index}. \n {"Comment: " + comment if comment else ""}' \
               f'\n Remember your password: {password}'
    logger.error(f'Invalid input: {form.errors}')
    return f'Invalid input: {form.errors}', 400


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename='stderr.txt',
                        format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S')
    logger.info('Started registration server')
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)