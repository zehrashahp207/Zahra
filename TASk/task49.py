from flask import Flask, render_template, request

app = Flask(__name__)

colors = {
    'qirmizi': 'Qirmizi enerji ve remzidir.',
    'mavi': 'Mavi sakitlik ve etibarliliq rengidir.',
    'yasil': 'Tebiet ve harmoniya rengidir.',
    'sari': 'Sari xosbextlik ve pozitiv rengdir.',
    'qara': 'Qara guc ve sirr rengidir.',
}

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        user_input = request.form.get('color', '').strip().lower()
        if user_input == '':
            message = 'Zehmet olmasa, reng daxil edin.'
        elif user_input in colors:
            message = colors[user_input]
        else:
            message = 'Bu reng siyahida yoxdur.'
    return render_template('rengg.html', message=message)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)