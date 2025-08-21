from flask import Flask, request
import random
import string

app = Flask(__name__)

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(chars) for _ in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password

@app.route("/", methods=["GET", "POST"])
def index():
    password = None
    if request.method == "POST":
        length = request.form.get("length", 12)
        try:
            length = int(length)
            if length < 6:
                length = 6  
        except ValueError:
            length = 12
        password = generate_password(length)

    return f"""
    <h1>Sifre Generatoru</h1>
    <form method="POST">
        Sifre uzunlugu (minimum 6): <input type="number" name="length" min="6" max="32" value="12" required><br><br>
        <button type="submit">Sifre yarat</button>
    </form>
    <br>
    {f"<h3>Yaradilmis sifre: <code>{password}</code></h3>" if password else ""}
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)
