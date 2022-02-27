from sinntelligence import app
from sinntelligence.database import db
from sinntelligence.forms import LoginForm, RegisterForm
from sinntelligence.models import User
from flask import redirect, render_template, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_required, login_user, logout_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # Check if username exists in the database.
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            return render_template(
                "register.html", form=form, error="Selected username is already taken."
            )

        # Check if e-mail address exists in the database.
        email = User.query.filter_by(email=form.email.data).first()
        if email:
            return render_template(
                "register.html",
                form=form,
                error="Selected e-mail address exists in the database.",
            )

        # Encrypt the password (privacy-related issues).
        hashed_password = generate_password_hash(form.password.data, method="sha256")

        new_user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()

        # Sharing the information between different URLs.
        session["message"] = "User created successfully. Welcome on board!"

        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    # Read and clean immediately (so that it does not appear again).
    try:
        message = session["message"]
        session["message"] = ""
    except:
        message = ""

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect(url_for("dashboard"))
        return render_template(
            "login.html",
            form=form,
            error="Invalid username or password. Please try again.",
        )

    return render_template("login.html", form=form, message=message)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))
