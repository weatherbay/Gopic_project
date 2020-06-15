from flask import Flask, render_template, flash,redirect,\
    url_for,session,logging,request,g,session, send_file
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SubmitField
from flask_wtf.file import FileField
from flask_wtf import Form
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from datetime import datetime
from flask_sessionstore import Session
import os
from base64 import b64encode






app = Flask(__name__)




env = 'dev'
if env == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pic.db'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  


#table for score
class pictable(db.Model):
    id =db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.VARCHAR(100),unique=True)
    image = db.Column(db.LargeBinary)
    entrytime = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    

    def __init__(self,name,image):
        self.name = name
        self.image = image
        



@app.route('/')
def index():
    return render_template('main.html')

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        name=request.form.get('name')
        photo = request.files['photo']
        data = pictable(name=name,image=photo.read())
        db.session.add(data)
        db.session.commit()
        flash('pic submitted','success')
        return redirect(url_for('view'))
          
    return render_template('register.html')

@app.route('/view',methods=['GET','POST'])
def view():
    if request.method =='POST':
        name = request.form['name']
        #connect to database
        data = pictable.query.filter_by(name=name).first()
        if name:
            
            ide = data.id
           
            
            
            
            

            #create login session
            session['logged_in'] = True
            session['name'] = name
            session['id'] = ide
            
            
            return redirect(url_for('view2'))
            
                
            
        else:
            error = 'invalid name'
            return render_template('view.html',error=error)
    return render_template('view.html')
    
@app.route('/view2')
def view2():
    name = session['name']
    data = pictable.query.filter_by(name=name).first()
    img = b64encode(data.image).decode("utf-8")
    
    return render_template('view2.html',data=data,img=img)


   


if __name__ == '__main__':
    app.secret_key='secret54678'
    app.run()