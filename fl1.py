import csv
import uuid
import random

def get_zip_codes():
    # list to store unique zip codes
    zip_codes = set()
    
    # open the CSV file
    with open('us_zip_codes.csv', 'r') as csvfile:
        # create a CSV reader object
        csv_reader = csv.reader(csvfile)

        # skip the header row
        next(csv_reader)

        # iterate over the rows
        for row in csv_reader:
            # add the zip code to the set
            zip_codes.add(row[3])

    # convert the set to a list
    zip_codes = list(zip_codes)

    return zip_codes

us_zip_codes = get_zip_codes()

def generate_zip_code():
    return str(random.choice(us_zip_codes))

# define the number of rows
num_rows = 1000000

# open a new csv file in write mode
with open('large_file.csv', 'w', newline='') as csvfile:
    # create a csv writer object
    csv_writer = csv.writer(csvfile)

    # write the header row
    csv_writer.writerow(['id', 'zip', 'type'])

    # write the data rows
    for i in range(num_rows):
        csv_writer.writerow([uuid.uuid4(), generate_zip_code(), random.randint(1, 100)])
