import csv
import json

f = open('linkedin-formatted-to-json.txt', 'r')
reader = csv.DictReader(f, fieldnames = ("end","name","title","industry","userid","start","type","desc"))
out = json.dumps([ row for row in reader ])
print out