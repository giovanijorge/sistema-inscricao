from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:Tf8TM3VaBH2RrYgFEjTFMNWm85PHNViZ@dpg-d0d74p1r0fns73848j80-a/sistema_inscricao'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'senha_padrao'
    from sistema_inscricao_pg.admin.views import admin_bp
app.register_blueprint(admin_bp)


    db.init_app(app)
    migrate.init_app(app, db)

    from .views import main
    app.register_blueprint(main)

    return app
