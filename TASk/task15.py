from flask import Flask, render_template

app = Flask(__name__)
#Esas sehife
@app.route("/")
def home():
    return"""
<h1>Ana Sehife</h1>
<p>Salam, hormetli istifadeci:)<p>
<a href="/haqqinda">Haqqimda<a><br>
<a href="/elaqe">Elaqe<a><br>
<a href="/layihe">Layihe<a><br>
"""
#Haqqinda sehifesi
@app.route("/haqqinda")
def haqqinda():
    return"""
<h2>Haqqimda</h2>
Menim adim Zehradir. Size komek ucun sayt yaratmisamm))<br>
<a href="/">Geri qayit</a>
"""
#Elaqe
@app.route("/elaqe")
def elaqe():
    return"""
<h2>Elaqe<h2>
<h4>Email:shahpelengovazehra@gmail.com<br>
Elaqe nomresi:050 *** ** **<h4>
<a href="/">Geri qayit</a>
"""

#Layihe
@app.route("/layihe")
def layihe():
    return"""
<h2>Layihe</h2>
Men sosial isciyem,sosial isle elaqeli problemlerinizle baqli muraciet ede bilersiz:))<br>
<a href="/">Geri qayit</a>
"""

if __name__=="__main__":
    app.run(port=1453,debug=True, host="0.0.0.0")
