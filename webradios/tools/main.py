from fatal import fatal
from stations import *
from image import *
import sys, os

options = {
    "add": {
        'opt': ['-a','--add'],
        'desc': 'Add stations from an HTML file.',
        'usage': '-a <json> <html> <country>',
        'f': stations_add
    },
    "connect": {
        'opt': ['-c','--connect'],
        'desc': 'Check stations availability of a JSON file.',
        'usage': '-c <json>',
        'f': stations_connect
    },
    "length": {
        'opt': ['-l','--length'],
        'desc': 'Get number of stations in a JSON file.',
        'usage': '-l <json>',
        'f': stations_length
    },
    "normalize": {
        'opt': ['-n','--normalize'],
        'desc': 'Normalize images of a folder.',
        'usage': '-n <img_folder>',
        'f': image_normalize
    },
    "sort": {
        'opt': ['-s','--sort'],
        'desc': 'Sort stations of a JSON file.',
        'usage': '-s <in_json> <out_json>',
        'f': stations_sort
    },
    "verify": {
        'opt': ['-v','--verify'],
        'desc': 'Check availability of stations images.',
        'usage': '-v <json> <img_folder>',
        'f': image_verify
    }
}

fname = os.path.basename(__file__)
if len(sys.argv) < 2: fatal("invalid number of arguments.")
if sys.argv[1] in ['-h','--help']:
    for x in options:
        print(f'{", ".join(options[x]["opt"])} :')
        print(f'\t{options[x]["desc"]}\n\tUsage: python3 {fname} {options[x]["usage"]}')
    exit(0)
for x in options:
    if sys.argv[1] in options[x]['opt']:
        try:
            print(sys.argv[2:])
            options[x]['f'](sys.argv[2:])
        except Exception as e : print(f'Usage: python3 {fname} {options[x]["usage"]} ({e})')
        exit(0)
