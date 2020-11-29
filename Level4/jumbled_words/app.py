from flask import *
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
import random

app = Flask('Jubmbled Words')
Bootstrap(app)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/JW'
mongo = PyMongo(app)
answer = {}


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('page.html')
    elif request.method == 'POST':
        return redirect('/')


@app.route('/jumble', methods=['GET', 'POST'])
def jumble():
    if request.method == 'GET':
        return render_template('jumble.html')
    elif request.method == 'POST':
        mongo.db.JW.insert_one({'word': request.form['word'].strip().lower()})
        return redirect('/')


@app.route('/figureout', methods=['GET', 'POST'])
def figure():
    global answer
    message=''
    if request.method == 'GET':
        docs = list(mongo.db.JW.find())
        words = {doc['word']: ''.join(random.sample(list(doc['word']), len(doc['word']))) for doc in docs}
        if len(words)==0:
            message = 'OOPS. No words available. Please submit new words to jumble.'
        else:
            message = ''
        return render_template('figure.html', words=words, message=message)
    elif request.method == 'POST':
        answer = request.form
        if len(answer)==0:
            return redirect('/')
        else:
            return redirect('/result')


@app.route('/result', methods=['GET'])
def result():
    global answer
    count = 0
    if request.method == 'GET':
        for key, value in answer.items():
            if key == value:
                count += 1
    return render_template('result.html', raw=count, options=len(answer), percent=count * 100 / len(answer))



app.run(debug=True)