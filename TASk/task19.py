from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
<h1>Xos geldiniz!</h1>
<h2>Ehvalinizi bizimle bolusmek ucun <a href='/feedback'>buraya klikleyin</a>.</h2>
"""

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        ad = request.form.get("ad")
        mood = request.form.get("mood")
        if ad and mood:
            if mood == "Yaxsiyam":
                mesaj = "Hemise yaxsi ol, deyis, inkisaf et, yuksel."
            elif mood == "Pisem":
                mesaj = "Pis olma, sen her seyden daha deyerlisen."
            elif mood == "Normalam":
                mesaj = "Daha yaxsi olaqa calis. Heyat cox gozeldi."
            else:
                mesaj = ""
            return f"""
<h2>Tesekkurler, {ad}!</h2>
<p>Ehvaliniz: <strong>{mood}</strong></p>
<p>{mesaj}</p>
<p>Unutmayin: Her bir gun yeni baslangicdir :heart:</p>
<a href="/feedback">Yeniden gonder</a>
"""
        else:
            return """
<h2>Zehmet olmasa, butun xanalari doldurun.</h2>
<a href="/feedback">Yeniden cehd et</a>
"""
    else:
        return """
<h1>Bugunki Ehvalinizi Paylasin</h1>
<form method="POST">
    Adiniz: <input type="text" name="ad" required><br><br>
    Ehvaliniz:<br>
    <button type="submit" name="mood" value="Yaxsiyam">Yaxsiyam</button>
    <button type="submit" name="mood" value="Pisem">Pisem</button>
    <button type="submit" name="mood" value="Normalam">Normalam</button>
</form>
"""

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)
