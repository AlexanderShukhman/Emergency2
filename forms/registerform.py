from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from forms.geo_validators import  AddressRequired


class RegisterForm(FlaskForm):
    email = EmailField('Электронная почта', validators=[DataRequired(message="Поле 'почта' не может быть пустым")])
    password = PasswordField('Пароль', validators=[DataRequired(message="Поле 'пароль' не может быть пустым")])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired(message="Поле 'пароль' не может быть пустым")])
    name = StringField('Имя оператора', validators=[DataRequired(message="Поле 'имя' не может быть пустым")])
    surname = StringField('Фамилия оператора', validators=[DataRequired(message="Поле 'фамилия' не может быть пустым")])
    locality = StringField('Район обслуживания вызовов', validators=[DataRequired(message="Поле 'район' не может быть пустым"), AddressRequired(unique=True)])
    position = StringField('Должность')
    submit = SubmitField('Зарегистрироваться')


