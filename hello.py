from flask import flask

app = Flask(__name___)

@app.route('/')
def hello():
  return 'hello world'  