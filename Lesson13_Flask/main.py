from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g, make_response
import sqlite3
import os
from FDataBase import FDataBase
from werkzeug.security import generate_password_hash, check_password_hash
from UserLogin import UserLogin
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config["SECRET_KEY"] = "dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf"
app.config.from_object(__name__)

MAX_CONTENT_LENGTH = 1024 * 1024

DATABASE = "/tmp/flsite.db"
DEBUG = True
# SECRET_KEY = "dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf"

app.config.update(dict(DATABASE=os.path.join(app.root_path, "flsite.db")))

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Авторизуйтесь"
login_manager.login_message_category = "success"


@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().fromdb(user_id, dbase)


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource("sq_db.sql", mode='r') as file:
        db.cursor().executescript(file.read())
    db.commit()
    db.close()


menu = [{"name": "Установка", "url": "install"},
        {"name": " Первое приложение", "url": "app"},
        {"name": "Обратная связь", "url": "contact"}]


def get_db():
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db


dbase = None


# TODO хендлер который срабатывает в первый запроса
@app.before_request
def before_request():
    global dbase
    db = get_db()
    dbase = FDataBase(db)


# TODO хендлер который срабатывает в первый запроса


@app.route("/")
def index():
    # TODO сессии и как с ними работать
    # if 'visits' in session:
    #     session['visits'] = session.get('visits') + 1
    # else:
    #     session['visits'] = 1
    # return f"ты посмотрел сайт : {session['visits']}"
    # TODO сессии и как с ними работать

    print(url_for('index'))
    return render_template("index.html", menu=dbase.getMenu(), posts=dbase.getPostsAnonce())


@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    if request.method == "POST":
        user = dbase.getUserByEmail(request.form['email'])
        if user and check_password_hash(user['psw'], request.form['psw']):
            userlogin = UserLogin().create(user)
            rm = True if request.form.get('remainme') else False
            login_user(userlogin, remember=rm)
            return redirect(request.args.get("next") or url_for('profile'))
        flash("Неверная пара логин/пароль", "error")
    return render_template("login.html", menu=dbase.getMenu(), title="Авторизация")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['email']) > 4 and len(request.form['psw']) > 4 and \
                request.form['psw'] == request.form['psw2']:
            hash = generate_password_hash(request.form['psw'])
            res = dbase.addUser(request.form['name'], request.form['email'], hash)
            if res:
                flash("Вы успешно зарегистрированы", "success")
                return redirect(url_for('login'))
            else:
                flash("Ошибка при добавлении в БД", "error")
        else:
            flash("Неверно заполнены поля", "error")
    return render_template("register.html", menu=dbase.getMenu(), title="Регистрация")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Вы вышли из аккаунта", "success")
    return redirect(url_for('login'))


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html", menu=dbase.getMenu(), title="Профиль")
    #     f"""<p><a href="{url_for('logout')}"> Выйти из профиля </a>
    # <p>user info: {current_user.get_id()} """


@app.route("/userava")
@login_required
def userava():
    img = current_user.getAvatar(app)
    if not img:
        return ""

    h = make_response(img)
    h.headers['Content-Type'] = 'image/png'
    return h


@app.route('/upload', methods=["POST", "GET"])
@login_required
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and current_user.verifyExt(file.filename):
            try:
                img = file.read()
                res = dbase.updateUserAvatar(img, current_user.get_id())
                if not res:
                    flash("Ошибка обновления аватара", "error")
                    return redirect(url_for('profile'))
                flash("Аватар обновлён", "success")
            except FileNotFoundError as error:
                flash("Ошибка чтения", "error")
        else:
            flash("Ошибка обновления аватара", "error")
    return redirect(url_for('profile'))


# TODO cookies
# @app.route("/login")
# def login():
#     log = ""
#     if request.cookies.get('logged'):
#         log = request.cookies.get('logged')
#
#     res = make_response(f"<h1>Форма авторизации</h1><p>logged: {log}")
#     res.set_cookie("logged", "yes")
#     return res
#
# # TODO очистка cookies
# @app.route("/logout")
# def logout():
#     res = make_response(f"<h1>Вы больше больше не авторизованы < /h1>")
#     res.set_cookie("logged", "", 0)
#     return res
# TODO cookies


# TODO хендлер который срабатывает в конце запроса
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "kink_db"):
        g.link_db.close()


# TODO хендлер который срабатывает в конце запроса

@app.route("/add_post", methods=["POST", "GET"])
def addPost():
    if request.method == "POST":
        if len(request.form["name"]) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['url'], request.form['post'])
            if not res:
                flash("Ошибка добавления", category='error')
            else:
                flash("Успешно", category='success')
        else:
            flash("Ошибка добавления", category='error')

    return render_template("add_post.html", menu=dbase.getMenu(), title="ДОбавлнеие статьи")


# TODO Обработка POST запроса и быстрым ответам пользователю о выполненной или не выполненной задаче
# @app.route("/contact", methods=["POST", "GET"])
# def contact():
#     if request.method == "POST":
#         if len(request.form["username"]) > 2:
#             flash("Сообщение отправлено", category='success')
#         else:
#             flash("Сообщение не отправлено", category='error')
#
#     return render_template("contact.html", title="Обратная связь", menu=menu)
# TODO Обработка POST запроса и быстрым ответам пользователю о выполненной или не выполненной задаче

@app.route("/post/<alias>")
@login_required
def showPost(alias):
    title, post = dbase.getPost(alias)
    if not title:
        abort(404)
    return render_template('post.html', menu=dbase.getMenu(), title=title, post=post)


#
# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if "userlogin" in session:
#         return redirect(url_for('profile', username=session['userlogin']))
#     elif request.method == "POST" and request.form['username'] == "admin" and request.form['psw'] == '123':
#         session['userlogin'] = request.form['username']
#         return redirect(url_for('profile', username=session['userlogin']))
#     return render_template('login.html', title="Авторизация", menu=menu)

# TODO обратка ошибок и изменение их значений с возможным перенаправлением на друге url
# @app.errorhandler(404)
# def page_note_found(error):
#     return render_template('page404.html', title="Страница не найдена", menu=menu), 404
# TODO обратка ошибок и изменение их значений с возможным перенаправлением на друге url

# @app.route("/profile/<username>")
# def profile(username):
#     if 'userlogin' not in session or session["userlogin"] != username:
#         abort(401)
#     return f"Пользователь: {username}"
# #


# TODO простой отлов url c обработкой через Html страницу и передачей аргумента в виде меню и title
# @app.route("/about")
# def about():
#     print(url_for('about'))
#     return render_template("about.html", title="О сайте", menu=menu)
# TODO простой отлов url


# TODO просмотр как работает url запрос без запуска сервера
# with app.test_request_context():
#     print(url_for('about'))
# TODO просмотр как работает url запрос без запуска сервера
if __name__ == '__main__':
    app.run(debug=True)
