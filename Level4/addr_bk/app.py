from flask import *
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
from bson import ObjectId

app = Flask('Address Book')
app.config['MONGO_URI'] = 'mongodb://localhost:27017/addrBk'
Bootstrap(app)

mongo = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def addrbk():
    if request.method == 'GET':
        documents = mongo.db.addrBk.find()
        return render_template('page.html', addresses=documents)
    elif request.method == 'POST':
        document = {}
        for item in request.form:
            document[item] = request.form[item]
        mongo.db.addrBk.insert_one(document)
        return redirect('/')

@app.route('/delete/<identity>')
def delete(identity):
    mongo.db.addrBk.delete_one({'_id':ObjectId(identity)})
    return redirect('/')

app.run(debug=True)