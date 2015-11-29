from flask import Flask
from flask import request
from flask import jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps
from collections import OrderedDict
import aiml
import base64
import json
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
        name = request.values['name']
        phno = request.values['phno']
        aadhaar=request.values['aadhaar']
        address=request.values['address']
        email = request.values['email']
        YOB = request.values['YOB']
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
            db.session.add(User(name, aadhaar ,phno, YOB, address, email))
            db.session.commit()
            return jsonify({"message": "User registration successful", "status": 200})
    else:
        return jsonify({"message": "Please provide all the information", "status": 401}), 401

@app.route('/upload_docs/signature',methods=['POST','GET'])
def upload():
    docs=json.loads(request.get_json())
    signature=str(docs['signature'])
    aadhaar=str(docs['aadhaar'])
    user=db.session.query(User).filter(User.aadhaar==aadhaar).all()
    s=open("Doc/Sig"+str(user[0].id)+".jpg","w")
    s.write(base64.decodestring(signature))
    s.close()


    db.session.add(Documents(user[0].id,"Doc/Sig"+str(user[0].id)+".jpg","0"))
    db.session.commit()
    return jsonify({"message":"Successfully Uploded","status": 200})


@app.route('/upload_docs/profilepic',methods=['POST','GET'])
def upload():
    docs=json.loads(request.get_json())

    profilepic=str(docs['profilepic'])
    aadhaar=str(docs['aadhaar'])
    user=db.session.query(User).filter(User.email==email).all()
    s=open("Doc/Sig"+str(user[0].id)+".jpg","w")
    s.write(base64.decodestring(profilepic))
    s.close()


    db.session.add(Documents(user[0].id," ","Doc/DP"+str(user[0].id)+".jpg"))
    db.session.commit()
    return jsonify({"message":"Successfully Uploded","status": 200})

@app.route('/aichat',methods=['POST','GET'])
def aichat():
    kernel=aiml.Kernel()
    kernel.learn("basic_chat.xml")
    Q=json.loads(request.get_json())
    Query=str(Q['Query'])
    return jsonify({"Answer":kernel.respond(Query.upper()),"status":200})

@app.route('/update_address',methods=['POST','GET'])
def update_address():

    content=json.loads(request.get_json())

    aadhaar=str(content['aadhaar'])
    newaddress=str(content['naddress'])
    user=db.session.query(User).filter(User.email==email).all()
    user[0].address=newaddress
    db.session.commit()
    return jsonify({"message":"Successfully Updated","flag":"0","status": 200})

if __name__ == '__main__':
    app.run( port=7000)
