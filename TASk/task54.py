from flask import Flask, request, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import uuid
from datetime import timedelta

app = Flask(__name__)

# Gizli açar (secret key)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['JWT_SECRET_KEY'] = app.config['SECRET_KEY']
app.config['JWT_TOKEN_LOCATION'] = ['headers']

jwt = JWTManager(app)

# Sadə "verilənlər bazası"
users_db = {}

class User:
    def __init__(self, public_id, name, email, password):
        self.public_id = public_id
        self.name = name
        self.email = email
        self.password = password

    @staticmethod
    def query_filter_by_email(email):
        for user in users_db.values():
            if user.email == email:
                return user
        return None

    @staticmethod
    def query_filter_by_public_id(public_id):
        return users_db.get(public_id, None)

@app.route('/')
def home():
    return "Welcome to the Home Page."

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if User.query_filter_by_email(email):
            return jsonify({'message': 'User already exists!'}), 400

        hashed_password = generate_password_hash(password)
        public_id = str(uuid.uuid4())
        new_user = User(public_id, name, email, hashed_password)
        users_db[public_id] = new_user

        return redirect(url_for('login'))
    return "Signup Page"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query_filter_by_email(email)
        if not user or not check_password_hash(user.password, password):
            return jsonify({'message': 'Invalid email or password'}), 401

        access_token = create_access_token(identity=user.public_id, expires_delta=timedelta(hours=1))
        return jsonify({'access_token': access_token})

    return "Login Page"

@app.route('/dashboard')
@jwt_required()
def dashboard():
    current_user_id = get_jwt_identity()
    current_user = User.query_filter_by_public_id(current_user_id)

    if not current_user:
        return jsonify({'message': 'User not found'}), 404

    return f"Welcome {current_user.name}! You are logged in."

if __name__ == "__main__":
    app.run(debug=True)
