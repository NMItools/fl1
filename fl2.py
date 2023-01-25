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
Lat The latitude of the random Position used for the query
Lon The longitude of the random Position used for the query
Radius The Radius in miles
Count_Time Execution time in milliseconds for the Query returning just the Row Count
Count The count of the number of rows returned by the Query
Data_Time Execution time in milliseconds for the Query returning all the Rows of data

Please test with at least 10 random Positions. So, the final Result table should have about 80 rows.

"""

import random
import psycopg2
from psycopg2 import sql
from datetime import datetime

# server = 'localhost'
server = '192.168.11.12'
db_port = 5435
baza = 'test_db'
db_user = 'postgres'
password = 'softdesk'
table_name = ''

def lon():
    # Longitude: -124.848974 to -66.885444
    return round(random.uniform(-124.848974, -66.885444), 6)

def lat():
    # Latitude:  24.396308 to 49.384358
    return round(random.uniform(24.396308, 49.384358), 6)

def db_connect():

    try:
        # PostgreSQL konekcija
        connection = psycopg2.connect(
            dbname=baza,
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
        db_status = (f" - Konekcija sa bazom nije moguća!\n"
                     f"   Da li je server '{server}' dostupan?\n"
                     f"   Funkcije za rad sa bazom podataka neće biti dostupne.")
        # sys.exit(1)
    else:
        db_status = f"Konekcija sa serverom '{server}' uspostavljena!"
        print(db_status)
        return cursor


def sql_1(lon, lat, radius, cursor):

    query = "SELECT public.cnt_within_dist('" + str(lon) + "','" + str(lat) + "', " + str(radius) + ");"

    print(query)
    cursor.execute(query)
    sql_result = cursor.fetchall()

    for row in sql_result:
        return row

cur = db_connect()

print(sql_1(lon(),lat(),1000,cur)[0])
