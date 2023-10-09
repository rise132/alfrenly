from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://Christiansimanjuntak:@christian123@cluster0.rglbdzz.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diary', methods=['GET'])
def show_diary():
    articles = list(db.diary.find({}, {'_id' : False}))
    return jsonify({'articles' : articles})
    
@app.route('/diary', methods=['POST'])
def save_diary():
    title_receive = request.form.get["title_give"]
    content_receive = request.form.get["content_give"]

    return jsonify({'msg':'Upload complete!'})
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)