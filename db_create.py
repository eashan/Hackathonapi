from app import db
from models import User


#create the database and db tables
db.create_all()

#demo insert statements
db.session.add(User("eashankadam","aadhaar123","9920875281","1994","12,Sampada Building, Bhagatlane, Matunga Mumbai 400016","eashankadam@gmail.com"))


#commit changes

db.session.commit()