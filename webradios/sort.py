import json, sys

if len(sys.argv) != 2:
    print("JSON file missing.")
    exit(0)
file = open(sys.argv[1])
data = json.load(file)
file.close()
order = sorted(sorted(data, key=lambda x: x['name'].lower()), key=lambda y: y['country'].lower())
print(json.dumps(order, indent=4))
