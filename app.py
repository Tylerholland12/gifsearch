from flask import Flask, render_template, request
import requests
import json
import giphy_client
from giphy_client.rest import ApiException
import urllib.request,urllib.parse,urllib.error
import pprint
# from app import app
# import unittest

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    q = request.args.get('query')
    print(q)
    params = {
        'q': q,
        'key': 'LE2B769USEX5',
        'lmt': 10
    }
    """Return homepage."""
    
    r = requests.get(
        "https://api.tenor.com/search?",params=params)

    # https://tenor.com/gifapi/documentation
    if r.status_code == 200:
        results = r.json()
        gifs = results['results']
        # trending_gifs = json.loads(r.content)
    else:
        gifs = None

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object
    
    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'


    return render_template("index.html", gifs=gifs)


# class AppTests(unittest.TestCase): 

#     # This runs implicitly before any tests are run
#     # We use this to set up our app before we test on it
#     def setUp(self):
#         # creates a test client
#         self.app = app.test_client()
#         # propagate the exceptions to the test client
#         self.app.testing = True

#     def test_home_status_code(self):
#         # sends HTTP GET request to the application
#         # on the specified path
#         result = self.app.get('/') 

#         self.assertIn(b'Hello', result.data)

#         # assert the status code of the response
#         self.assertEqual(result.status_code, 200) 


# if __name__ == '__main__':
#     unittest.main()

if __name__ == '__main__':
    app.run(debug=True)
