from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Создание экземпляра приложения Flask
app = Flask(__name__)

# Настройка URI для подключения к базе данных SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///base.db"

# Инициализация экземпляра SQLAlchemy с использованием приложения Flask
db = SQLAlchemy(app)

# Импорт моделей данных и маршрутов
from application import models, routing

# Создание всех таблиц в базе данных
with app.app_context():
    db.create_all()

# Запуск приложения в режиме отладки
app.run(debug=True)
