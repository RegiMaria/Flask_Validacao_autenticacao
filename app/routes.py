from flask import render_template, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required
from app.forms import RegistrationForm, LoginForm
from app.models import User
from app import app, db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        novo_usuario = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Usuário cadastrado com sucesso!', category='success')
        return redirect(url_for('user'))  
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = User.query.filter_by(email=form.email.data).first()
        if usuario and usuario.verificar_senha(form.senha.data):
            login_user(usuario)
            flash(f"Sucesso! Seu usuário é {usuario.username}", category="success")
            return redirect(url_for('user'))  # Redireciona para a página inicial após o login bem-sucedido
        else:
            flash("Usuário ou senha incorretos. Por favor, tente novamente.", category="danger")
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required  # Exige que o usuário esteja autenticado para acessar essa rota
def logout():
    logout_user()
    flash('Você saiu com sucesso.', category='success')
    return redirect(url_for('index'))

@app.route('/user')
def user():
    return render_template('user.html')