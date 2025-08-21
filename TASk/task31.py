from flask import Flask, request, render_template, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "gizli-açar"  

@app.route("/", methods=["GET", "POST"])
def index():
    if "target" not in session:
        session["target"] = random.randint(1, 20)
        session["tries"] = 0

    message = ""

    if request.method == "POST":
        guess = request.form.get("guess")

        if guess:
            try:
                guess = int(guess)
                session["tries"] += 1
                target = session["target"]

                if guess < target:
                    message = "Daha boyuk bir reqem seç!"
                elif guess > target:
                    message = "Daha kicik bir rəqəm seç!"
                else:
                    result = f"Təbriklər! {session['tries']} cehde tapdin! Rəqəm: {target}"
                    session.pop("target")
                    session.pop("tries")
                    return render_template("cavab.html", result=result)
            except ValueError:
                message = "zehmet olmasa duzgun reqem daxil et!"

    return render_template("anas.html", message=message)

@app.route("/restart")
def restart():
    session.pop("target", None)
    session.pop("tries", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)