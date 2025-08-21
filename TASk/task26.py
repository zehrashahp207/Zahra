from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/water", methods=["GET","POST"])
def water():
    if request.method == "POST":
        ad = request.form.get("ad")
        su = request.form.get("su")
        mesq = request.form.get("mesq")

        if not ad or not su or mesq not in ["beli","xeyr"]:
            error = "Zehmet olmasa butun mehsullari duzgun doldurun."
            return render_template("water_form.html", error=error)
        
        try:
            su_miqdari = float(su)
        except ValueError:
            error = "Su miqdari duzgun formada olmalidir."
            return render_template("water_form.html", error=error)
        
        minimum_su = 2.0 if mesq == "xeyr" else 2.7

        if su_miqdari >= minimum_su:
            mesaj = "Ela! Su istehlakiniz kifayet qederdir."
        elif 1.5 <= su_miqdari < minimum_su:
            mesaj = "Orta seviyyededir. Bir az daha cox su icmeye calisin."
        else:
            mesaj = "Diqqet! Bedeniniz kifayet qeder su qebul etmir. Daha cox su icin."

        return render_template("result.html", ad=ad, su=su_miqdari, mesq=mesq, mesaj=mesaj)
    return render_template("water_form.html", error=None)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)