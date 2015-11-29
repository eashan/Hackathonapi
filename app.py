from flask import Flask
from flask import request
from flask import jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps
from collections import OrderedDict
import aiml
import base64
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

@app.route('/upload_docs',methods=['POST','GET'])
def upload():
    signature=request.values['signature']
    profilepic=request.values['profilepic']
    email=request.values['email']
    user=db.session.query(User).filter(User.email==email).all()
    s=open("Doc/Sig"+str(user[0].id)+".jpg","w")
    s.write(base64.decodestring(signature))
    s.close()
    p=open("Doc/DP"+str(user[0].id)+".jpg","w")
    p.write(base64.decodestring(profilepic))
    p.close()

    db.session.add(Documents(user[0].id,"Doc/Sig"+str(user[0].id)+".jpg","Doc/DP"+str(user[0].id)+".jpg"))
    db.session.commit()
    return jsonify({"message":"Successfully Uploded","status": 200})

@app.route('/aichat',methods=['POST','GET'])
def aichat():
    kernel=aiml.Kernel()
    kernel.learn("basic_chat.xml")
    Query=request.values['Query']
    return jsonify({"Answer":kernel.respond(Query),"status":200})

@app.route('/update_address',methods=['POST','GET'])
def update_address():
    email=request.values['email']
    newaddress=request.values['naddress']
    user=db.session.query(User).filter(User.email==email).all()
    user[0].address=newaddress
    db.session.commit()
    return jsonify({"message":"Successfully Updated","status": 200})

if __name__ == '__main__':
    app.run()
