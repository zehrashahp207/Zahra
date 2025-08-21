from flask import Flask, request, render_template, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "sirli-soz"

# Sadə heyvan siyahısı (azərbaycanca və ya ingiliscə qarışıq istifadə edə bilərik)
HEYVANLAR = [
    "aslan", "ayi", "at", "balina", "canavar", "deve", "devequşu", 
    "ejdaha", "fil", "ilan", "it", "pisik", "qarga", "okuz"
    "quş", "sincab", "timsah", "zebra", "lama", "kirpi"
]

@app.route("/", methods=["GET", "POST"])
def herf_oyunu():
    if "herf" not in session:
        session["herf"] = random.choice("abcdefikqlmosz")

    mesaj = ""
    herf = session["herf"]

    if request.method == "POST":
        soz = request.form.get("soz", "").strip().lower()

        if soz.startswith(herf) and soz in HEYVANLAR:
            mesaj = f"Dogrudur! '{soz}' sozu '{herf.upper()}' herfi ile baslayan heyvan adidir!"
        elif soz.startswith(herf):
            mesaj = f"'{soz}' '{herf.upper()}' ile baslayir, amma heyvan adi deyil."
        else:
            mesaj = f"Sehv! '{soz}' sozu '{herf.upper()}' herfi ile baslamir."

        return render_template("netice.html", mesaj=mesaj)

    return render_template("herf.html", herf=herf)

@app.route("/restart")
def restart():
    session.pop("herf", None)
    return redirect(url_for("herf_oyunu"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)