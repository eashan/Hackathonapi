from app import db
from models import User


#create the database and db tables
db.create_all()

#demo insert statements
db.session.add(User("eashan","kadam","aadhaar123","12,Sampada Building, Bhagatlane, Matunga Mumbai 400016","eashankadam@gmail.com","pass"))


#commit changes

db.session.commit()