from __future__ import print_function
import csv

testa = []
file = 'c.csv'
with open(file) as fh:
    rd = csv.DictReader(fh, delimiter=',') 
    for row in rd:
        testa.append(row)
        print(row)

testa