from flask_sqlalchemy import SQLAlchemy
from models import *
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///interview.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()

