from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
<h1>Normal yuxu, saglam heyat!</h1>
<p>Gundelik yuxu keyfiyyetinizi yoxlamaq ucun <a href="/sleep">buraya klikleyin</a>.</p>
"""

@app.route("/sleep", methods=["GET", "POST"])
def sleep():
    if request.method == "POST":
        ad = request.form.get("ad")
        saat = request.form.get("saat")
        oyanma = request.form.get("oyanma")

        if not ad or not saat or not oyanma:
            return """
            <h2>Zehmet olmasa butun melumatlari doldurun.</h2>
            <a href="/sleep">Geri qayit</a>
            """

        try:
            saat_yatdi = float(saat)
            oyanma_sayi = int(oyanma)
        except ValueError:
            return """
            <h2>Yuxu saati ve oyanma sayi duzgun formatda olmalidir.</h2>
            <a href="/sleep">Geri qayit</a>
            """

        if saat_yatdi >= 7 and oyanma_sayi <= 1:
            mesaj = "Ela! Yuxu keyfiyyetin yaxsidir, bu cur davam et!"
        elif 5 <= saat_yatdi < 7 or oyanma_sayi <= 3:
            mesaj = "Yuxu keyfiyyetin orta seviyededir. Daha cox yatmaga ve az oyanmaga calis."
        else:
            mesaj = """
            <strong>Diqqet!</strong> Yuxu keyfiyyetin dusuktur.<br>
            Daha erken yatmaga calis ve hekimle meslehetlesmek faydali ola biler.
            """

        return f"""
        <h2>Tesekkurler, {ad}!</h2>
        <p>Bu gece {saat_yatdi} saat yatmisan ve {oyanma_sayi} defe oyanmisan.</p>
        <p>{mesaj}</p>
        <a href="/sleep">Yeniden yoxla</a>
        """

    # GET metodu (ilk form gorsenmesi)
    return """
    <h1>Yuxu keyfiyyeti yoxlayici</h1>
    <form method="POST">
        Adiniz: <input type="text" name="ad" required><br><br>
        Bu gece nece saat yatdiniz? <input type="number" name="saat" step="0.1" min="0" max="24" required><br><br>
        Nece defe oyandiniz? <input type="number" name="oyanma" min="0" required><br><br>
        <button type="submit">Gonder</button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)