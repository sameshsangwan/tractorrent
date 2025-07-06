from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://tractorrentdb:tractorrentdb@tractorrent-db.xw6h2ow.mongodb.net/?retryWrites=true&w=majority&appName=tractorrent-db")
db = client['tractorrent']
tractors = db['tractors']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add-tractor', methods=['GET', 'POST'])
def add_tractor():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        purpose = request.form['purpose']
        image = request.form['image']
        distance = request.form['distance']

        # Save to MongoDB
        tractor_data = {
            "name": name,
            "price": price,
            "purpose": purpose,
            "image": image,
            "distance": distance
        }
        tractors.insert_one(tractor_data)

        return "✅ Tractor added and saved to MongoDB!"
    return render_template('add_tractor.html')

if __name__ == '__main__':
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)