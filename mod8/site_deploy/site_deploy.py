from flask import Flask

app = Flask(__name__)

@app.route('/')
def happy_new_year():
  return 'С новым годом!'

if __name__ == '__main__':
  app.run(debug=True)
