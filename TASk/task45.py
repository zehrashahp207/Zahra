from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def color_picker():
    background = "#ffffff"  
    if request.method == "POST":
        color = request.form.get("color")
        if color:
            background = color

    return f"""
    <html>
        <body style="background-color: {background};">
            <h1>Reng Secici</h1>
            <form method="POST">
                Reng secin: <input type="color" name="color" value="{background}">
                <button type="submit">Tətbiq et</button>
            </form>
            <p><strong>Secilmis reng: {background}</strong></p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)