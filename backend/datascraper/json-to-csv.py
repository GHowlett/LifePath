import csv
import json

def fileDataAsVar(filename):
    with open(filename, "r") as fp:    
        data = fp.read()

    return data

json_data = fileDataAsVar("linkedin-formatted-to-json.txt")

print json.loads(json_data)