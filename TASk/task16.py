from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<h2>Heyvanlar dunyasi</h2>
<p>Asagidaki heyvanlardan birini secin ve haqqinda melumat oxuyun:<p>
<ul>
    <li><a href="/animal/cat">Pisik</a></li>
    <li><a href="/animal/dog">It</a></li>
    <li><a href="/animal/bird">Qus</a></li>
    <li><a href="/animal/dolphin">Delfin</a></li>
    <li><a href="/animal/horse">At</a></li>
    <li><a href="/animal/rabbit">Dovsan</a></li>
</ul>
"""

@app.route("/animal/<name>")
def animal_info(name):
    info = {
        "cat":"Pisik ev heyvani olaraq cox meshurdur. O, musteqil ve cevik heyvandir.",
        "dog":"It insanin en yaxsi dostudur. O, sadiq ve agilli bir heyvandir.",
        "bird":"Quslar ucmaq qabiliyyetine malik canlilardir ve cox ferqli novleri vardir.",
        "dolphin": "Delfin agilli və sosial dəniz memelilerinden biridir. Onlar suda suretle hereket edir.",
        "horse":"At uzun muddet insanlar terefinden neqliyyat ve eylence meqsedi ile istifade olunub.",
        "rabbit":"Dovsan kicik ve yumusaq tuklu heyvandir, cox tez coxalir ve sevilir."
    }
    description = info.get(name.lower())
    if description:
        return f"""
<h2>{name.capitalize()}</h2>
<p>{description}</p>
<a href="/">Geri qayit</a>
"""
    else:
        return"""
<h2>Heyvan tapilmadi!</h2>
<p>Zehmet olmasa, siyahidan bir heyvan secin.</p>
<a href="/">Ana sehifeye geri don</a>
"""
if __name__ == "__main__":
    app.run(port=1453,debug=True, host="0.0.0.0")