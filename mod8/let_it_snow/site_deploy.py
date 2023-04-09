from flask import Flask, render_template, send_from_directory
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
js_dir = os.path.join(base_dir, 'js')

app = Flask(__name__, template_folder=base_dir)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(js_dir, path)


if __name__ == '__main__':
    app.run(debug=True)
