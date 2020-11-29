from flask import *
from flask_pymongo import PyMongo
from datetime import datetime
from bson import ObjectId

app = Flask('diary')
app.config['MONGO_URI'] = 'mongodb://localhost:27017/diary'
mongo = PyMongo(app)

session = {}


@app.route('/', methods=['GET', 'POST'])
def home():
    global session
    if request.method == 'GET':
        if len(session) == 0:
            return redirect('/login')
        else:
            return render_template('home.html', s=session, docs=list(mongo.db.entry.find({'user': session['user']})))
    elif request.method == 'POST':
        mongo.db.entry.insert_one(
            {'user': session['user'], 'entry': request.form['entry'], 'timestamp': datetime.now()})
        return render_template('home.html', s=session, docs=list(mongo.db.entry.find({'user': session['user']})))


@app.route('/login', methods=['GET', 'POST'])
def login():
    global session
    if request.method == 'GET':
        return render_template('login.html', message='')
    elif request.method == 'POST':
        doc = list(mongo.db.users.find({'user': request.form['user'], 'pass': request.form['pass']}))
        if len(doc) == 0:
            return render_template('login.html', message='login did not match')
        else:
            session = dict(doc[0])
            return redirect('/')


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'GET':
        return render_template('reg.html', message='')
    elif request.method == 'POST':
        doc = dict(mongo.db.users.find({'user': request.form['user']}))

        if len(doc) == 0:
            mongo.db.users.insert_one(dict(request.form))
            return redirect('/login')
        else:
            return render_template('reg.html', message='user already exists')


@app.route('/logout', methods=['GET'])
def logout():
    global session
    if request.method == 'GET':
        session = {}
        return redirect('/login')


@app.route('/delete/<identity>', methods=['GET'])
def delete(identity):
    mongo.db.entry.delete_one({'_id': ObjectId(identity)})
    return redirect('/')


app.run(debug=True)
