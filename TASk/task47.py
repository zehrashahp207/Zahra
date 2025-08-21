from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = []

@app.route('/')
def index():
    return render_template('xedin.html', posts=posts)

@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('posths.html')

@app.route('/post/<int:post_id>')
def view_post(post_id):
    if 0 <= post_id < len(posts):
        post = posts[post_id]
        return render_template('gonder.html', post=post)
    return "Post tapilmadi", 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)
