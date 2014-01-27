import json

with open("data/linkedin-data-as-python-lists.txt", "r") as fp:
    data = fp.read()

json_data = json.loads(data)

for eachLst in json_data:
    for eachDict in eachLst:
        for eachAttr in eachDict:
            print '"' + unicode(eachDict[eachAttr]).encode('utf-8') + '",',
        print
