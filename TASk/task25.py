from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ana_sehife():
    ad = "Aysel"
    yas = 22
    maraqlar = ["Kitab oxumaq", "Kod yazmaq", "Seyahet"]

    return render_template("index.html", ad = ad, yas = yas, maraqlar = maraqlar)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)