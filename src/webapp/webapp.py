import json
import os

from flask import Flask, request, jsonify, render_template, redirect

src_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
app = Flask(__name__, static_folder=src_dir + '/static/', template_folder=src_dir + '/templates/')


def start_flask(debug=True):
    app.run(port=8080, debug=debug)


@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def home_page():
    return render_template('index.html')

#my compiler said there was an indentation error, and i dont know how to fix it so i just put a comment here so it can run --Epictitus
'''
@app.errorhandler(404)
def not_found(e):c
    path = request.path[1:]
    if '/../' not in path:
        if os.path.isfile('static' + request.path):
            response = app.send_static_file(path)
            response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
            response.headers["Pragma"] = "no-cache"
            response.headers["Expires"] = "0"
            response.headers['Cache-Control'] = 'public, max-age=0'
            return response

    return render_template("404.html"), 404
'''
