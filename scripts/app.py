from flask import Flask
from flask import render_template
from datetime import datetime
from pymongo import MongoClient


app = Flask(__name__, static_url_path='/static')
app.config['MONGO_URI'] = 'mongodb://localhost:27017/TweetSearch'
mongo = MongoClient(app.config['MONGO_URI'])
db = mongo.TweetSearch
collection = db.TweetData

@app.route('/')
def hello_world():
    return render_template('index.html')

def index():
    db = mongo.TweetSearch 
    collection = db.TweetData 
    documents = collection.find()
    print(documents)
# def get_data():
#     data = list(collection.find({}, {'_id': 0})) 
#     return jsonify(data)


if __name__== "__main__":
    app.run(debug=True)