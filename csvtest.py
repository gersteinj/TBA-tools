import csv
items = []
for n in range(15):
    items.append(n)

with open('writetest.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(items)
