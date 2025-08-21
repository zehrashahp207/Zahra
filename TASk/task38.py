from flask import Flask, request, redirect, url_for

app = Flask(__name__)


quiz = [
    {
        "question": "Azerbaycanin paytaxti hansidir?",
        "options": ["Gence", "Baki", "Sumqayit", "Seki"],
        "answer": "Baki"
    },
    {
        "question": "Dunyanin en uzun cayi hansidir?",
        "options": ["Nil", "Amazon", "Volga", "Yangtze"],
        "answer": "Nil"
    },
    {
        "question": "Python nece proqramlasdirma dilidir?",
        "options": ["Asagi seviye", "Yuksek seviye", "Masin dili", "Assembler"],
        "answer": "Yuksek seviye"
    },
    {
        "question": "HTML ne ucun istifade olunur?",
        "options": ["Proqramlasdirma", "Veb sehife qurusu", "Verilenler bazasi", "Qrafik dizayn"],
        "answer": "Veb sehife qurusu"
    },
    {
        "question": "Azerbaycanin milli musiqi aleti hansidir?",
        "options": ["Tar", "Piano", "Gitara", "Saksafon"],
        "answer": "Tar"
    },
    {
        "question": "Dunyanin en boyuk okeani hansidir?",
        "options": ["Atlantik", "Hint", "Arktika", "Pasifik"],
        "answer": "Pasifik"
    },
    {
        "question": "Qalereya ne ucun istifade olunur?",
        "options": ["Resmlar ucun", "Videolar ucun", "Kitablar ucun", "Musiqi ucun"],
        "answer": "Resmlar ucun"
    },
    {
        "question": "Insan bedeninde en boyuk orqan hansidir?",
        "options": ["Deri", "Qaraciyer", "Beyin", "Urek"],
        "answer": "Deri"
    },
    {
        "question": "Qar nece rengdir?",
        "options": ["Ag", "Qara", "Goy", "Qirmizi"],
        "answer": "Ag"
    },
    {
        "question": "Tebii ehtiyatlar hansidir?",
        "options": ["Menevi", "Xammal", "Texniki", "Maddi"],
        "answer": "Xammal"
    },
    {
        "question": "Su nece molekulelerden ibaretdir?",
        "options": ["H2O", "CO2", "O2", "NaCl"],
        "answer": "H2O"
    },
    {
        "question": "Dunyanin en boyuk qitesi hansidir?",
        "options": ["Avropa", "Asiya", "Afrika", "Antarktida"],
        "answer": "Asiya"
    },
    {
        "question": "Elektronun yuku necedir?",
        "options": ["Menfi", "Musbet", "Netral", "Pozitiv"],
        "answer": "Menfi"
    },
    {
        "question": "Yay nece fəsildir?",
        "options": ["Isti fesil", "Soyuq fesil", "Qis fesili", "Yagmurlu fesil"],
        "answer": "Istilik fəsili"
    },
    {
        "question": "Dunya nece sekildedir?",
        "options": ["Dairevi", "Kvadrat", "Duz", "Ucbucaq"],
        "answer": "Dairevi"
    },
    {
        "question": "Quslar ne ile uca biler?",
        "options": ["Pence", "Qanad", "Ayaq", "Budaq"],
        "answer": "Qanad"
    },
    {
        "question": "Qar nece yaranir?",
        "options": ["Buz kristallari", "Yagmurdur", "Duman", "Gunes isigi"],
        "answer": "Buz kristallari"
    },
    {
        "question": "Kitab ne ucundur?",
        "options": ["Oxumaq ucun", "Yemek ucun", "Yatmaq ucun", "Oyun ucun"],
        "answer": "Oxumaq ucun"
    }
]


@app.route("/", methods=["GET", "POST"])
def quiz_game():
    if request.method == "POST":
        score = 0
        for i in range(len(quiz)):
            user_answer = request.form.get(f"q{i}")
            if user_answer == quiz[i]["answer"]:
                score += 1
        return f"""
        <h1>Netice</h1>
        <p>Siz {len(quiz)} sualdan {score} doğru cavab verdiniz.</p>
        <a href="/">Yeniden oyna</a>
        """

    questions_html = ""
    for i, q in enumerate(quiz):
        options_html = ""
        for option in q["options"]:
            options_html += f'<input type="radio" name="q{i}" value="{option}" required> {option}<br>'
        questions_html += f"<h3>{q['question']}</h3>{options_html}<br>"

    return f"""
    <h1>Quiz Oyunu</h1>
    <form method="POST">
        {questions_html}
        <button type="submit">Cavablari Gonder</button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)