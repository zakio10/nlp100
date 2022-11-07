import json

res = []
decoder = json.JSONDecoder()
with open('./jawiki-country.json', 'r') as f:
    line = f.readline()
    while line:
        res.append(decoder.raw_decode(line))
        line = f.readline()

# https://www.nooozui.com/entry/20200110/1578612600
for d in res:
    if d[0]["title"] == "イギリス":
        print(d[0]["text"])