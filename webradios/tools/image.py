import glob, json
from PIL import Image
from fatal import fatal

SIZE = (512,512)

def image_normalize(*args: str):
    imgfolder = args[0]
    if imgfolder[-1] != '/': imgfolder += '/'
    for filename in glob.glob(f'{imgfolder}*'):
        name = '.'.join(filename.split('/')[-1].split('.')[:-1])
        try:
            Image.open(filename).resize(SIZE).save(f"{imgfolder}{name}.png")
            print(f"OK - {filename}")
        except Exception as e: print(f"   - {filename} : {e}")

def image_verify(*args: str):
    jsonfile, imgfolder = args[0], args[1]
    jl = None
    try:
        with open(jsonfile) as file:
            jl = json.load(file)
            file.close()
    except: fatal("Error while reading JSON file.")
    if imgfolder[-1] != '/': imgfolder += '/'
    for obj in jl:
        try:
            if Image.open(f"{imgfolder}{obj['icon']}").size[:2] != SIZE:
                raise Exception("Size does not match !")
            print(f"OK - {obj['name']}")
        except Exception as e: print(f"   - {obj['name']} : {e}")
