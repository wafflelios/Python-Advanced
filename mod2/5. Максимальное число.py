from flask import Flask

app = Flask(__name__)


@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    try:
        numbers = numbers.split('/')
        numbers = [int(num) for num in numbers]
        return 'Максимальное число:' + str(max(numbers))
    except ValueError:
        return 'Ни одно число не было передано.'


if __name__ == "__main__":
    app.run(debug=True)
