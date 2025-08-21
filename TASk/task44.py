from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def word_count():
    result = ""
    if request.method == "POST":
        text = request.form.get("text")
        if text and text.strip():
            words = text.strip().split()
            count = len(words)
            result = f"Daxil etdiyiniz metnde {count} soz var."
        else:
            result = "Zehmet olmasa metn daxil edin."

    return f"""
    <h1>Soz sayici</h1>
    <form method="POST">
        Metn daxil edin:<br>
        <textarea name="text" rows="5" cols="40" required></textarea><br><br>
        <button type="submit">Say</button>
    </form>
    <p><strong>{result}</strong></p>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)
