s="paraparaparadise"
ss="paragraph"

x=[s[i:i+2] for i in range(len(s)-1)]
y=[ss[i:i+2] for i in range(len(ss)-1)]

print("x: ", x)
print("y: ", y)
print("set(x): ", set(x))
print("set(y): ", set(y))

print("set(x) | set(y) :", set(x) | set(y))
print("set(x) & set(y) :", set(x) & set(y))
print("set(x) \ set(y) :", set(x) - set(y)) # set(x) - set(y)

# 集合の演算
# https://www.javadrive.jp/python/set/index6.html