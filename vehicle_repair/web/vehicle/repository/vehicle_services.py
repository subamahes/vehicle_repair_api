#!/usr/bin/env python

import json

from vehicle.repository.connection import *


def select_details():
        sql = ("SELECT"
                " v._id," 
                " v.services," 
                " v.cost" 
                " from" 
                " vehicle.vehicle_services v"  
               )

        conn = db_connection()
        result = []

        with conn:
            cur = conn.cursor()
            cur.execute(sql)

            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            for row in rows:
                res = dict(
                    _id = row[0],
                    services=row[1],
                    cost= row[2]
                )
                result.append(res)
        cur.close()
        conn.close()
        return result

def select_details_with_services(service):
        sql = ("SELECT"
                " v.cost" 
                " from" 
                " vehicle.vehicle_services v"
                " where v.services = %s"  
               )

        conn = db_connection()
        result = []

        with conn:
            cur = conn.cursor()
            cur.execute(sql, (service,))

            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            for row in rows:
                result.append(row)
        cur.close()
        conn.close()
        return result[0][0]