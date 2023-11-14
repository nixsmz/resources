import requests, json

URL = "https://gitlab.com/nixsmz/resources/-/raw/main/webradios/stations.json"

js = requests.get(URL).json()
ctry = sorted(list(set(x["country"] for x in js)))
for c in ctry:
    radios = filter(lambda x: x["country"] == c, js)
    with open(f"{c}.json", "w+") as file:
        json.dump(list(radios), file, indent=4)
with open("Countries.json", "w+") as f:
    json.dump(ctry, f, indent=4)
