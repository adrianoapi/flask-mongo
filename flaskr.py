
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client   = MongoClient('localhost', 27017)
database = client['flask_mongo'];

collection = database.collection_names(include_system_collections = False)

for col in collection:
    print col

@app.route('/')
def testing():
    return render_template('main/home.html')

if __name__ == '__main__':
    app.run()