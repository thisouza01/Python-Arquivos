import csv

with open('teste1.csv') as csvfile:
    reader = csv.reader(csvfile)
    for item in reader:
        print(item)