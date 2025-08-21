from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("hom.html")

@app.route("/fruit", methods=["GET","POST"])
def fruit():
    if request.method == "POST":
        ad = request.form.get("ad")
        porsiya = request.form.get("porsiya")
        sekerli = request.form.get("sekerli")
        if not ad or not porsiya or sekerli not in ["beli", "xeyr"]:
            error = "Zehmet olmasa butun melumatlari duzgun daxil edin."
            return render_template("fruit_form.html", error=error)
        
        try:
            porsiya_sayi = int(porsiya)
        except ValueError:
            error = "Porsiya sayi reqem olmalidir."
            return render_template("fruit_form.html", error=error)
        
        if porsiya_sayi >= 3 and sekerli == "xeyr":
            mesaj = "Tebrikler!Meyve qebulu balansli ve saglamdir."
        elif 1 <= porsiya_sayi < 3 or sekerli == "beli":
            mesaj = "Yaxsidir, amma daha az sekerli meyvelere ustunluk verin ve porsiyani artirin."
        else:
            mesaj = "Cox az meyve yeyirsiniz.Gune azi 2-3 porsiya elave etmeye calisin."
        return render_template("resul.html", ad=ad, porsiya=porsiya_sayi, sekerli=sekerli, mesaj=mesaj)
    return render_template("fruit_form.html", error=None)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=1453)