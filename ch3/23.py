import json
import re

res = []
decoder = json.JSONDecoder()
with open('./jawiki-country.json', 'r') as f:
    line = f.readline()
    while line:
        res.append(decoder.raw_decode(line))
        line = f.readline()

# 参考URL
# https://www.nooozui.com/entry/20200110/1578612600
# https://qiita.com/yamaru/items/255d0c5dcb2d1d4ccc14
# https://qiita.com/FukuharaYohei/items/3b0df4d9893b98537e95
for d in res:
    if d[0]["title"] == "イギリス":
        pattern = r'^.*==.*==$'
        result = re.findall(pattern, d[0]["text"], re.MULTILINE)
        print(result)

for _ in result:
    count = len(str(re.findall(r'==(=*?)(?:.*).*$', _)[0])) + 1
    print(str(re.findall(r'==(=*?)(?:.*)', _)[0]))
    print(_, count)
