from flask import Flask
from flask import Response, jsonify, request
import db 

import os

app = Flask(__name__,static_url_path='/static', static_folder='web/static/images')
port = int(os.environ.get("PORT", 5000))
deb = os.environ.get("DEBUG", False)

@app.route('/')
def hello_world():
    return 'Flask Dockerized and deployed to Heroku'

@app.route('/trace')
def tr():
    longi = request.args.get('longi')
    lati = request.args.get('lati')
    return db.storedata(db.match(longi,lati))[0]

@app.route('/isup')
def server():
    message = {
        'status': 200,
        'message': 'Connected'
    }
    return jsonify(message)

@app.route('/pro')
def lookup():
    message = {
        'status' : 200,
        'product' : db.getobj(int(request.args.get('id')))
    }
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=deb,host='0.0.0.0',port=port)
