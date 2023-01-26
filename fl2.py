"""
Let's assume that US is a rectangle defined by the corners:

Lat     Lon
48.6    -120.5
31.0     -67.0

Each random Position must be within this rectangle. I.e. 48.6 > Lat > 31.0 and -120.5 < Lon < -67.0

For each random Position run 4 Queries with Radius values of 10, 20, 50, and 100 miles.

For each combination of Position and Radius perform a Query that returns just the count of result rows,
and another Query that returns the rows.

The result of each of the 8 Queries per Position should be reported as a CSV file with the following
headers and data:

Header Data
------ -----
Lat         - The latitude of the random Position used for the query
Lon         - The longitude of the random Position used for the query
Radius      - The Radius in miles
Count_Time  - Execution time in milliseconds for the Query returning just the Row Count
Count       - The count of the number of rows returned by the Query
Data_Time   - Execution time in milliseconds for the Query returning all the Rows of data

Please test with at least 10 random Positions. So, the final Result table should have about 80 rows.

"""

import random
import psycopg2
from datetime import datetime
import csv
from colorama import Fore
import platform
import multiprocessing
import psutil

import cpuinfo


# database connection parameters

server = 'localhost'
# server = '192.168.11.12'
db_port = 5435
database = 'test_db'
db_user = 'postgres'
password = 'softdesk'
table_name = ''

def specs():
    print("----------")
    print("OS       :" + str(platform.system())+ " " + str(platform.version()))
    print("CPU      :" + cpuinfo.get_cpu_info()['brand_raw'] + " - " + str(multiprocessing.cpu_count()) + " core(s)")
    print("CPU      :" + str(platform.processor()))
    print("RAM (GB) :" + str(round(psutil.virtual_memory().total / (1024.0 ** 3),0)))

def timestamp():
    time = datetime.now()
    time_hms = time.strftime("%H:%M:%S")
    return [time, time_hms]

def longitude():
    # Longitude limits: -124.848974 to -66.885444
    return round(random.uniform(-124.848974, -66.885444), 6)

def latitude():
    # Latitude limits:  24.396308 to 49.384358
    return round(random.uniform(24.396308, 49.384358), 6)

def db_connect():

    try:
        
        # PostgreSQL connection

        connection = psycopg2.connect(
            dbname=database,
            port=db_port,
            user=db_user,
            host=server,
            password=password
            )
        
        cursor = connection.cursor()

    except psycopg2.OperationalError as e:
        print(95*"=")
        print(95*"-")
        print(f"{e}")
        print(95*"-")
        db_status = (f" - Database connection failed!\n")
    else:
        db_status = f"Connected to '{server}' successfully!"
        print(db_status)
        return cursor


def sql_1(lon, lat, radius, cursor):

    query = "SELECT public.cnt_within_dist('" + str(lon) + "','" + str(lat) + "', " + str(radius) + ");"

    # print(query)
    cursor.execute(query)
    sql_result = cursor.fetchall()

    for row in sql_result:
        return row


def sql_2(lon, lat, radius, cursor):

    query = "SELECT * FROM public.rows_within_dist('" + str(lon) + "','" + str(lat) + "', " + str(radius) + ");"
    cursor.execute(query)
    # sql_result = cursor.fetchall()
    # for row in sql_result:
    #     try:
    #         print(row)
    #     except:
    #         return (0,0)

with open('report.csv', 'w', newline='') as csvfile:
    header = ['Lat', 'Lon', 'Radius', 'Count_Time', 'Count', 'Data_Time']
    rows = []
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
   
    cur = db_connect()
    print(f"{Fore.RED}Executing queries for 10 random points in USA...")
    t0, tp0 = timestamp()[0], timestamp()[1]
    
    for i in range(10):
        
        print(f"{Fore.CYAN} - Point " + str(i+1))
        
        radius = [10,20,50,100]
        lon = longitude()
        lat = latitude()
        
        for n in radius:
            
            print(f"{Fore.CYAN}   radius " + str(n) + "...")

            t1, tp1 = timestamp()[0], timestamp()[1]
            count = sql_1(lon, lat, n, cur)[0]
            t2, tp2 = timestamp()[0], timestamp()[1]
            sql_2(lon, lat, n, cur)
            t3, tp3 = timestamp()[0], timestamp()[1]
            row = [lat, lon, n, round((t2 - t1).total_seconds()*1000,1), count, round((t3 - t2).total_seconds()*1000,1)]
            rows.append(row)

    t, tp = timestamp()[0], timestamp()[1]
    print(f"{Fore.GREEN}Execution finished for {round((t - t0).total_seconds(),1)} sec.")
    csvwriter.writerows(rows)
    print(f"{Fore.WHITE}CSV report file created.")

cur.close()
print(specs())