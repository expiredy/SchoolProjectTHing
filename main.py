from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_ngrok import run_with_ngrok
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField
from data.ConstantPhrases import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'expiredy_key'


@app.route("/")
def distribution_page():
    return redirect("/login")

@app.route("/login")
def login_page():
    return render_template("login.html")


@app.route("/profile")
def page_of_grade():
    return render_template("profile.html")

@app.route("/home")
def home_page():
    lessons = {}
    return render_template("home_page.html", HomeWorkTitle=MotivationPhrase, lessons=lessons, list=list)

@app.route("/chat")
def chat_paqe():
    return render_template("chat_page.html")

def main():
    run_with_ngrok(app)
    app.run()

"""
Моя цель - создать удобный в использовании сайт для обмена информацией между школьниками и их учителями:
1. Странички, котрые я хочу реализовать:
    1.1 Страница со входом (регестрации не будет, т.к. всю информацию в базу данных должны заносить работники школы или министерства образования)
    1.2 Главная страинчка, на которой, в сокращённом виде будет выводиться информация с остальных страниц, находятся ссылки на страницы
    1.3 Страница профиля ученика, который может настраивать свои данные вроде номера телефона, электронной почты, которые будут заноситься в базу данных
    1.4 Старица класса, где будут находиться: ссылка на чат и важная информация
    1.5 Страничка с рассписанием, домашними заданиями и оценками ученика.
    1.6 Страничка с подробным описанием урока (кабинет, тема котору. будут проходить на уроке и ссылка на профиль учителя
2. Технологии которые я хочу использовать:
    2.1 SQLite для хранения данных
    2.2 Flask для облегчённой работы на сервере
3. А что же по базам данных?
    3.1 Таблица всех юзеров с их личной информацией и уровнем доступа к редактированию или взаимодействию со страницами
    3.2 Данные из чатов
    3.1 База данных с уроками и домашними заданиями 
    3.1 База данных с оценками учеников 
"""

if __name__ == '__main__':
    main()
