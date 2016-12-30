from bokeh import Scatter, output_file, show
import csv

file = open('batteries.csv', 'r', newline='')
csvreader = csv.reader(file)



file.close()
