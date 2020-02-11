from flask import Flask, request, render_template
from login import login_user, serve_login_page

app = Flask(__name__)


@app.route('/')
def index():
    return 'Server Works'


@app.route('/greet/<name>')
def say_hello(name=None):
    return render_template('/user-profile.html', name=name)


# Adding Variables
@app.route('/user/<username>')
def show_user(username):
    return f"UserName is {username}"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_user()
    elif request.method == 'GET':
        serve_login_page()


# Accessing data from the Request
@app.route('/user', methods=['GET', 'POST'])
def get_user():
    username = request.form['username']
    password = request.form['password']
    # login(arg,arg) is a function that tries to log in and returns true or false
    status = login(username, password)
    return status


# Uploading data
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        static_file = request.files['the_file']
        static_file.save('/var/www/uploads/profilephoto.png')

    return 'Success'
