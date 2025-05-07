from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import Inscricao

main = Blueprint('main', __name__)

@main.route('/inscrever', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        inscricao = Inscricao(nome=nome, email=email, telefone=telefone)
        db.session.add(inscricao)
        db.session.commit()
        flash('Inscrição realizada com sucesso!')
        return redirect(url_for('main.index'))
    return render_template('form_ab.html')
