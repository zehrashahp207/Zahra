from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    age = None
    error = None

    if request.method == "POST":
        dob_str = request.form.get("dob")
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d")  
            today = datetime.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 0:
                error = "Dogum tarixi gelecekde ola bilmez."
                age = None
        except (ValueError, TypeError):
            error = "Zehmet olmasa duzgun tarix formatinda daxil edin (YYYY-MM-DD)."

    return f"""
    <h1>Dogum Gunu Hesablayici</h1>
    <form method="POST">
        Dogum tarixinizi daxil edin: <input type="date" name="dob" required><br><br>
        <button type="submit">Yasimi Hesabla</button>
    </form>
    <br>
    {f"<h3>Siz {age} yasindasiniz.</h3>" if age is not None else ""}
    {f"<p style='color:red;'>{error}</p>" if error else ""}
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)
