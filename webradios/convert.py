import glob, sys
from PIL import Image

SIZE = (512,512)

if len(sys.argv) != 2:
    print("No source folder.")

for filename in glob.glob(f'{sys.argv[1]}/*'):
    name = '.'.join(filename.split('/')[-1].split('.')[:-1])
    try:
        Image.open(filename).resize(SIZE).save(
            f"images/{name}.png"
        )
        print(f"OK - {filename}")
    except Exception as e: print(f"   - {filename} : {e}")
