from flask import Flask
import os


app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'you-will-never-guess'
basedir = os.path.abspath(os.path.dirname(__file__))


from app import routes