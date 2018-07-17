
from flask         import Flask, render_template, request, redirect, url_for
from pymongo       import MongoClient
from bson.objectid import ObjectId 

app = Flask(__name__)

client     = MongoClient('localhost', 27017)
database   = client['flask_mongo'];
collection = database.books

@app.route('/')
def index():
    return render_template('main/home.html')

@app.route('/books/new', methods = ['GET'])
def new():
    return render_template('books/new.html')

@app.route('/books', methods = ['GET'])
def list():
    list_colletcion = collection.find()
    return render_template('books/list.html', books = list_colletcion)

@app.route('/books/<id>')
def listOne(id):
    data = collection.find_one({
        '_id': ObjectId(id)
    })
    return render_template('books/one.html', book = data)

@app.route('/books/create', methods = ['POST'])
def create():
    collection.insert_one({
        'name'    : request.form['name'    ],
        'subtitle': request.form['subtitle'],
        'isbn'    : request.form['isbn'    ]
    })
    return redirect(url_for('list'))

if __name__ == '__main__':
    app.run()