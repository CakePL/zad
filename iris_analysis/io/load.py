import csv


def load(filename):
    csvfile = open(filename, newline='')
    reader = csv.DictReader(csvfile)
    result = {key: [] for key in reader.fieldnames if key != 'variety'}
    for row in reader:
        for key in row:
            if key != 'variety':
                result[key].append(float(row[key]))
    return result


