from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
<h1>Ise qeydiyyat sistemi</h1>
<p>Muraciet ucun <a href="/register">buraya klikleyin</a>.</p>
"""

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        ad = request.form.get("ad")
        soyad = request.form.get("soyad")
        email = request.form.get("email")
        telefon = request.form.get("telefon")

        if not ad or not soyad or not email or not telefon:
            return """
            <h2>Zehmet olmasa butun saheleri doldurun.</h2>
            <a href="/register">Geri qayit</a>
            """

        return f"""
        <h2>Tesekkurler, {ad} {soyad}!</h2>
        <p>Sizin muracietiniz qebul olundu.</p>
        <p><strong>Elaqe:</strong> {email} | {telefon}</p>
        <a href="/register">Basqa bir qeydiyyat et</a>
        """

    # GET metodu - formu göstər
    return """
    <h1>Ise qeydiyyat formu</h1>
    <form method="POST">
        Adiniz: <input type="text" name="ad" required><br><br>
        Soyadiniz: <input type="text" name="soyad" required><br><br>
        Email: <input type="text" name="email" required><br><br>
        Telefon: <input type="text" name="telefon" required><br><br>
        <button type="submit">Gonder</button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)
