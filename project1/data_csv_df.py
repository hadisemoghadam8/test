
'''file = open(r"E:\practicing\project\test\project1\A.csv", 'rt')
spamreader = csv.reader(file, delimiter=' ', quotechar='|')

'''
import csv

with open(r"E:\practicing\project\test\project1\A.csv", 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open(r"E:\practicing\project\test\project1\A.csv", 'w') as new_file:
        fieldnames = ['Value', 'variable_name']

    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

    csv_writer.writeheader ()

    for line in csv_reader:
        csv_writer.writerow(line)
