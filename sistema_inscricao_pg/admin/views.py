from flask import Blueprint, render_template, redirect, url_for, request, session
from sistema_inscricao_pg.models import Admin, Palestra, Inscricao
from sistema_inscricao_pg import db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = Admin.query.filter_by(username=username, password=password).first()
        if admin:
            session['admin_logged_in'] = True
            return redirect(url_for('admin.dashboard'))
    return render_template('admin/login.html')

@admin_bp.route('/dashboard')
def dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin.login'))
    palestras = Palestra.query.all()
    inscricoes = Inscricao.query.all()
    return render_template('admin/dashboard.html', palestras=palestras, inscricoes=inscricoes)

