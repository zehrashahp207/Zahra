from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

responses = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        color = request.form['color']

        responses.append({'name': name, 'age': age, 'color': color})
        
        return redirect(url_for('index'))
    
    return render_template('basliq.html', responses=responses)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)