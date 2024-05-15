from flask_wtf import FlaskForm
from app.models import User
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, ValidationError

class RegistrationForm(FlaskForm):
    def validate_nome(self, check_user):
        user = User.query.filter_by(nome=check_user.data).first()
        if user:
            raise ValidationError("Usuário já existe! Cadastre outro nome de usuário")

    def validate_email(self, check_email):
        email = User.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError("Email já existe! Cadastre outro email")

    username = StringField(label='Username', render_kw={"placeholder": "Username"}, validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField(label='Email', render_kw={"placeholder": "Email"}, validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', render_kw={"placeholder": "Password"}, validators=[DataRequired(), Length(min=4, message="A senha deve ter no mínimo 4 caracteres.")])
    submit = SubmitField(label='Register')
    
    
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    senha = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')


