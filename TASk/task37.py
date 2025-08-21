from flask import Flask, request, redirect, url_for

app = Flask(__name__)

notes = []
note_id_counter = 1

@app.route("/")
def home():
    notes_list = ""
    for note in notes:
        notes_list += f"""
        <li>
            {note['text']}
            <a href="/edit/{note['id']}">[Redakte]</a>
            <a href="/delete/{note['id']}" onclick="return confirm('Silinsin?')">[Sil]</a>
        </li>
        """
    return f"""
    <h1>Sade Qeyd Sistemi</h1>
    <a href="/add">Yeni Qeyd Elave Et</a>
    <ul>
        {notes_list if notes else '<li>Qeyd yoxdur</li>'}
    </ul>
    """

@app.route("/add", methods=["GET", "POST"])
def add_note():
    global note_id_counter
    if request.method == "POST":
        text = request.form.get("text")
        if text:
            notes.append({"id": note_id_counter, "text": text})
            note_id_counter += 1
            return redirect(url_for("home"))
        else:
            return "<h3>Zehmt olmasa qeyd metnini yazin!</h3><a href='/add'>Geri</a>"
    return """
    <h1>Yeni Qeyd Elave Et</h1>
    <form method="POST">
        <textarea name="text" rows="4" cols="50" placeholder="Qeyd metnini yazin..." required></textarea><br><br>
        <button type="submit">Elave Et</button>
    </form>
    <a href="/">Geri</a>
    """

@app.route("/edit/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    note = next((n for n in notes if n["id"] == note_id), None)
    if not note:
        return "<h3>Qeyd tapilmadi!</h3><a href='/'>Geri</a>"

    if request.method == "POST":
        text = request.form.get("text")
        if text:
            note["text"] = text
            return redirect(url_for("home"))
        else:
            return f"<h3>Zehmet olmasa qeyd metnini yazin!</h3><a href='/edit/{note_id}'>Geri</a>"

    return f"""
    <h1>Qeyd Redakte Et</h1>
    <form method="POST">
        <textarea name="text" rows="4" cols="50" required>{note['text']}</textarea><br><br>
        <button type="submit">Yadda saxla</button>
    </form>
    <a href="/">Geri</a>
    """

@app.route("/delete/<int:note_id>")
def delete_note(note_id):
    global notes
    notes = [n for n in notes if n["id"] != note_id]
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)
