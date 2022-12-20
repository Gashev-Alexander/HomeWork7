from controller import *
greeting()
choice_todo()

import csv

with open('phone.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('phone.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)

import json

with open('phone.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('phone.json', 'w') as f:
    json.dump(rows, f)