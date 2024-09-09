from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired


class Language(FlaskForm):
    language = SelectField('Choose Language', choices=[('en', 'English'), ('es', 'Spanish'), ('de', 'German'), ('it', 'Italian'), ('ru', 'Russian')], validators=[DataRequired()])
    submit = SubmitField('Get Joke')

  