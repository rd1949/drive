import datetime
import time
from flask_cors import CORS

from flask import Flask, make_response, jsonify
import logging

from src.app.app import users_blueprint


logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
logger = logging.getLogger("rest_server_app")

app = Flask(__name__)
CORS(app)
app.register_blueprint(users_blueprint)




@app.route('/ping')
def ping():
    logger.info("application pinged...")
    return jsonify({'status': 'Welcome to Ylytic!'})

#
# @app.route('/secured-ping')
# @auth.login_required
# def secured_ping():
#     logger.info("application pinged...")
#     return jsonify({'status': 'Welcome to Secured Ylytic!'})
#
#
# @app.route('/authorised-ping')
# @auth.login_required(role=['ADMIN'])
# def authorised_ping():
#     logger.info("application pinged...")
#     return jsonify({'status': 'Welcome to Authorised Secured Ylytic!'})


if __name__ == '__main__':
    app.run()
