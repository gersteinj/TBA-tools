import csv
my_dict = {1257: 9, 1626: 5, 1676: 6, 5624: 1}


with open('writetest.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for key, value in my_dict.items():
        writer.writerow([key, value])
