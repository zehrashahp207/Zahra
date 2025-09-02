from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)
  
# Sadə söz-lüğət nümunəsi (ing - az)
sozluk = {
"apple": "alma",
    "cat": "pisik",
    "book": "kitab",
    "sun": "gunesh",
    "water": "su",
    "car": "masin",
    "house": "ev",
    "dog": "it",
    "tree": "agac",
    "flower": "gul",
    "milk": "sud",
    "bird": "qush",
    "fish": "baliq",
    "phone": "telefon",
    "computer": "komputer",
    "table": "masa",
    "chair": "stul",
    "window": "pencere",
    "door": "qapi",
    "school": "mekteb",
    "teacher": "muellim",
    "student": "telebe",
    "pen": "qelem",
    "paper": "kagiz",
    "road": "yol",
    "city": "seher",
    "river": "cay",
    "mountain": "dag",
    "music": "musiqi",
    "coffee": "qehve"
}

@app.route("/", methods=["GET", "POST"])
def oyun():
    sozler = list(sozluk.keys())
    if request.method == "POST":
        ing_soz = request.form.get("ing_soz")
        cevrilen = request.form.get("cevrilen", "").strip().lower()
        dogru_cevab = sozluk.get(ing_soz, "").lower()

        if cevrilen == dogru_cevab:
            mesaj = "Tebrikler! Tercume dogrudur."
        else:
            mesaj = f"Tercume sehvdir. Dogru cavab: {dogru_cevab}"

        yeni_soz = random.choice(sozler)

        return render_template("oyun.html", ing_soz=yeni_soz, mesaj=mesaj)
    
    ilk_soz = random.choice(sozler)
    return render_template("oyun.html", ing_soz=ilk_soz)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)
