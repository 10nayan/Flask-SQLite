from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///interview.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        nationality = request.form.get("nationality")
        birthplace = request.form.get("birthplace")
        print(name, age)
        try:
            new_person = Person(name = name, age = age, nationality_id = nationality, birthplace = birthplace)
            db.session.add(new_person)
            db.session.commit()
        except Exception as e:
            return str(e)
        return redirect(url_for('index'))
    all_persons = Person.query.all()
    print(all_persons)
    return render_template("index.html", persons = all_persons)

@app.route("/delete/<int:id>", methods = ["GET"])
def delete(id):
    try:
        person = db.query.get(id)
        db.session.delete(person)
        db.session.commit()
        return redirect(url_for("index"))
    except:
        return jsonify({"message": "Something unexpected happened"})
    
@app.route("/update/<int:id>", methods = ["POST"])
def update(id):
    try:
        person = db.query.get(id)
        name = request.form.get("name")
        age = request.form.get("age")
        nationality = request.form.get("nationality")
        birthplace = request.form.get("birthplace")
        new_person = Person(name = name, age = age, nationality_id = nationality, birthplace = birthplace)
        db.session.delete(person)
        db.session.add(new_person)
        db.session.commit()
        return redirect(url_for("index"))
    except:
        return jsonify({"message": "Something unexpected happened"})
    

if __name__ == "__main__":
    app.run(debug = True)