import csv


def save(filename, lst):
    csvfile = open(filename, 'w', newline='')
    fieldnames = [key for key in lst[0]]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for x in lst:
        writer.writerow(x)
