from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def planner():
    if request.method == "POST":
        ad = request.form.get("ad")
        gun = request.form.get("gun")
        plan1 = request.form.get("plan1")
        plan2 = request.form.get("plan2")
        plan3 = request.form.get("plan3")

        if not ad or not gun or not plan1:
            return render_template("planner.html", error="zehmet olmasa en azi bir fealiyyet daxil edin.")
        planlar = [p for p in [plan1, plan2, plan3] if p.strip()!=""]

        return render_template("gosterici.html", ad=ad, gun=gun, planlar=planlar)
    return render_template("planner.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)