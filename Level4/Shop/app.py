from flask import *
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask("Shop")
app.config['MONGO_URI'] = 'mongodb://localhost:27017/shop'
mongo = PyMongo(app)
Bootstrap(app)


@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html')


@app.route('/sell', methods=['GET', 'POST'])
def sell():
    if request.method == 'GET':
        return render_template('sell.html')
    elif request.method == 'POST':
        mongo.db.shop.insert_one(dict(request.form))
        return redirect('/')


@app.route('/buy', methods=['GET', 'POST'])
def buy():
    if request.method == 'GET':
        return render_template('buy.html', prod=[dict(doc) for doc in list(mongo.db.shop.find({}))])
    elif request.method == 'POST':
        mongo.db.cart.insert_one(dict(request.form))
        return redirect('/cart')


@app.route('/cart', methods=['GET'])
def cart():
    if request.method == 'GET':
        docs = list(mongo.db.cart.find({}))[-1]
        l=[]
        tot = 0
        temp = {}
        for key in list(docs.keys())[1:]:
            temp = dict(list(mongo.db.shop.find({'_id':ObjectId(key)}))[0])
            temp['quantity'] = docs[key]
            temp['total'] = float(docs[key]) * float(temp['price'])
            tot+=float(docs[key]) * float(temp['price'])
            l.append(temp)
        return render_template('cart.html', prod_list=l, tot=tot)


@app.route('/empty',methods=['GET'])
def empty():
    if request.method == 'GET':
        mongo.db.cart.delete_many({})
        return redirect('/')


app.run(debug=True)
