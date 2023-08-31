from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C {}'.format(text.replace('_',' '))

@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text):
    return 'Python {}'.format(text.replace('_',' ')) 

@app.route('/number/<int:n>', strict_slashes=False)
def check_number(n):
    return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def templete_one(n):
    return render_template('5-number.html', number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def templete_two(n):
    even_odd = 'even' if (n%2==0) else 'odd'
    return render_template('5-number.html', number=n ,even_odd =even_odd )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

__doc__ = """
doc for module
"""