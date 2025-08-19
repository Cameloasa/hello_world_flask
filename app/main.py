
from flask import Flask, request, render_template_string
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

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            return f'Hello, {name}!'
        return 'Please provide a name.'
    return render_template_string('''
        <form method="post">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name">
            <input type="submit" value="Submit">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
