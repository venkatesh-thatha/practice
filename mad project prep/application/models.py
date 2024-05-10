from application.database import db

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True,auto_increment=True)
    name=db.Column(db.String(80),nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone=db.Column(db.String(10),unique=True,nullable=False)
    password = db.Column(db.String(80), nullable=False)
    address=db.Column(db.String(120),nullable=False)
    role=db.Column(db.String(80),nullable=False,default='customer')


def __init__(self, name, username, email,phone,password,address,role):
    self.name=name
    self.username = username
    self.email = email
    self.phone=phone
    self.password = password
    self.address=address
    self.role=role

    
    def __repr__(self):
        return '<User %r>' % self.username