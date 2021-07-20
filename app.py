from flask import Flask, render_template, request, redirect, url_for, abort, flash
from flask_wtf import form
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
import datetime
import locale
from os import environ
from forms import LoginForm, Registration, Answer, Settings
from flask_sqlalchemy import SQLAlchemy
from models import Users, db
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
import generate_quest as gen
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


@login.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/')
def homepage():
    return render_template('index.html', title='Blog')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/game/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    forms = LoginForm()
    if forms.validate_on_submit():
        nick = forms.username.data
        password = forms.password.data
        user = Users.query.filter_by(username=nick).first()
        if not (user and user.check_password(password)):
            abort(403)
        login_user(user, remember=forms.remember_me)
        return redirect(url_for('main_math'))
    return render_template('math/login.html', title="Login", form=forms)


@app.route('/game/registration', methods=['GET', 'POST'])
def registration():
    register_form = Registration()
    if register_form.validate_on_submit():
        email = register_form.email.data
        name = register_form.username.data
        password = register_form.password.data
        existing_user = Users.query.filter_by(email=email).first()
        if existing_user:
            abort(400)
        user = Users(username=name, email=email, password=password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main_math'))
    return render_template('math/registration.html', title="Registration", form=register_form)


@app.route('/game/math')
def main_math():
    return render_template('math/index.html', title="MathTR")


@app.route('/play', methods=['GET', 'POST'])
def play_menu():
    score = 1
    forms = Answer()
    example = gen.Example(change=[current_user.class_user, current_user.level])
    if forms.validate_on_submit():
        answer = forms.answer.data
        if answer == current_user.last_answer:
            if int(current_user.level) == 1:
                score = 1
            elif int(current_user.level) == 2:
                score = 3
            elif int(current_user.level) == 3:
                score = 5
            current_user.score += score
            db.session.commit()
            return redirect(url_for('play_menu'))
        else:
            flash('Это был неправильный ответ.')
            return redirect(url_for('play_menu'))
    else:
        example.gen_ex()
        current_user.last_answer = example.result
        db.session.commit()
    return render_template('math/play.html', title='Game', form=forms, example=example.str_example)


@app.route('/game/math/settings', methods=['GET', 'POST'])
def settings():
    forms = Settings()
    if forms.validate_on_submit():
        nick = forms.username.data
        existing_user = Users.query.filter_by(username=nick).first()
        if existing_user:
            flash('Человекс с таким именем уже есть')
        else:
            if nick != '':
                current_user.username = nick
                db.session.commit()
        level = forms.level.data
        class_user = forms.clas.data
        if class_user != '':
            if 5 <= int(class_user) <= 6:
                current_user.class_user = class_user
            else:
                flash('Доступны только 5е и 6е классы')
        if level != '':
            if 1 <= int(level) <= 3:
                current_user.level = level
            else:
                flash('Доступны только 1-3 уровни')
            db.session.commit()
        return redirect(url_for('homepage'))
    return render_template('math/settings.html', title='Настройки', form=forms)


@app.route('/user/<string:nick>')
def user(nick):
    user = Users.query.filter_by(username=nick).first()
    if 0 <= user.score < 100:
        rank = 'iron.png'
        rank_name = 'Железо'
    elif 100 <= user.score < 300:
        rank = 'bronze.png'
        rank_name = 'Бронза'
    elif 300 <= user.score < 500:
        rank = 'silver.png'
        rank_name = 'Серебро'
    elif 500 <= user.score < 1000:
        rank = 'gold.png'
        rank_name = 'Золото'
    elif 1000 <= user.score < 2000:
        rank = 'platium.png'
        rank_name = 'Платина'
    elif 2000 <= user.score < 3000:
        rank = 'diamond.png'
        rank_name = 'Алмаз'
    elif 3000 <= user.score < 5000:
        rank = 'master.png'
        rank_name = 'Мастер'
    elif 5000 <= user.score < 10000:
        rank = 'gr_master.png'
        rank_name = 'Гранд-мастер'
    elif user.score >= 10000:
        rank = 'legend.png'
        rank_name = 'Легенда'
    else:
        rank = ''
        rank_name = ''
    return render_template('math/user.html', title=nick, user=user, rank=rank, rank_name=rank_name)


@app.route('/game/math/rating')
def rating_math():
    users = Users.query.order_by(Users.score.desc()).all()[0:10]
    return render_template('math/rating.html', title="Rating", users=users)


@app.route('/game/snake')
def snake():
    return render_template('game/snake.html')


if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
