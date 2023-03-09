from flask import Flask
import os

app = Flask(__name__)


@app.route('/preview/<size>/<path:file_name>')
def file_preview(size, file_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, file_name.split('/')[-1])
    with open(file_path) as file:
        text_len = os.stat(file_path).st_size - 1
        if int(size) < text_len:
            text_len = int(size)
        return f'<b>{file_path}</b> {text_len} <br>{file.read(text_len)}'


if __name__ == "__main__":
    app.run(debug=True)
