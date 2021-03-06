import csv
import hashlib
import os
import pandas as pd
import random

import time

# def conversion(text):
#     hash_object = hashlib.md5(str.encode(str(text)))
#     md5_hash = hash_object.hexdigest()
#     return print("Order ID " + md5_hash)
#     # return print("Order ID " + str(text))

# start = time.time()
# print("Starting...")

# file_to_open = os.path.expanduser("~/Documents/SMPL/csv-processing/src/1.5mil-sales-records.csv")
# df = pd.read_csv(file_to_open)
# df["Order ID"] = df["Order ID"].map(conversion)

# end = time.time()
# print((end - start))



# data = [] #Buffer list 
# with open("CSV\\verliezen.csv", "rb") as input_file:
#     reader = csv.reader(input_file, delimiter=";")
#     for row in reader:
#         if row[-1] == 'amsterdam':
#             data.append(row)

# with open("the_new_csv.csv", "w+") as to_file:
#     writer = csv.writer(to_file, delimiter=";")
#     for new_row in data:
#         writer.writerow(new_row)


input_file = os.path.expanduser("~/Documents/SMPL/csv-processing/src/1.5mil-sales-records.csv")

root, ext = os.path.splitext(input_file)
output_file = root + '-new.csv'


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


def random_data_column_to_csv(input_file, output_file):
    n = sum(1 for line in open(input_file)) - 1 #number of records in file (excludes header)
    s = 300000 #desired sample size
    skip = sorted(random.sample(range(1,n+1),n-s)) #the 0-indexed header will not be included in the skip list
    df = pd.read_csv(input_file, skiprows=skip)
    df.to_csv(output_file, index=False)


# def random_data_column_to_csv(input_file, output_file):
#     # Open output_file in write mode
#     with open(output_file, 'w') as write_obj:
#         # Create a csv.writer object from the output file object
#         csv_writer = csv.writer(write_obj)
#         # Making data frame from csv file  
#         data = pd.read_csv(input_file)
#         # Generating one row  
#         sampleRows = data.sample(frac =.25) 
#         # Checking if sample is 0.25 times data or not
#         if (0.25*(len(data))== len(sampleRows)):
#             print( "Cool")
#             print(len(data), len(sampleRows))
#         # Read each row of the input csv file as list
#         for row in sampleRows:
#             # Write the row / list to the output file
#             csv_writer.writerow([row])


def separate_column_to_csv(input_file, output_file, row_index):
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


def conversionToMD5(number):
    hash_object = hashlib.md5(str.encode(str(number)))
    return hash_object.hexdigest()


header_of_new_col = 'MD5 Hash'
# default_text = 'Some Text'


# Add column with same text in all rows
# add_column_in_csv(input_file, output_file, lambda row, line_num: row.append(default_text))


# Add column to csv by merging contents from first & second column of csv
# add_column_in_csv(input_file, output_file, lambda row, line_num: row.append(row[0] + '__' + row[1]))


# Add the column in csv file with header
# add_column_in_csv(input_file, output_file, lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(conversionToMD5(row[6])))


# Separate column in csv to new csv file
# separate_column_to_csv(input_file, output_file, 6)


# Create MD5 hash in separate column
# input_file_test = os.path.expanduser("~/Documents/SMPL/csv-processing/src/1.5mil-sales-records-new.csv")
# root_test, ext_test = os.path.splitext(input_file_test)
# output_file_test = root_test + '-test.csv'

# add_column_in_csv(input_file_test, output_file_test, lambda row, line_num: row.append('MD5 Hash') if line_num == 1 else row.append(conversionToMD5(row[0])))




start = time.time()
print("Starting...")

random_data_column_to_csv(os.path.expanduser("~/Documents/SMPL/csv-processing/src/1.5mil-sales-records-new.csv"), os.path.expanduser("~/Documents/SMPL/csv-processing/src/1.5mil-sales-records-random.csv"))

end = time.time()
print((end - start))


# with open(File1) as r1, open(output, 'w') as w:
#     writer = csv.writer(w)
#     merge_from = csv.reader(r1)
#     # merge_to = csv.reader(r2)
#     # skip 1 line of headers
#     for _ in range(1):
#         next(merge_from)
#     for merge_from_row in merge_from:
#         # insert from col 0 as to col 0
#         merge_to_row.insert(0, merge_from_row[0])
#         # replace from col 1 with to col 3
#         merge_to_row[1] = merge_from_row[3]
#         # delete merge_to rows 5,6,7 completely
#         del merge_to_row[5:8]
#         writer.writerow(merge_to_row)