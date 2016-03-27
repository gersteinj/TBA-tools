import csv

data = [['team', 'founded', 'years active'],
        [1257, 2004, 9],
        [1626, 2005, 10]
        ]

with open('writetest.csv', 'w', newline='\n') as f:
    writer = csv.writer(f, delimiter=',')
    for row in data:
        writer.writerow(row)
