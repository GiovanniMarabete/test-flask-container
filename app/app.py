from flask import Flask, render_template, url_for, jsonify
from AzureCLI import *
app = Flask(__name__)

posts = [
    {
        'author': 'Pippo',
        'title': 'Blog post 1',
        'content': 'First post GitHub Actions 2023',
        'date_posted': 'Febraury 20, 2019'
    },
    {
        'author': 'Pluto',
        'title': 'Blog post GitHub Actions',
        'content': 'Second post content',
        'date_posted': 'Febraury 28, 2019'
    }

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title ='About')

@app.route('/login')
def login():
    return render_template('login.html', title ='Login')

@app.route('/register')
def register():
    return render_template('register.html', title ='Register')

@app.route('/listvms', methods=['GET'])
def listvms():
    return jsonify(AzureCLI.listVMs())

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0', port="80")
    