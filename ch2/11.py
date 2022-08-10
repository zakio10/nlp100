with open('popular-names.txt') as f:
    s = f.read()

s = s.replace("\t", " ")

with open('11py.txt', mode='w') as f:
    f.write(s)