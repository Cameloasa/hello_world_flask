
from flask import Flask
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/date')
def date():
    return f'Current date: {datetime.now().strftime("%Y-%m-%d")}'

if __name__ == '__main__':
    app.run(debug=True)
