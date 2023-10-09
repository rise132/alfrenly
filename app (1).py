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
    
    from datetime import datetime
    now = datetime.now()
    print(now)
    date_time = now.strftime("%Y-%m-%d-%H-%M-%S")
    print(date_time)
    extension = file.filename.split('.')[-1]
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'file-{mytime}.{extension}'
    
    file = request.files["file_give"]
    save_to = 'static/mypicture.jpg'
    file.save(save_to)
    save_to = f'static/{filename}'
    file.save(save_to)

    doc = {
    'file': filename,
    'title': title_receive,
    'content': content_receive
    }
    db.diary.insert_one(doc)

    return jsonify({'msg':'Upload complete!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)