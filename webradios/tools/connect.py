import requests, json

with open('stations.json', 'r') as file:
    data = json.load(file)
    file.close()
for i in data:
    try:
        r = requests.get(i.get('url'), stream=True, headers={"Range": "bytes=0-4096"}, timeout=3)
        if r.status_code == requests.codes.ok: print(f'OK - {i.get("name")}')
        else: print(f'   - {i.get("name")} (check: {i.get("url")})')
    except: print(f'   - {i.get("name")} (check: {i.get("url")})')
