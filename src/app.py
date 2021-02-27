from flask import Flask, make_response, jsonify, request
from flask_cors import CORS
import pandas as pd
import requests
import datetime
from io import BytesIO
from functools import wraps
import logging.config
import sys
import os

# Logger
logConfigPath = os.path.join(os.getcwd(), 'config', 'logging.ini')
logging.config.fileConfig(logConfigPath, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

# Create App
app = Flask(__name__)

# Middlewares
CORS(app)

# Logging


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("method -> {}".format(func.__name__, args))
        return func(*args, **kwargs)

    return wrapper

# Routes


@app.route('/')
@log
def helloWord():
    return make_response('Hello Word', 200)


@app.route("/city", methods=["GET"])
@log
def getCityInfo():
    '''
        Get information regarding a city
    '''

    df = pd.read_csv("./static/cities.csv", delimiter=",")
    try:
        if len(request.args) > 1:
            raise Exception(
                f'Too many parameters, only 1 argument is required, {len(request.args)} are given', 'Error: Too many arguments. Only one is needed')
        else:
            for k in request.args.keys():
                if k in ['insee', 'name', 'postalCode', 'gps']:
                    # return a list of dictionnaries
                    result = df[df[k] == request.args[k].upper()
                                ].to_dict('records')
                    # get only the dictionnary inside the list
                    if len(result) != 0:
                        print(result)
                        result = result[0]
                    else:
                        raise Exception(
                            f"Data not found with {k} = {request.args[k]}", f'Data not found with {k} = {request.args[k]}')
                else:
                    raise Exception(
                        f"Parameter '{k}' invalid", f"Error: Invalid parameters '{k}'")
        return make_response(result, 200)
    except Exception as err:
        logger.error(err.args[0])
        return make_response(err.args[1], 400)


@app.route('/scrap', methods=['POST'])
@log
def scrapData():
    """
    Download the csv files containing the list of cities in France
    """
    URL = 'https://datanova.legroupe.laposte.fr/explore/dataset/laposte_hexasmal/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true'

    try:
        response = requests.get(URL, allow_redirects=True).content
        dataFrame = pd.read_csv(BytesIO(response), delimiter=';')
        dataFrame.columns = ['insee', 'name',
                             'postalCode', 'ligne5', 'acheminement', 'gps']
        dataFrame.to_csv('./static/cities.csv', index=False,
                         columns=['insee', 'name', 'postalCode', 'gps'])

        return make_response('scraping cities data succeeded', 200)

    except Exception as err:
        print(err)
        return make_response('Error during scraping cities data', 400)


# Run server
if __name__ == "__main__":

    # Run the service
    app.run(port=9002, debug=True)
