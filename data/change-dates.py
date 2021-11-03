import csv
import sys

assert len(sys.argv) > 1

date_column_id = sys.argv[1]

r = csv.reader(sys.stdin, delimiter=";")
w = csv.writer(sys.stdout, delimiter=";")
keys = []
for row in r:
    if keys == []:
        keys = row
        date_idx = keys.index(date_column_id)
    else:
        date = int(row[date_idx])
        y, m, d = (date//10000)%100, (date//100)%100, (date//1)%100
        row[date_idx] = "19{:02d}-{:02d}-{:02d}".format(y, m, d)
    w.writerow(row)
