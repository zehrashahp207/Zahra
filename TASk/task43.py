from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1"))
            num2 = float(request.form.get("num2"))
            operation = request.form.get("operation")

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    result = "Sifira bolme mumkun deyil!"
                else:
                    result = num1 / num2
            else:
                result = "Emeliyyat secilmeyib."
        except (ValueError, TypeError):
            result = "Zehmet olmasa duzgun eded daxil edin."

    return f"""
    <h1>Sade Kalkulyator</h1>
    <form method="POST">
        Birinci eded: <input type="text" name="num1" required><br><br>
        Ikinci eded: <input type="text" name="num2" required><br><br>
        Emeliyyat:
        <select name="operation" required>
            <option value="">Secin</option>
            <option value="add">Toplama (+)</option>
            <option value="subtract">Cixma (-)</option>
            <option value="multiply">Vurma (*)</option>
            <option value="divide">Bolme (/)</option>
        </select><br><br>
        <button type="submit">Hesabla</button>
    </form>
    <h2>Netice: {result}</h2>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)
