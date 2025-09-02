from flask import Flask
import names

app = Flask(__name__)


@app.route('/')
def home():
    return 'MAIN PAGE'  


@app.route('/greeting/<person>')
def greet(person):
    return f'Hello, {person}!'



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)