from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    app.app_context().push()
    db.app = app
    db.init_app(app)


class Meal(db.Model):
    __tablename__ = "meals"

    name = db.Column(db.Text, primary_key=True)
    description = db.Column(db.Text, primary_key=True)

    def serialize(self):
        return {
            "name": self.name,
            "description": self.description
        }
