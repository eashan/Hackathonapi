from flask import Flask
from flask import request
from flask import jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps
from collections import OrderedDict


from flask.ext.bcrypt import Bcrypt
# create the application object
app = Flask(__name__)

# config
app.secret_key = 'my precious'

#config
app.config['DEBUG'] = True

app.config.from_object('config.DevelopmentConfig')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:eashanrocks@localhost/KnowYC'

#create sqlalchemy object

db=SQLAlchemy(app)




from models import *





@app.route('/register', methods=['POST','GET'])
def register():
    if 'name' in request.values and 'email' in request.values and 'password' in request.values:
        fname = request.values['fame']
        lname = request.values['lname']
        aadhaar=request.values['aadhaar']
        address=request.values['address']
        email = request.values['email']
        password = request.values['password']
        if email == "" or password == "" or name == "":
            return jsonify({"message": "Please provide all the information", "status":401}), 401
        results = db.session.query(User).filter(User.email == email).all()
        if results:
            if results:
                user = db.session.query(User).filter(User.email == email, User.password == password).all()
                if user:
                    return jsonify({"message": "User registration successful", "status": 200})
                else:
                    return jsonify({"message": "Authentication error", "status": 401}), 401
        else:
            db.session.add(User(fname,lname,aadhaar,address,email, password))
            db.session.commit()
            return jsonify({"message": "User registration successful", "status": 200})
    else:
        return jsonify({"message": "Please provide all the information", "status": 401}), 401

#@app.route('/upload',method=['POST'])
#def upload():

if __name__ == '__main__':
    app.run()
