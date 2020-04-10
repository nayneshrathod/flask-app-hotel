import os
import yaml
from flask import Flask, render_template, redirect, request, session, flash
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
Bootstrap(app)
CKEditor(app)

db = yaml.load(open('db.yaml'))
# app.config['MYSQL_']
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = os.urandom(24)
mysql = MySQL(app)

app.config['SECRET_KEY'] = 'secret'


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/product')
def product():
    return render_template('products.html')

if __name__ == "__main__":
    app.run(debug=True)