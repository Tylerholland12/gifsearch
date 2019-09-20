from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    q = request.args.get('query')
    print(q)
    params = {
        'q': q,
        'key': 'LE2B769USEX5',
        'lmt': '5'
    }
    
    r = requests.get(
        "https://api.tenor.com/v1/search",params=params)

    if r.status_code == 200:
        results = r.json()
        gifs = results['results']
       
    else:
        gifs = None

    return render_template("index.html", gifs=gifs)

if __name__ == '__main__':
    app.run(debug=True)
