from flask import Flask
import subprocess
import shlex

app = Flask(__name__)


def start_server(port: int):
    command = shlex.split(f'lsof -i:{port}')
    res = subprocess.run(command, capture_output=True).stdout.decode()
    if res != '':
        for value in res.split():
            if value.isdigit():
                command = shlex.split(f'kill {value}')
                subprocess.run(command)
                break
    app.run(port=port)


start_server(5000)
