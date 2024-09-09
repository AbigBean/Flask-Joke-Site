from app import app
from flask import render_template, redirect, url_for, request
from app.pyjokes import generate_joke
from app.forms import Language






@app.route('/', methods=["GET", 'POST'])
def index():
    selected_language = request.form.get('language', 'en')

    form = Language()
    form.language.data = selected_language
    if form.validate_on_submit():
        language = form.language.data
        return redirect(url_for('joke', language=language))

    return render_template('index.html', title="Get a Joke", form=form)


@app.route('/joke/<language>')
def joke(language):
    form = Language()
    joke = generate_joke(language)
    form.language.data = language
    return render_template('index.html', title="Get a Joke", form=form, joke=joke)