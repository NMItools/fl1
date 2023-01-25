"""
# ==============================================================================
# Geospatial query timing research
# ==============================================================================

January 16, 2023

# Generate Input Task

- Create a CSV file with 1 million rows containing
[
    ID:          UUID;                // 36 char if stored or returned as a standard dash-separated
    US ZIP Code: string (5 char);     // There are about 42k distinct values, so expect to see 25 - 250 of each (Uniform distribution
    Type:        string (100 char);   // Randomly distributed across about 100 distinct values
]
"""

import csv
import uuid
import random
from datetime import datetime

import platform
import multiprocessing
import psutil

import cpuinfo

from colorama import init
from colorama import Fore, Back

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

def get_us_zip_codes():
    # list to store unique zip codes
    zip_codes = list()
    
    # open the CSV file
    with open('us_zip_codes2.csv', 'r') as csvfile:
        # create a CSV reader object
        csv_reader = csv.reader(csvfile)

        # skip the header row
        next(csv_reader)

        # iterate over the rows
        for row in csv_reader:
            # add the zip code to the set
            zip_codes.append(row)

    # convert the set to a list
    zip_codes = list(zip_codes)

    return zip_codes

def get_zip_code():
    return random.choice(us_zip_codes)

def create_csv():
    # open a new csv file in write mode
    with open('large_file.csv', 'w', newline='') as csvfile:
        # create a csv writer object
        csv_writer = csv.writer(csvfile)

        # write the header row
        csv_writer.writerow(['id', 'zip', 'type', 'lon','lat'])

        # write the data rows
        for i in range(num_rows):
            zip_data = get_zip_code()
            csv_writer.writerow([uuid.uuid4(), zip_data[2], random.randint(1, 100), zip_data[0], zip_data[1]])     

# prepare a list of ZIP codes 
us_zip_codes = get_us_zip_codes()

# define the number of rows
num_rows = 1000000

t1, tp1 = timestamp()[0], timestamp()[1]
print(f"{Fore.GREEN}Creation of CSV file with {num_rows} rows started at {tp1}")
create_csv()
t2, tp2 = timestamp()[0], timestamp()[1]
print(f"{Fore.GREEN}CSV file created for {round((t2 - t1).total_seconds(),1)} sec. at {tp2}")
print(specs())
