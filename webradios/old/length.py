import json, sys

if len(sys.argv) != 2:
    print("JSON file missing.")
    exit(0)
file = open(sys.argv[1])
data = json.load(file)
file.close()
print(len(data))
