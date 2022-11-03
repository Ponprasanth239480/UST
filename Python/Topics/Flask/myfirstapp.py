# Import Flask class
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///products.db"

#database instance
db = SQLAlchemy(app)

class MyProduct(db.Model):
    productid = db.Column(db.Integer, primary_key = True)
    product = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.productid}-{self.product}-{self.desc}"

# @ - Decorators in Python to tell flask what URL should trigger our function
@app.route('/', methods =["GET","POST"])
def hello_world():
    if request.method == "POST":
        productid = request.form['productid']
        product = request.form['product']
        desc = request.form['desc']
    
        product=MyProduct(productid=productid,product=product,desc=desc)
        db.session.add(product)
        db.session.commit()

    allProducts = MyProduct.query.all()
    return render_template('index.html', allProducts = allProducts)
    #return "<p>Welcome to Flask</p>"

@app.route('/show')
def Clothing():
    allProducts = MyProduct.query.all()
    print(allProducts)
    return "<p>This is Clothing Page</p>"

@app.route('/delete/<int:productid>')
def delete(productid):
    allProducts = MyProduct.query.filter_by(productid = productid).first()
    db.session.delete(allProducts)
    db.session.commit()
    print(allProducts)
    # Redirects the page to Home Page
    return redirect("/")

# Endpoint for update existing records using product id
@app.route('/update/<int:productid>', methods = ["GET","POST"])
def update(productid):
    if request.method=='POST':
        productid = request.form['productid']
        product = request.form['product']
        desc = request.form['desc']
        allProducts = MyProduct.query.filter_by(productid = productid).first()
        allProducts.productid = productid
        allProducts.product = product
        allProducts.desc = desc
        db.session.add(allProducts)
        db.session.commit()
        return redirect("/")
        
    allProducts = MyProduct.query.filter_by(productid = productid).first()
    return render_template('update.html', allProducts = allProducts)



if __name__ == "__main__":
    app.run(debug=True,port=7000)
