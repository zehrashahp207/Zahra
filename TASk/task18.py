from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def home():
    return """
<h1>Xeyallarini menimle bolus<h1>
<h2>Oz sexsi ada dunyani qurmaq ucun <a href='/ada'>bura klikle</a>.</h2>
"""
@app.route("/ada", methods=["GET", "POST"])
def ada():
    if request.method == "POST":
        ad = request.form.get("ad")
        adanin_adi = request.form.get("ada_adi")
        ne_olsun = request.form.get("ne_olsun")
        if ad and adanin_adi and ne_olsun:
            return f"""
<h2>Tebrikler, {ad}!</h2>
<p>Senin xeyal adanin adi: <strong>{adanin_adi}</strong></p>
<p>Bu adada olacaq: <em>{ne_olsun}</em></p>
<p>Xeyal gucdur. Unutma: Her boyuk ideya kicik bir xeyal ile baslayir</p>
<a href="/ada">Yeniden cehd et</a>
"""
    return """
<h1>Xeyalinda bir ada qur</h1>
<form method="POST">
Adin: <input type="text" name="ad"><br><br>
Xeyalindaki adanin adi: <input type="text" name="ada_adi"><br><br>
Bu adada neler olsun?: <input type="text" name="ne_olsun"><br><br>
<input type="submit" value="Adani Qur">
</form>
"""

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)