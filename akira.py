#!/usr/bin/env python3
import csv

# NOTE: Class to define the blueprint of the provinces
class Province():
    def __init__(self, provid, name, dev):
        self.provid = provid
        self.name = name
        self.dev = dev
    # NOTE: Had to use __str__ to print the provinces, will change later
    def __str__(self):
        return(str(self.provid) +" "+ str(self.name) +" "+ str(self.dev))

with open('provinces.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        # NOTE: .strip was very useful here, so I don't end up with brackets in my list. YAY
        development = list([row[2].strip('('), row[3], row[4].strip(')')])
        province_id = row[0]
        province_name = str('"'+row[1]+'"')
        print(Province(province_id, province_name, development))
