from flask import Flask, render_template, request

app = Flask(__name__)

colors = {
    'qirmizi':'Qirmizi enerji remzidir.',
    'mavi':'Mavi sakitlik ve etibarliliq rengidir.',
    'yasil':'Tebiet ve harmoniya rengidir.',
    'sari':'Sari xosbextlik ve pozitiv rengdir.',
    'qara': 'Qara guc ve sirr rengidir.',
}

html_colors = {
    'qirmizi':'red',
    'mavi':'blue',
    'yasil':'greemessage = n',
    'sari':'yellow',
    'qara':'black',
}

@app.route('/',methods=['GET','POST'])
def index():
    message = ''
    selected_color = ''
    user_input = ''
    if request.method == 'POST':
        user_input = request.form.get('color', '').strip().lower()
        if user_input == '':
            message = 'Zehmet olmasa, reng daxil edin.'
        elif user_input in colors:
            message = colors[user_input]
            selected_color = html_colors.get(user_input, 'black')
        else:
            message = 'Bu reng siyahida yoxdur.'
    return render_template('color.html', message=message, color_name=user_input, text_color=selected_color)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)