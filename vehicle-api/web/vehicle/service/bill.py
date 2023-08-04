#!/usr/bin/env python
GST = 0.18
DISCOUNT = 0.05
from vehicle.service.customer_details import *
from vehicle.service.vehicle_services import *

def vehicle_repair_bill(vehicle_owner_name, service):
    customer_details = select_details_with_vehicle_owner_name(vehicle_owner_name)

    cost = vehicle_services_cost(service)

    discount_amt = DISCOUNT * cost
    pay_cost = cost - discount_amt
    pay = pay_cost + (cost*GST)

    cost_to_pay = dict(
        cost = cost,
        discount = DISCOUNT,
        discount_amt = discount_amt,
        pay_cost_after_discount = pay_cost,
        gst = GST,
        pay_with_GST = pay
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
        cost = cost,
        gst = GST,
        pay_with_GST = pay
    )

    result=[]
    result.append(customer_details)
    result.append(cost_to_pay)

    return result