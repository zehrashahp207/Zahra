from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
<h1>Saqlam heyat ucun, su qebulu tovsiuecisi</h1>
<p>Su icmeye verdisinizi izlemek ucun <a href="/water">buraya klikleyin</a>.</p>
"""

@app.route("/water", methods=["GET", "POST"])
def water():
    if request.method == "POST":
        ad = request.form.get("ad")
        cekisi = request.form.get("cekisi")
        stakan = request.form.get("stakan")

        if not ad or not cekisi or not stakan:
            return """
            <h2>Zehmet olmasa butun melumatlari doldurun.</h2>
            <a href="/water">Geri qayit</a>
            """
        try:
            cekisi_kg = float(cekisi)
            stakan_sayi = int(stakan)  
        except ValueError:
            return """
            <h2>Ceki ve stekan sayi duzgun formatda olmalidir.</h2>
            <a href="/water">Geri qayit</a>
            """
        ideal_su_ml = cekisi_kg * 35
        ideal_stakan = ideal_su_ml / 250 

        if stakan_sayi < ideal_stakan:
            qalib_olmaq_ucun = ideal_stakan - stakan_sayi
            mesaj = f"Sen daha {qalib_olmaq_ucun:.1f} stekan su icmelisen. Daha cox su ic, saglam qal!"
        elif ideal_stakan <= stakan_sayi <= ideal_stakan * 2:
            mesaj = "Artiq kifayet qeder su icmisen, bele davam et!"
        else:
            mesaj = """
            <strong>Diqqet!</strong> Cox su icmek saglamliq ucun tehlukelidir.<br>
            Lutfen, su qebulunu normaya sal ve hekimle meslehetles.
            """

        return f"""
<h2>Tesekkurler, {ad}!</h2>
<p>Cekisi: {cekisi_kg} kg</p>
<p>Bugun {stakan_sayi} stekan su icmisen.</p>
<p>Idmancilar ucun ideal gundelik su miqdari texminen {ideal_stakan:.1f} stekandir.</p>
<p>{mesaj}</p>
<a href="/water">Yeniden qeyd et</a>
"""

    return """
<h1>Su qebulu tovsiyyecisi</h1>
<form method="POST">
    Adiniz: <input type="text" name="ad" required><br><br>
    Cekisi(kq): <input type="number" step="0.1" name="cekisi" min="30" max="200" required><br><br>
    Bugun nece stekan su icdiniz? <input type="number" name="stakan" min="0" required><br><br>
    <button type="submit">Gonder</button>
</form>
"""

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)