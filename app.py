from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo
from flask import request

app = Flask(__name__)
app.config['MONGO_URI'] ='mongodb://localhost:27017/TweetSearch'
db=PyMongo(app).db
def search_keyword(keyword,data):
    video_data=[]
    for d in data:
        f=d.pop('_id')
    for key_outer,inner_dict in d.items():
        quoties=[inner_dict['tweet_text']]
        replies=[]
        if keyword in  inner_dict['tweet_text']:
            for key_inner,value in inner_dict['quoted_by'].items():
                quoties.append(value['tweet_text'])
            for key_inner,value in inner_dict['replied_by'].items():
                replies.append(value['tweet_text'])
            video_data.append([inner_dict['tweet_url'],quoties])
    return video_data
    # return 'Keyword not found'
@app.route('/')
def index():
    return render_template('search.html')
def clean_string(sentence):
    # Remove non-alphabetic characters and normalize to lowercase
    clean_sentence = ''.join(c.lower() for c in sentence if c.isalpha())
    # Remove non-ASCII characters
    clean_sentence = ''.join(c for c in clean_sentence if ord(c) < 128)
    return clean_sentence

@app.route('/search', methods=['GET'])
def hello_world():
    keyword = request.args.get('keyword', '')
    data = db.TweetData.find({})

    result = search_keyword(keyword, data)
    return render_template('search.html', video_data=result)

@app.route('/button_click', methods=['POST'])
def button_click():
        replies=[]
        button_id = request.form['button_id']
        data = db.TweetData.find({})
        for d in data:
            f=d.pop('_id')
        for key_outer,outer_dict in d.items():
            if clean_string(button_id) == clean_string(outer_dict['tweet_text']):
                for key_inner,value in outer_dict["replied_by"].items():
                    replies.append(value['tweet_text'])
            else:
                for key_inner,inner_dict in outer_dict['quoted_by'].items():
                    if clean_string(button_id) == clean_string(inner_dict['tweet_text']):
                        for key_inner,value in inner_dict["replied_by"].items():
                            replies.append(value['tweet_text'])
        return replies

if __name__== "__main__":
    app.run(debug=True)
