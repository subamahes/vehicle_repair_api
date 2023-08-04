#!/usr/bin/env python

import json

from vehicle.repository.connection import *


def select_details():
        sql = ("SELECT" 
                " c.vehicle_id," 
                " c.vehicle_number," 
                " c.vehicle_type,"
                " c.vehicle_model_number,"
                " c.vehicle_owner_name," 
                " c.phone_number," 
                " c.date_of_service" 
                " from"  
                " vehicle.customer_details c" 
                " order by c.vehicle_number"
               )
        print(sql)
        conn = db_connection()
        result = []

        with conn:
            cur = conn.cursor()
            cur.execute(sql)
            print(sql)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            for row in rows:
                res = dict(
                    vehicle_id = row[0],
                    vehicle_number=row[1],
                    vehicle_type= row[2],
                    vehicle_model_number=row[3],
                    vehicle_owner_name = row[4],
                    phone_number = row[5],
                    date_of_service = row[6]
                )
                result.append(res)
        cur.close()
        conn.close()
        return result


def select_details_with_vehicle_number(vehicle_number):
        sql = ("SELECT" 
                " c.vehicle_id," 
                " c.vehicle_number," 
                " c.vehicle_type,"
                " c.vehicle_model_number,"
                " c.vehicle_owner_name," 
                " c.phone_number," 
                " c.date_of_service" 
                " from"  
                " vehicle.customer_details c" 
                " where c.vehicle_number = %s" 
                " order by c.date_of_service DESC"
               )
        conn = db_connection()
        result = []

        with conn:
            cur = conn.cursor()
            cur.execute(sql, (vehicle_number,))
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]

            if rows != []:

                bas_detail = dict(
                        base_details = dict(
                            vehicle_number=rows[0][1],
                            vehicle_type= rows[0][2],
                            vehicle_model_number=rows[0][3],
                            vehicle_owner_name = rows[0][4],
                            phone_number = rows[0][5]
                        )
                    )
                result.append(bas_detail)

                for row in rows:
                    res = dict(
                        vehicle_id = row[0],
                        vehicle_number=row[1],
                        date_of_service = row[6]
                    )
                    result.append(res)

        cur.close()
        conn.close()
        return result

def select_details_with_vehicle_number_for_date_of_service(vehicle_number):
        sql = ("SELECT"  
                " c.date_of_service" 
                " from"  
                " vehicle.customer_details c" 
                " where c.vehicle_number = %s"
                " order by c.date_of_service DESC" 
               )
        conn = db_connection()
        result = []

        with conn:
            cur = conn.cursor()
            cur.execute(sql, (vehicle_number,))
            rows = cur.fetchall()
            
            columns = [desc[0] for desc in cur.description]
            
            if rows != []:
                result = dict(
                    date_of_service = rows[0][0]
                )

        cur.close()
        conn.close()

        return result

def select_details_with_vehicle_owner_name(vehicle_owner_name):
        sql = ("SELECT" 
               " DISTINCT c.vehicle_number,"
                " c.vehicle_id," 
                " c.vehicle_type,"
                " c.vehicle_model_number,"
                " c.vehicle_owner_name," 
                " c.phone_number," 
                " c.date_of_service" 
                " from"  
                " vehicle.customer_details c" 
                " where c.vehicle_owner_name = %s"
                " order by c.date_of_service DESC" 
               )
        conn = db_connection()
        result = []

        with conn:
            cur = conn.cursor()
            cur.execute(sql, (vehicle_owner_name,))
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            
            if rows != []:

                bas_detail = dict(
                        base_details = dict(
                            vehicle_number=rows[0][0],
                            vehicle_type= rows[0][2],
                            vehicle_model_number=rows[0][3],
                            vehicle_owner_name = rows[0][4],
                            phone_number = rows[0][5]
                        )
                    )
                result.append(bas_detail)

                for row in rows:
                    res = dict(
                        vehicle_id = row[1],
                        vehicle_number=row[0],
                        date_of_service = row[6]
                    )
                    result.append(res)

        cur.close()
        conn.close()

        return result


def insert(detail):
        sql = ('insert into vehicle.customer_details'
               ' ( vehicle_number,'
               ' vehicle_type,'
               ' vehicle_model_number,'
               ' vehicle_owner_name,'
               ' phone_number,'
               ' date_of_service)'
               ' values( %s, %s, %s,%s, %s, %s)'
               ' RETURNING *'
               ) 

        conn = db_connection()
        result = []
        with conn:
            cur = conn.cursor()
            print((detail["vehicle_type"]))
            cur.execute(sql, (detail["vehicle_number"],detail["vehicle_type"],detail["vehicle_model_number"],detail["vehicle_owner_name"],detail["phone_number"],detail["date_of_service"]))
            rows = cur.fetchall()
            
            columns = [desc[0] for desc in cur.description]

            for row in rows:
                res = dict(
                    vehicle_id = row[0],
                    vehicle_number=row[1],
                    vehicle_type= row[2],
                    vehicle_model_number=row[3],
                    vehicle_owner_name = row[4],
                    phone_number = row[5],
                    date_of_service = row[6]
                )
                result.append(res)

        cur.close()
        conn.close()
        return result[0] if len(result) == 1 else None