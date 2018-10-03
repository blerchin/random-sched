#!/usr/bin/env python3

import yaml
import csv
import random

with open('data.yml') as f:
    data = yaml.load(f.read())
    people = data['people']
    dates = data['dates']

random.shuffle(people)

def get_person():
    if len(people) > 0:
        return people.pop()
    else:
        return "None"

schedule = [ (date, get_person()) for date in dates ]

with open('schedule.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Date', 'Name'])
    for row in schedule:
        writer.writerow(row)
