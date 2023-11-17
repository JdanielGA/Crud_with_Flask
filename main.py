from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

info = ['Info 1', 'Info 2', 'Info 3', 'Info 4', 'Info 5']

@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/login'))
    response.set_cookie('user_ip', user_ip)
    return response


@app.route("/login")
def login():
    return render_template('login_page.html')

@app.route("/home")
def home():
    user_ip = request.cookies.get('user_ip')
    return render_template('home.html', user_ip=user_ip)

@app.route("/create")
def create():
    return render_template('create.html')

@app.route("/read")
def read():
    return render_template('read.html', info=info)

@app.route("/update")
def update():
    return render_template('update.html')

@app.route("/delete")
def delete():
    return render_template('delete.html')