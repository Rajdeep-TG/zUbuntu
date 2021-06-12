import sys

try:
    import requests
    import flask
except ImportError:
    print("Unable to Import Modules")
try:
    app = flask.Flask(__name__)

@app.route('/')
def index():
    res = requests.get('https://TechGeeks.pythonanywhere.com/')
    return res.content

@app.route('/<path:path>')
def routes(path):
    res = requests.get('http://TechGeeks.pythonanywhere.com/{}'.format(path))
    return res.content

if __name__=="__main__":
    app.run()
except Exception as e:
    print(sys.version)
    print("Flask version: " + flask.__version__)
    print("Exception: " + e)
