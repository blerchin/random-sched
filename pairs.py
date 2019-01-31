#!/usr/bin/env python3

import yaml
import csv
import math
import random

with open('data.yml') as f:
    data = yaml.load(f.read())
    people = data['people']

random.shuffle(people)
numPairs = math.ceil(len(people) / 2)

def get_person(list):
    if len(list) > 0:
        return list.pop()
    else:
        return "None"

pairs = [ (get_person(people), get_person(people)) for num in range(numPairs)]
interviewers = [pair[0] for pair in pairs]
random.shuffle(interviewers)
interviewees = [pair[1] for pair in pairs]
random.shuffle(interviewees)
pairs += [ (get_person(interviewees), get_person(interviewers)) for num in range(numPairs)]

with open('pairs.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Interviewer', 'Interviewee'])
    for row in pairs:
        writer.writerow(row)
