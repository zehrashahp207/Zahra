from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = "gizli-soz"

xatireler = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        basliq = request.form.get("basliq")
        metn = request.form.get("metn")

        if not basliq or not metn:
            return render_template("anash.html", error="Zehmet olmasa hem basliq hem metn daxil edin.", xatireler=xatireler)

        xatireler.append({"basliq": basliq, "metn": metn})

        return redirect(url_for("show_xatireler"))

    return render_template("anash.html", xatireler=xatireler)

@app.route("/sonh")
def show_xatireler():
    return render_template("sonh.html", xatireler=xatireler)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)
