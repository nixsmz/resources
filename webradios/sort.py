import json

file = open("stations.json")
data = json.load(file)
file.close()
order = sorted(sorted(data, key=lambda x: x['name']), key=lambda y: y['country'])
print(json.dumps(order, indent=4))
