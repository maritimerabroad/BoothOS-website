
#Licenced under the GPLv2


#IMPORTS
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


#APP SETUP
app = Flask(__name__)
app.config["DEBUG"] = True


#DATABASE SETUP
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="maritimerabroad",
    password="Iamwealthy1",
    hostname="maritimerabroad.mysql.pythonanywhere-services.com",
    databasename="maritimerabroad$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#MODELS
class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))


#REST OF THE APP
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=Comment.query.all())

    comment = Comment(content=request.form["contents"])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))

