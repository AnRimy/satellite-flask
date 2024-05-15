from flask import render_template, redirect, request

# Импорт приложения и базы данных
from application import app, db

# Импорт моделей данных
from application.models import Satellites

# Маршрут для главной страницы
@app.route("/")
def main():
    # Получение всех спутников из базы данных
    model = Satellites.query.all()
    # Отображение главной страницы с данными о спутниках
    return render_template("main.html", satellites=model)

# Маршрут для страницы с деталями спутника
@app.route("/satellite/<int:satellite_number>")
def satellite_details(satellite_number):
    # Поиск спутника по номеру в базе данных
    satellite = Satellites.query.filter_by(number=satellite_number).first()
    # Отображение страницы с деталями выбранного спутника
    return render_template("satellite.html", satellite=satellite)
