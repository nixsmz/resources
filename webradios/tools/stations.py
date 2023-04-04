import  unicodedata, requests, json, bs4
from bs4 import BeautifulSoup
from fatal import fatal

def stations_sort(*args: str):
    jsonfile, outputfile = args[0], args[1]
    jl = None
    try:
        with open(jsonfile) as file:
            jl = json.load(file)
            file.close()
    except: fatal("Error while reading JSON file.")
    order = sorted(sorted(jl, key=lambda x: x['name'].lower()), key=lambda y: y['country'].lower())
    try:
        with open(outputfile, 'w') as of: json.dump(order, of, indent=4)
    except: fatal("Error while writing to output file.")

def stations_length(*args: str):
    jsonfile = args[0]
    jl = None
    try:
        with open(jsonfile) as file:
            jl = json.load(file)
            file.close()
    except: fatal("Error while reading JSON file.")
    print(len(jl))

def stations_add(*args: str) -> list:
    jsonfile, htmlfile, country = args[0], args[1], args[2]
    if country is None: fatal("Country not specified.")
    def stations_add_url(div: bs4.element.Tag) -> str:
        try:
            for d in div.find_all('div'):
                for e in d.find_all('div'):
                    if 'sq emp' in e.get('class') or 'sq' in e.get('class'):
                        for f in e.find_all('div'):
                            if 'cn' in f.get('class') and f.string.lower() in ['mp3','wav']:
                                return e.get('title')
        except: pass
        return None
    content, jl = None, []
    try:
        with open(htmlfile, 'r') as file:
            content = file.read()
            file.close()
        with open(jsonfile) as file:
            for e in json.load(file): jl.append(e)
            file.close()
    except: fatal("Error while reading HTML file.")
    html, ret, mem = BeautifulSoup(content, 'html.parser').body, [], []
    for div in html.find_all('div'):
        try:
            if 'stnblock' in div.get('class'):
                title = str(unicodedata.normalize('NFKD', div.find('h3').string).encode('ascii', 'ignore').decode("ascii"))
                url = stations_add_url(div)
                ct = country.capitalize()
                if url is None: raise Exception()
                r = requests.get(url, stream=True, headers={"Range": "bytes=0-4096"}, timeout=3)
                if r.status_code == requests.codes.ok:
                    icon = f"{ct.lower()}_{title.lower().replace(' ','_')}.png"
                    if title not in mem:
                        if len(list(filter(lambda x: x.get('icon') == icon, jl))) == 0:
                            jl.append({
                                'name': title.capitalize(),
                                'country': ct,
                                'url': url,
                                'icon': icon,
                            })
                            mem.append(title)
                            print(f"Added: {title.capitalize()}, {ct}")
        except: pass
    return ret

def stations_connect(*args: str):
    jsonfile = args[0]
    jl = None
    try:
        with open(jsonfile) as file:
            jl = json.load(file)
            file.close()
    except: fatal("Error while reading JSON file.")
    for i in jl:
        try:
            r = requests.get(i.get('url'), stream=True, headers={"Range": "bytes=0-4096"}, timeout=5)
            if r.status_code == requests.codes.ok: print(f'OK - {i.get("name")}')
            else: print(f'   - {i.get("name")} (check: {i.get("url")})')
        except: print(f'   - {i.get("name")} (check: {i.get("url")})')
