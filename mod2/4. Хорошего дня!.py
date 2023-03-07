from flask import Flask
from datetime import datetime

app = Flask(__name__)

WEEKDAYS_TUPLE = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')


@app.route('/hello-world/<user_name>')
def hello_world(user_name):
    weekday = datetime.today().weekday()
    res = f'Привет, {user_name}. '
    if weekday in (2, 4, 5):
        return res + f'Хорошей {WEEKDAYS_TUPLE[weekday]}!'
    else:
        return res + f'Хорошего {WEEKDAYS_TUPLE[weekday]}!'


if __name__ == "__main__":
    app.run(debug=True)
