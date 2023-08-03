#!/usr/bin/env python

from vehicle.repository.vehicle_services import *


def vehicle_services():
    results = select_details()
    return(results)

def vehicle_services_cost(service):
    results = select_details_with_services(service)
    return(results)