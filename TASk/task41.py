from flask import Flask, request

app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            number = int(request.form.get("number"))
            if number % 2 == 0:
                result = f"{number} cut ededdir."
            else:
                result = f"{number} tek ededdir."
        except(ValueError, TypeError):
            result = "Zehmet olmasa duzgun bir eded daxil edin."

    return f"""
<h1>Eded Cut-Tek Yoxlayici</h1>
<form method="POST">
Eded daxil edin:<input type="number" name="number" required>
<button type="submit">Yoxla</button>
</form>
<p><strong>{result}</strong></p>
"""
    
if __name__ == "__main__":
    app.run(debug=True, port=1453, host="0.0.0.0")