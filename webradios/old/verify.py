import json, sys
from PIL import Image

SIZE = (512,512)

if len(sys.argv) != 2:
    print("No JSON file to read.")
    exit(0)

file = open(sys.argv[1])
for obj in json.load(file):
    try:
        if Image.open(f"images/{obj['icon']}").size[:2] != SIZE:
            raise Exception("Size does not match")
        print(f"OK - {obj['name']}")
    except Exception as e: print(f"   - {obj['name']} : {e}")
file.close()
