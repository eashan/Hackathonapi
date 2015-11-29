from app import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class User(db.Model):

    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    phno=db.Column(db.String(20),nullable=False)
    aadhaar = db.Column(db.String(20),nullable=True)
    address = db.Column(db.String(400),nullable=True)
    email = db.Column(db.String(200), unique=True, nullable=False)
    YOB=db.Column(db.String(20),nullable=True)
    documents=relationship("Documents",backref="User")

    def __init__(self, name, aadhaar ,phno, YOB, address, email):
        self.name= name
        self.aadhaar = aadhaar
        self.address = address
        self.phno = phno
        self.YOB= YOB
        self.email = email


    def __repr__(self):
        return '<name {} >'.format(self.name)

class Documents(db.Model):

    __tablename__="Documents"

    id=db.Column(db.Integer,primary_key=True)
    signature=db.Column(db.String(100),nullable=True)
    profilepic=db.Column(db.String(100),nullable=True)
    empid=db.Column(db.Integer,ForeignKey('User.id'))


    def __init__(self,empid,profilepic,signature):
        self.signature=signature
        self.profilepic=profilepic
        self.empid=empid


    def __repr__(self):
        return '<empid {}>'.format(self.empid)