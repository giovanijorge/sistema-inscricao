from flask import Flask, render_template, request, redirect
import random
from datetime import datetime
import psycopg2
import os

app = Flask(__name__)

# Conexão com o banco de dados Render
DATABASE_URL = os.getenv("DATABASE_URL") or "postgresql://admin:senha@host/sistema_inscricao"

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route("/inscricao", methods=["GET", "POST"])
def inscricao():
    versao = request.args.get("v") or random.choice(["A", "B"])  # Escolhe aleatoriamente ou via query string

    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        data_hora = datetime.now()

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO inscricoes (nome, email, telefone, data_hora, versao)
            VALUES (%s, %s, %s, %s, %s)
        """, (nome, email, telefone, data_hora, versao))
        conn.commit()
        cur.close()
        conn.close()

        return redirect("/obrigado")

    # Renderiza o formulário apropriado
    template = "form_ab.html" if versao == "A" else "form_b.html"
    return render_template(template)
