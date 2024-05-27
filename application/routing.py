from flask import render_template, redirect, request, url_for, flash

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

# Маршрут для обработки входа в админ-панель
@app.route("/admin", methods=["POST"])
def admin_login():
    password = request.form.get("password")
    if password == "1231":
        return redirect(url_for("admin_panel"))
    else:
        flash("Неверный пароль")
        return redirect(url_for("main"))

# Маршрут для админ-панели
@app.route("/admin/panel", methods=["GET", "POST"])
def admin_panel():
    if request.method == "POST":
        # Получение данных из формы
        number = request.form['number']
        name = request.form['name']
        desc = request.form['desc']
        image_path = request.form.get('image_path', '')
        status = request.form['status']
        target = request.form['target']
        dataStart = request.form['dataStart']
        country = request.form['country']
        massa = request.form['massa']

        # Создание нового спутника
        new_satellite = Satellites(
            number=number,
            name=name,
            desc=desc,
            image_path=image_path,
            status=status,
            target=target,
            dataStart=dataStart,
            country=country,
            massa=massa
        )

        # Добавление спутника в сессию и сохранение в базе данных
        db.session.add(new_satellite)
        db.session.commit()

        # Перенаправление на страницу администратора
        return redirect(url_for("admin_panel"))

    # Получение всех спутников из базы данных
    satellites = Satellites.query.all()
    return render_template("admin_panel.html", data=satellites)

# Маршрут для удаления спутника
@app.route("/admin/delete/<int:satellite_id>", methods=["POST"])
def delete_satellite(satellite_id):
    satellite = Satellites.query.get_or_404(satellite_id)
    db.session.delete(satellite)
    db.session.commit()
    return redirect(url_for("admin_panel"))



