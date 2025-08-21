from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def xercler():
    if request.method == "POST":
        ad = request.form.get("ad")
        hefte = request.form.get("hefte")
        xerc_list = []
        total = 0

        for i in range(1, 8):
            qiymet = request.form.get(f"qiymet{i}")
            if qiymet:
                try:
                    q = float(qiymet)
                    xerc_list.append(q)
                    total += q
                except ValueError:
                    return render_template("xercler.html", error="Qiymetler yalniz reqemle olmalidir.")

        if not ad or not hefte or not xerc_list:
            return render_template("xercler.html", error="Zehmet olmasa ad, hefte ve en azi bir xerci daxil edin.")

        return render_template("hesab.html", ad=ad, hefte=hefte, xerc_list=xerc_list, total=total)

    return render_template("xercler.html")
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)
