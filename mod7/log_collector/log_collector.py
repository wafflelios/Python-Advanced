from flask import Flask, request

app = Flask(__name__)


@app.route('/logs/post', methods=['POST'])
def post_log():
    data = request.form.to_dict()
    with open('logs/log_collector.log', 'a+') as file:
        log = f'{data["levelname"]} | {data["name"]} | {data["asctime"]} | {data["lineno"]} | {data["msg"]}\n'
        file.write(log)


@app.route('/logs/get')
def get_log():
    with open('logs/log_collector.log', 'r') as file:
        result = str(file.read())
        return result.replace('\n', '<br>')


if __name__ == '__main__':
    app.run(debug=True)