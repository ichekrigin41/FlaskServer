from flask import Flask



#To RUN
#in cmd: export FLASK_APP=server.py
#in cmd: flask run 

app  = Flask(__name__)
@app.route("/")

def TestRouting():
    return "<p> Testing1 </p>"