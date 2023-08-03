#!/usr/bin/env python

from flask import Blueprint
from flask import request

from vehicle.utils.json_display import StatusCode
from vehicle.service.customer_details import *

from vehicle.utils.json_display import *

blueprint = Blueprint('customer_details', __name__)


#
# http://127.0.0.1:5000/
#

@blueprint.route('/customer-details', methods=['GET'])
def customer_details():
    try:

        result = service_customer_details()
        code = StatusCode.OK

    except BaseException as ex:

        code = StatusCode.SERVER_ERROR
        result = dict(
            error_message='Unexpected error while finding the customer details.'
        )

    return build_json_response(code, result)

@blueprint.route('/customer-details/<vehilce_number>', methods=['GET'])
def customer_details_using_vehicle_number(vehilce_number):
    try:
        result = service_customer_details_with_vehicle_number(vehilce_number)
        code = StatusCode.OK

    except BaseException as ex:

        code = StatusCode.SERVER_ERROR
        result = dict(
            error_message='Unexpected error while finding the customer details.'
        )

    return build_json_response(code, result)


@blueprint.route('/customer-details', methods=['POST'])
def do_customer_details():
    try:
        req_json = request.get_json()
        result = post_service_customer_details(req_json)
        code = StatusCode.OK

    except BaseException as ex:

        code = StatusCode.SERVER_ERROR
        result = dict(
            error_message='Unexpected error while finding the customer details.'
        )

    return build_json_response(code, result)
    