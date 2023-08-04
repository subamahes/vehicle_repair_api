#!/usr/bin/env python

from vehicle.repository.customer_details import *


def service_customer_details():
    customer_details = select_details()
    
    return (customer_details)

def service_customer_details_with_vehicle_number(vehilce_number):
    customer_details = select_details_with_vehicle_number(vehilce_number)
    if customer_details == []:
        return 0
    else:
        return (customer_details)
    

def post_service_customer_details(req_json):
    customer_details = insert(req_json)
    
    return (customer_details)