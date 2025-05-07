from flask import Flask
from sistema_inscricao_pg import create_app

app = create_app()

if __name__ == '__main__':
  app = Flask(__name__)

