import csv

rezult = {}

with open("C:\Crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2][6:10] == "2015":
            if row[5] not in rezult:
                rezult[row[5]] = 1
            else:
                rezult[row[5]] = rezult[row[5]] + 1

maxim = max(rezult.values())
for i, j in rezult.items():
    if j == maxim:
        print(i)


