# Test of comparison
import csv
import hashlib
import os
import pandas as pd
import time

# 1. Get list of random data
# 2. Convert to MD5
# 3. Compare with hashed list, print out matching emails

current_directory = os.getcwd()
os.chdir(current_directory)
os.chdir('src/test')


def add_column_in_csv(input_file, output_file, transform_row):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = csv.reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = csv.writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)


# Pull a single column out to a new csv
def column_to_csv(input_file, output_file, row_index):
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = csv.reader(read_obj, delimiter = ',', lineterminator='\n')
        # Create a csv.writer object from the output file object
        csv_writer = csv.writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Write the row / list to the output file
            csv_writer.writerow([row[row_index]])


# Conversion to md5
def conversionToMD5(number):
    hash_object = hashlib.md5(str.encode(str(number)))
    return hash_object.hexdigest()


# Convert data in csv to md5
def convert_csv_data(input_file, output_file, column_name):
    df = pd.read_csv(input_file)
    df[column_name] = df[column_name].map(conversionToMD5)
    df.to_csv(output_file, index=False)


# Created big, hashed records to test against
# input_file = os.path.expanduser('~/Documents/SMPL/csv-processing/src/1.5mil-sales-records-new.csv')
# convert_csv_data(input_file, 'hashed-sales-records.csv', 'Order ID')


# Takes random sample and adds hashed column to it in new file
# add_column_in_csv('random-sales-records.csv', 'random-sales-records-h.csv', lambda row, line_num: row.append('MD5 Hash') if line_num == 1 else row.append(conversionToMD5(row[0])))


start = time.time()
print("Starting...")

# https://stackoverflow.com/questions/38252759/compare-csv-values-against-another-csv-and-output-results
def compare_and_output_results(comparison_file, master_hash_file):
    with open(master_hash_file) as hashes:
        hashes = csv.reader(hashes)
        hashes = set(row[0] for row in hashes)

    with open(comparison_file) as input_file:
        reader = csv.DictReader(input_file)
        with open('output-test.csv', 'w') as output_file:
            writer = csv.DictWriter(output_file, reader.fieldnames)
            writer.writeheader()
            writer.writerows(row for row in reader if row['MD5 Hash'] in hashes)

compare_and_output_results('random-sales-records-h.csv', 'hashed-sales-records.csv')


end = time.time()
print((end - start))