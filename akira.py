#!/usr/bin/env python3
import csv

# NOTE: Class to define the blueprint of the provinces
class Province():
    def __init__(self, provid, name, dev):
        self.provid = provid
        self.name = name
        self.dev = dev

    def __str__(self):
        return(str(self.provid) +" "+ str(self.name) +" "+ str(self.dev))


with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        province_id = row[0]
        province_name = str('"'+row[1]+'"')
        # NOTE: .strip was very useful here, so I don't end up with brackets
        # NOTE: in my list. YAY
        development = list([row[2].strip('('), row[3], row[4].strip(')')])

        print(Province(province_id, province_name, development))
