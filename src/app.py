from flask import Flask, make_response, jsonify, request
from flask_cors import CORS
import json
import pandas as pd
import requests
import datetime
from io import BytesIO
from functools import wraps
import threading
import logging


# Create App
app = Flask(__name__)

# Middlewares
CORS(app)

# Logging
def log(func):
    import logging
    logging.basicConfig(filename='./logs/cityInfo.log', level=logging.INFO)

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info('Hello')
        logging.info("methods = {} - URL = {}".format(kwargs, args))
        print('Yo')
        return func(*args, **kwargs)

    return wrapper

# Routes
@log
@app.route("/city", methods=["GET"])
def getCityInfo():
    '''
        Get information regarding a city
    '''

    df = pd.read_csv("./static/cities.csv", delimiter=",")

    if len(request.args) > 1:
        logging.error(f"Too many parameters")
        return make_response('Error: Too many arguments. Only one is needed', 400)
    else:
        for k in request.args.keys():
            if k in ['insee', 'name', 'postalCode', 'gps']:
                # return a list of dictionnaries
                result = df[df[k] == request.args[k].upper()].to_dict('records')
                # get only the dictionnary inside the list 
                result = result[0]
            else:
                logging.error(f"Parameter {k} invalid")
                return make_response("Error: Invalid parameters", 400)

    return make_response(result, 200)

@log
@app.route('/scrap', methods=['POST'])
def scrapData():
    """
    [summary]
    Download the csv files containing the list of cities in France
    """    
    URL = 'https://datanova.legroupe.laposte.fr/explore/dataset/laposte_hexasmal/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true'
    
    try:
        response = requests.get(URL, allow_redirects=True).content
        dataFrame = pd.read_csv(BytesIO(response), delimiter=';')
        dataFrame.columns=['insee','name','postalCode','ligne5','acheminement','gps']
        dataFrame.to_csv('./static/cities3.csv', index=False, columns=['insee','name','postalCode','gps'])

        return make_response('scraping cities data succeeded', 200)

    except Exception as err:
        print(err)
        return make_response('Error during scraping cities data', 400)
    


# Run server
if __name__ == "__main__":

    # Run the service
    app.run(port=9002, debug=True)


 