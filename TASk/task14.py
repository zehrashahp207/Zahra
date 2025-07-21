from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Basliq</h1>
    <p><strong>Qalin</strong ve <em>italik</em> metn.</p>
    <p><b>Qalin</b> ve <i>italik</i> stil numunesi.</p>
    <p><mark>Isiqlandirilmis</mark> ve <small>kicik</small> yazi.</p>
    <p><del>Kohne</del> <ins>Yeni</ins> qiymet.</p>
    <p>Kimyevi: H<sub>2</sub>0, Riyazi: X<sup></p>
    <hr>
    Salam<br>Necesen?"""

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=1453)
