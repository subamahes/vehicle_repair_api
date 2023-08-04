#!/usr/bin/env python

from flask import Blueprint
from flask import request

from vehicle.utils.json_display import StatusCode
from vehicle.service.bill import *

from vehicle.utils.json_display import *

blueprint = Blueprint('bill', __name__)


#
# http://127.0.0.1:5000/
#

@blueprint.route('/new-bill/', methods=['GET'])
def first_bill():
    try:
        req_data = request.args
        vehicle_number = req_data.get('vehicle_number', default=None, type=str)
        service = req_data.get('service', default=None, type=str)
        result = vehicle_repair_bill_first(service, vehicle_number)
        code = StatusCode.OK

    except BaseException as ex:

        code = StatusCode.SERVER_ERROR
        result = dict(
            error_message='Unexpected error while billing.'
        )

    return build_json_response(code, result)

@blueprint.route('/bill/', methods=['GET'])
def bill():
    try:
        req_data = request.args
        vehicle_owner_name = req_data.get('vehicle_owner_name', default=None, type=str)
        service = req_data.get('service', default=None, type=str)
        
        result = vehicle_repair_bill(vehicle_owner_name, service)
        code = StatusCode.OK

    except BaseException as ex:

        code = StatusCode.SERVER_ERROR
        result = dict(
            error_message='Unexpected error while billing.'
        )

    return build_json_response(code, result)
