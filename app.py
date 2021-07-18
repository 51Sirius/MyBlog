from flask import Flask, render_template, request, redirect, url_for, abort
from os import environ
import locale
from models import Users, db
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
import cfg
from flask_migrate import Migrate

app = Flask(__name__)
locale.setlocale(locale.LC_ALL, '')
app.config['SECRET_KEY'] = cfg.S_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
login = LoginManager(app)
migrate = Migrate(app, db)


@app.route('/')
def homepage():
    return render_template('index.html', title='Blog')


if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
