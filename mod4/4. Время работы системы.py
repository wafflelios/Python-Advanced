from flask import Flask

app = Flask(__name__)


@app.route('/uptime', methods=['GET'])
def get_uptime():
    with open('/proc/uptime') as file:
        uptime = float(file.readline().split()[0])
        return f'Current uptime is {uptime} seconds.'


if __name__ == "__main__":
    app.run(debug=True)
