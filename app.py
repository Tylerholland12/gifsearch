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

# api_key = 'LE2B769USEX5'
# gif_limit = 10
# gif_search_term = 'excited'
# request_gif = request.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %(gif_search_term, api_key, gif_limit))

# if request_gif.status_code == 200:
#     top_10_gifs = json.loads(request_gif.content)
#     pp = pprint.PrettyPrinter(indent=4)
#     print(top_10_gifs)
#     pp.pprint(top_10_gifs) #pretty prints the json file.
#     for i in range(len(top_10_gifs['results'])):
#         url = top_10_gifs['results'][i]['media'][0]['gif']['url'] #This is the url from json.
#         print (url)
#         urllib.request.urlretrieve(url, str(i)+'.gif') #Downloads the gif file.
# else:
#     top_10_gifs = None
@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
   
    q = request.args.get('query')
    print(q)
    params = {
        'q': q,
        'key': 'LE2B769USEX5',
        'lmt': 10
    }
    """Return homepage."""
    # TODO: Extract the query term from url using request.args.get() 
    r = requests.get(
        "https://api.tenor.com/search",params=params)

    
    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    

    # TODO: Make an API call to Tenor using the 'requests' library. For 
    # reference on how to use Tenor, see: 
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
