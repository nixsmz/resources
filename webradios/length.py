import json

file = open("stations.json")
data = json.load(file)
file.close()
print(len(data))
