import requests,os
from flask import Flask, jsonify,render_template, request, redirect, url_for, session, logging
app = Flask(__name__)


with open('dictionary.txt', 'r') as myfile:
    data = myfile.read()
li = data.split("\n")
dic = {}
for i in li:
    vals = i.split("=")
    dic[vals[0]]=vals[1]


@app.route('/secondcontainer',methods=['POST'])
def receiveword():
    content = request.get_json(force=True)
    word = content['word']
    if word in dic:
        response = {word:dic[word]}
        return response
    else:
        response = {word : "Word not found in dictionary."}
        return response

        
if __name__ == '__main__':
    server_port = os.environ.get('PORT', '5001')
    app.run(debug=True, port=server_port, host='0.0.0.0')