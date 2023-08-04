#!/usr/bin/env python

from flask import Blueprint
from flask import request

from vehicle.utils.json_display import StatusCode
from vehicle.service.vehicle_services import *

from vehicle.utils.json_display import *

blueprint = Blueprint('vehicle_services', __name__)


#
# http://127.0.0.1:5000/
#

@blueprint.route('/vehicle-services', methods=['GET'])
def vehicle_services_api():
    try:

        result = vehicle_services()
        code = StatusCode.OK

    except BaseException as ex:

        code = StatusCode.SERVER_ERROR
        result = dict(
            error_message='Unexpected error while getting the vehicle services'
        )

    return build_json_response(code, result)
