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
        'lmt': '10'
    }
    
    r = requests.get(
        "https://api.tenor.com/search?",params=params)

    if r.status_code == 200:
        results = r.json()
        gifs = results['results']
    else:
        gifs = None

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object
    
    # data = r.json()
    # print(data)
    
    
    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    return render_template("index.html", gifs=gifs)

if __name__ == '__main__':
    app.run(debug=True)
