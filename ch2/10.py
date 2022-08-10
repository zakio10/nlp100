with open('popular-names.txt') as f:
    s = f.read()

print("len :", len(s.rstrip().split("\n")))