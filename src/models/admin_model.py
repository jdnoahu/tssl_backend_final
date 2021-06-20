from src.common import db, ma


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=False)
    password = db.Column(db.String(144), unique=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password


class AdminSchema(ma.Schema):
    class Meta:
        fields = ('email', 'password')
