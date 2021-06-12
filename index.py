try:
    import requests
    from flask import Flask
except ImportError:
    print("Unable to Import Modules")

app = Flask(__name__)

@app.route('/')
def index():
    res = requests.get('https://TechGeeks.pythonanywhere.com/')
    return res.content

@app.route('/<path:path>')
def routes(path):
    res = requests.get('http://TechGeeks.pythonanywhere.com/{}'.format(path))
    return res.content

if __name__=="__main__":
    app.run(port=5000)
