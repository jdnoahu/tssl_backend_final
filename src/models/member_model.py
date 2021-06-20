from src.common import db, ma


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), unique=False)
    last_name = db.Column(db.String(100), unique=False)
    sobriety_date = db.Column(db.String(100), unique=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(144), unique=False)

    def __init__(self, first_name, last_name, sobriety_date, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.sobriety_date = sobriety_date
        self.email = email
        self.password = password


class MemberSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name',
                  'sobriety_date', 'email', 'password')
