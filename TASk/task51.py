from flask import Flask, render_template, request, redirect, url_for
import csv
import os
app = Flask(__name__)
CSV_FILE = 'responses.csv'
def read_csv():
    responses = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                responses.append(row)
    return responses
def write_csv(data):
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'age', 'color']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        color = request.form['color']
        new_response = {'name': name, 'age': age, 'color': color}
        write_csv(new_response)
        return redirect(url_for('index'))
    responses = read_csv()
    return render_template('basliq.html', responses=responses)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)