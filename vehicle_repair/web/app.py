#!/usr/bin/env python

from flask import Flask

from vehicle.api import customer_details

from vehicle.api import vehicle_services

from vehicle.api import bill
from vehicle.api import home

app = Flask(__name__)

app.register_blueprint(customer_details.blueprint)

app.register_blueprint(vehicle_services.blueprint)
app.register_blueprint(bill.blueprint)

app.register_blueprint(home.blueprint)

@app.after_request
def after_request(response):
    headers = response.headers
    headers['Access-Control-Allow-*'] = '*'
    headers['Access-Control-Allow-Credentials'] = True
    headers['Access-Control-Allow-Headers'] = '*'
    headers['Access-Control-Expose-Headers'] = '*'
    headers['Access-Control-Allow-Methods'] = '*'
    headers['Access-Control-Allow-Origin'] = '*'
    headers['node-cache'] = 'Missed node-cache'
    return response


if __name__ == '__main__':
    app.run(debug=True)
