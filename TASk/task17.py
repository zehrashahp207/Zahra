from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
<h1>Xos geldiniz!<h1>
<h2>Ehvalinizi bizimle bolusmek ucun <a href='/feedback'>buraya klikleyin</a>.<h2>
"""

@app.route("/feedback",methods=["GET","POST"])
def feedback():
    if request.method == "POST":
        ad = request.form.get("ad")
        mood = request.form.get("mood")
        if ad and mood:
            return f"""
<h2>Tesekkurler,{ad}!</h2>
<p>Ehvaliniz:<strong>{mood}</stong><p>
<p>Unutmayin:Her bir gun yeni baslangicdir❤️</p>
<a href="/feedback">Yeniden gonder</a>
"""
        else:
            return"""
<h2>Zehmet olmasa,butun xanalari doldurun.</h2>
<a href="/feedback">Yeniden cehd et</a>
"""
    return """
<h1>Bugunki Ehvalinizi Paylasin</h1>
<form method="POST">
    Adiniz:<input type="text" name="ad"><br><br>
    Bugunku ehvaliniz: <input type="text" name="mood"><br><br>
    <input type="submit" value="Gonder">
</from>
"""

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)