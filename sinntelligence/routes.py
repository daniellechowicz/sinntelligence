from flask import flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sinntelligence import app
from sinntelligence.database import db
from sinntelligence.helpers import allowed_file
from sinntelligence.models import Image
from werkzeug.utils import secure_filename
import os


@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/dashboard")
@login_required
def dashboard():
    # Get all images belonging to current user.
    user_images_root = os.path.join(
        app.config["IMAGES_SAVE_DIRECTORY"], current_user.username
    )

    # Check whether the directory exists.
    if os.path.exists(user_images_root):
        filenames = os.listdir(user_images_root)
        paths = [
            os.path.join("images", current_user.username, filename)
            for filename in filenames
        ]
        return render_template(
            "dashboard.html", username=current_user.username, paths=paths
        )

    return render_template("dashboard.html", username=current_user.username)


@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    if request.method == "POST":
        files = request.files.getlist("file")
        for file in files:
            if file.filename == "":
                return redirect(request.url)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)

                # Create a folder for the current user if it does not exist.
                user_directory = os.path.join(
                    app.config["IMAGES_SAVE_DIRECTORY"], current_user.username
                )
                if not os.path.exists(user_directory):
                    os.mkdir(user_directory)

                # Save the file.
                path = os.path.join(user_directory, filename)
                file.save(path)

                # Commit to the database.
                image = Image(username=current_user.username, name=filename, path=path)
                db.session.add(image)
                db.session.commit()

        return redirect(url_for("dashboard"))

    return render_template("upload.html", name=current_user.username)


@app.route("/image/<int:id>")
def image(id):
    # Get all images belonging to current user.
    user_images_root = os.path.join(
        app.config["IMAGES_SAVE_DIRECTORY"], current_user.username
    )

    # Check whether the directory exists.
    if os.path.exists(user_images_root):
        filenames = os.listdir(user_images_root)
        paths = [
            os.path.join("images", current_user.username, filename)
            for filename in filenames
        ]
        return render_template("image.html", path=paths[id - 1])

    return render_template("image.html")
