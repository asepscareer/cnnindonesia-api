from flask import Flask, jsonify
from src import base

app = Flask(__name__)
data = base.GetData()

@app.route('/')
def home():
    return jsonify({
        "status": 200,
        "total data": len(data.index()),
        "data": data.index()
    }), 200

@app.route('/nasional')
def nasional():
    return jsonify({
        "status": 200,
        "total data": len(data.nasional()),
        "data": data.nasional()
    }), 200

@app.route('/internasional')
def internasional():
    return jsonify({
        "status": 200,
        "total data": len(data.internasional()),
        "data": data.internasional()
    }), 200

@app.route('/ekonomi')
def ekonomi():
    return jsonify({
        "status": 200,
        "total data": len(data.ekonomi()),
        "data": data.ekonomi()
    }), 200

@app.route('/olahraga')
def olahraga():
    return jsonify({
        "status": 200,
        "total data": len(data.olahraga()),
        "data": data.olahraga()
    }), 200

@app.route('/teknologi')
def teknologi():
    return jsonify({
        "status": 200,
        "total data": len(data.teknologi()),
        "data": data.teknologi()
    }), 200

@app.route('/hiburan')
def hiburan():
    return jsonify({
        "status": 200,
        "total data": len(data.hiburan()),
        "data": data.hiburan()
    }), 200

@app.route('/gaya-hidup')
def social():
    return jsonify({
        "status": 200,
        "total data": len(data.social()),
        "data": data.social()
    }), 200