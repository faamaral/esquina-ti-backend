from flask import Blueprint, url_for, redirect, request, flash, render_template
from flask_login import current_user, login_required, login_user, logout_user
from flask_wtf import FlaskForm

from flask_admin import AdminIndexView, expose, helpers
from werkzeug.urls import url_parse
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email
from app.models import User

auth_admin = Blueprint('auth_admin', __name__)

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email('Enter with a valid email address')])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

@auth_admin.route('/admin/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated and current_user.admin:
        return redirect(url_for('admin.index'))
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash("Email ou senha invalidos")
            return redirect(url_for('auth_admin.login'))
        if user.admin is False:
            flash("Usuário não administrador")
            return redirect(url_for('auth_admin.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('admin.index')
            return redirect(next_page)
    return render_template('login.html', title="Entrar", form=form)

@auth_admin.route('/admin/logout')
def logout():
    logout_user()
    return redirect(url_for('admin.index'))



