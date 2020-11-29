from flask import *
from flask_pymongo import PyMongo

app = Flask("Login")
app.config['MONGO_URI'] = 'mongodb://localhost:27017/login'
mongo = PyMongo(app)


session = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    global session
    if request.method == 'GET':
        if len(session) == 0:
            return redirect('/login')
        else:
            return render_template('home.html', s=session)


@app.route('/reg', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('reg.html')
    elif request.method == 'POST':
        mongo.db.login.insert_one(dict(request.form))
        return redirect('/')


@app.route('/login', methods=['GET','POST'])
def login():
    global session
    if request.method == 'GET':
        return render_template('login.html', m='')
    elif request.method == 'POST':
        session = dict(request.form)
        docs = list(mongo.db.login.find({'email':session['email'], 'pass':session['pass']}))
        if len(docs) != 0:
            session = dict(docs[0])
            return redirect('/')
        else:
            return render_template('login.html', m='incorrect username/ password')


@app.route('/logout', methods = ['GET'])
def logout():
    global session
    if request.method == 'GET':
        session = []
        return redirect('/')

app.run(debug=True)