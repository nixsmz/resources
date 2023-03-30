from bs4 import BeautifulSoup
import unicodedata, requests, json, bs4, sys

def add_fatal(msg: str) -> None:
    print(f"\33[1;31mE\33[0m {msg}")
    exit(0)

def add_url(div: bs4.element.Tag) -> str:
    try:
        for d in div.find_all('div'):
            for e in d.find_all('div'):
                if 'sq emp' in e.get('class') or 'sq' in e.get('class'):
                    for f in e.find_all('div'):
                        if 'cn' in f.get('class') and f.string.lower() in ['mp3','wav']:
                            return e.get('title')
    except: pass
    return None

def add(filename: str) -> list:
    file = open(filename, "r")
    content = file.read()
    file.close()
    html, ret, mem = BeautifulSoup(content, 'html.parser').body, [], []
    for div in html.find_all('div'):
        try:
            if 'stnblock' in div.get('class'):
                title = str(unicodedata.normalize('NFKD', div.find('h3').string).encode('ascii', 'ignore').decode("ascii"))
                url = add_url(div)
                ct = filename.split('/')[-1].split('.')[0].capitalize()
                if url is None: raise Exception()
                r = requests.get(url, stream=True, headers={"Range": "bytes=0-4096"}, timeout=3)
                if r.status_code == requests.codes.ok:
                    if title not in mem:
                        ret.append({
                            'name': title.capitalize(),
                            'country': ct,
                            'url': url,
                            'icon': f"{ct.lower()}_{title.lower().replace(' ','_')}.png",
                        })
                        mem.append(title)
        except: pass
    return ret

if len(sys.argv) != 2: fatal("html file missing.")
print(json.dumps(add(sys.argv[1]), indent=4))
