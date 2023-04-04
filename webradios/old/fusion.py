import glob, json, sys

res = []
for x in sys.argv[1:]:
    file = open(x)
    data = json.load(file)
    file.close()
    for s in data: res.append(s)
print(json.dumps(res, indent=4))
