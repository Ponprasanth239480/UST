from flask import Flask, jsonify, render_template,request, redirect,  session, url_for,Response
from flask_pymongo import PyMongo
import pymongo

app = Flask(__name__)

client= pymongo.MongoClient('mongodb://localhost:27017')
client.server_info()
db = client['users']
collection = db['userlogin']
collection1 = db['foodorder']


@app.route('/', methods = ["GET","POST"])
def loginpage():
    if request.method=="POST":
        uname = collection.find_one({'mailID':request.form['uname']})
        psw = collection.find_one({'password':request.form['psw']})
        if uname:
            if psw:
                return redirect("/both")
                #return render_template('both.html')
            else:
                return redirect("/")
        else:
                return redirect("/")        
                 
    return render_template('login.html')


@app.route('/register', methods = ["GET","POST"])
def registerpage():
    if request.method=="POST":
        mailID=request.form.get('email')
        password=request.form.get('psw')
        confirm_password=request.form.get('psw-repeat')
            
        if password==confirm_password:
            collection.insert_one({'mailID':mailID,'password':password,'confirm_password':confirm_password})
            return redirect("/")
        else:
            return "incorrect password"
    
    
    return render_template('registration.html')



@app.route('/both', methods = ["GET","POST"])
def bookpage():
    if request.method=="POST":
        table=request.form.get('table')
        name=request.form.get('name')
        seater=request.form.get('seater')
        food=request.form.get('food')
        collection1.insert_one({'table':table,'name':name,'seater':seater,'food':food})
        bookings = collection1.find({})
        return render_template('both.html',bookings=bookings)
        #return redirect('/next',bookings=bookings)
    else:
        return render_template('both.html')





if __name__ == "__main__":
    # change the port number 
    app.run(debug=True, port=8080)