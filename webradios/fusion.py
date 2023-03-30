import glob, json

res = []
for x in glob.glob("ok/*.json"):
    file = open(x)
    data = json.load(file)
    file.close()
    for s in data: res.append(s)
print(json.dumps(res, indent=4))
