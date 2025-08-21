from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("ev.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        ad = request.form.get("ad")
        soyad = request.form.get("soyad")
        email = request.form.get("email")
        telefon = request.form.get("telefon")

        if not ad or not soyad or not email or not telefon:
            error = "Zehmet olmasa butun saheleri doldurun."
            return render_template("register.html", error=error, ad=ad, soyad=soyad, email=email, telefon=telefon)

        return render_template("success.html", ad=ad, soyad=soyad, email=email, telefon=telefon)

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)
