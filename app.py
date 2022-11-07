from flask import Flask, request, jsonify, redirect, send_from_directory

app = Flask(__name__)

usrs = {}


@app.route("/")
def hello_world():
    cluster_id = request.args.get('user')

    if cluster_id in usrs.keys():
        usrs[cluster_id] = usrs[cluster_id]+1
    else :
        usrs[cluster_id] = 1
        
    return jsonify(usrs)