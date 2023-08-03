#!/usr/bin/env python
GST = 0.18

from vehicle.service.customer_details import *
from vehicle.service.vehicle_services import *

def vehicle_repair_bill(vehicle_owner_name, service):
    customer_details = select_details_with_vehicle_owner_name(vehicle_owner_name)

    cost = vehicle_services_cost(service)
    pay = cost + (cost*GST)
    cost_to_pay = dict(
        pay = pay
    )
    result=[]
    result.append(customer_details)
    result.append(cost_to_pay)
    print(result)
    return result
    
def vehicle_repair_bill_first(service, vehicle_number):

    customer_details = select_details_with_vehicle_number_for_date_of_service(vehicle_number)
    print(customer_details)
    cost = vehicle_services_cost(service)
    pay = cost + (cost*GST)

    cost_to_pay = dict(
        pay = pay
    )

    result=[]
    result.append(customer_details)
    result.append(cost_to_pay)

    return result