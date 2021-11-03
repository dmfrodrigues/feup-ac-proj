import csv
import sys

r = csv.reader(sys.stdin, delimiter=";")
w = csv.writer(sys.stdout, delimiter=";")
first = True
for row in r:
    if first:
        first = False

        birth_number_idx = row.index("birth_number")
        
        del row[birth_number_idx]
        
        row.append("birthdate")
        row.append("sex")

        birthdate_idx = row.index("birthdate")
        sex_idx = row.index("sex")
    else:
        birth_number = int(row[birth_number_idx])
        del row[birth_number_idx]

        y, m, d = (birth_number//10000)%100, (birth_number//100)%100, (birth_number//1)%100
        sex = "M"
        if m >= 50:
            m -= 50
            sex = "F"

        row.append("19{:02d}-{:02d}-{:02d}".format(y, m, d))
        row.append(sex)

    w.writerow(row)
