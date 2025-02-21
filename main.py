from flask import Flask, render_template, request, url_for, redirect, session
app = Flask(__name__)
app.secret_key =' Space Portfolio'


@app.route('/')
def start():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    session['username'] = username
    return redirect(url_for('index'))

@app.route('/index', methods = ['GET','POST'])
def index():
    user = session['username']
    return render_template('index.html', user = user)

if __name__ == "__main__":
    app.run(debug=True)