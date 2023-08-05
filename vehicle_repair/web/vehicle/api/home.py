#!/usr/bin/env python

from flask import Blueprint
from flask import request, render_template

from vehicle.utils.json_display import StatusCode

from vehicle.utils.json_display import *

blueprint = Blueprint('home' , __name__, template_folder="templates")


#
# http://127.0.0.1:5000/
#

@blueprint.route('/home', methods=['GET'])
def index():
    return render_template('index.html')

@blueprint.route('/customer-details/register', methods=['GET'])
def register():
    return render_template('register.html')

@blueprint.route('/services', methods=['GET'])
def vehicle_services():
    return render_template('services.html')

@blueprint.route('/bill', methods=['GET'])
def bill():
    return render_template('bill.html')

@blueprint.route('/bill-first', methods=['GET'])
def bill_first():
    return render_template('bill_new.html')
    