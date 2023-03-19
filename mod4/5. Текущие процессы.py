import shlex
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route('/ps', methods=['GET'])
def ps():
    args: list[str] = request.args.getlist('arg')
    clean_args = [shlex.quote(arg) for arg in args]
    command = shlex.split(f'ps {"".join(clean_args)}')
    res = subprocess.run(command, capture_output=True)
    return f'<pre>{res.stdout.decode()}</pre>'


if __name__ == '__main__':
    app.run(debug=True)
