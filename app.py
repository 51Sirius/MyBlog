from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html', title='Blog')


@app.route('/favorites')
def favorites():
    return render_template('favorites.html', title='Favorites')


if __name__ == '__main__':
    app.run()
