from flask import Flask

app = Flask(__name__)


@app.route('/love_cats')
def love_cats():
    return 'I love cats!'


@app.route('/hello_world')
def hello_world():
    return 'Hello, world!'


@app.errorhandler(404)
def not_found_error(error):
    reply = 'Seems like the page you want to go does not exist :(<br>' \
            '<br>' \
            'List of all available pages:<br>'
    base = 'http://127.0.0.1:5000'
    for rule in list(app.url_map.iter_rules())[1:]:
        reply += f'<a href="{base}{str(rule)}">{base}{str(rule)}</a><br>'
    return reply


if __name__ == '__main__':
    app.run(debug=True)